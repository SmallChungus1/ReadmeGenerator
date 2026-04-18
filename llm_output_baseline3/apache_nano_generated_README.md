# nano

[![Build Status](https://travis-ci.org/apache/couchdb-nano.svg?branch=master)](https://travis-ci.org/apache/couchdb-nano)
[![Version](https://img.shields.io/npm/v/nano.svg)](https://www.npmjs.com/package/nano)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

The official **CouchDB client for Node.js** — a lightweight, powerful, and reliable library for interacting with CouchDB databases from within your Node.js applications.

---

## Description

`nano` is a simple and robust client library that enables Node.js developers to connect to, query, and manipulate CouchDB databases. Built on top of the `request` module, it provides a clean, intuitive API for performing common database operations such as creating and deleting databases, storing and retrieving documents, managing views, and replicating data across nodes.

This library is ideal for developers who need to build scalable, real-time data applications using CouchDB's document-oriented NoSQL model, with minimal boilerplate and maximum flexibility.

---

## Features

- ✅ **Simple, intuitive API** for database operations (create, read, update, delete)
- ✅ **Full support for CouchDB views and design documents**
- ✅ **Bulk operations** (bulk insert, bulk update, bulk delete)
- ✅ **Attachments support** (upload, download, and manage binary data)
- ✅ **Automatic database creation** with retry logic
- ✅ **Replication support** with automatic fallback on missing databases
- ✅ **Built-in error handling and logging**
- ✅ **Supports both synchronous and asynchronous operations**
- ✅ **Extensible** with custom request hooks and logging strategies

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Prerequisites

- **Node.js** version `>=0.8.0`
- A running **CouchDB** instance (typically accessible at `http://localhost:5984`)

> Note: `nano` does not require a CouchDB server to be installed locally. However, it will fail to connect if no server is available at the specified URL.

---

## Installation

Install `nano` via npm:

```bash
npm install nano
```

> This installs the core library. To use it in your project, simply require it in your Node.js application.

---

## Usage

### Basic Database Connection

```javascript
const nano = require('nano')('http://localhost:5984');

// Create a database (if it doesn't exist)
nano.db.create('my_database', (err, response) => {
  if (err) console.error('Error creating database:', err);
  else console.log('Database created successfully!');
});

// Insert a document
nano.db.insert({ _id: 'doc1', name: 'John Doe' }, 'my_database', (err, response) => {
  if (err) console.error('Error inserting document:', err);
  else console.log('Document inserted:', response);
});

// Retrieve a document
nano.db.get('doc1', 'my_database', (err, body) => {
  if (err) console.error('Error fetching document:', err);
  else console.log('Document retrieved:', body);
});
```

### Advanced Operations

```javascript
// Use views
nano.db.view('my_design_doc', 'my_view', { keys: ['john'] }, (err, result) => {
  if (err) console.error('View error:', err);
  else console.log('View results:', result);
});

// Replicate data between databases
nano.replicate('http://localhost:5984/source', 'http://localhost:5984/destination', (err, response) => {
  if (err) console.error('Replication failed:', err);
  else console.log('Replication successful:', response);
});

// Handle attachments
nano.db.attachment.get('doc1', 'image.png').pipe(response);
```

---

## Examples

### 1. Bulk Document Transformation

Transforms documents by removing fields before saving.

```javascript
// examples/bulk_transform.js
const db = require('nano')('http://localhost:5984/emails');
const async = require('async');

function update_row(row, cb) {
  const doc = row.doc;
  delete doc.subject;
  db.insert(doc, doc._id, (err, data) => {
    if (err) console.log('err at ' + doc._id);
    else console.log('updated ' + doc._id);
    cb(err);
  });
}

function list(offset) {
  offset = offset || 0;
  db.list({ include_docs: true, limit: 10, skip: offset }, (err, data) => {
    const total = data.total_rows;
    const rows = data.rows;
    if (offset === total) return;

    async.forEach(rows, update_row, () => {
      list(offset + 10);
    });
  });
}

list();
```

### 2. Express Server with CouchDB Integration

Serves a simple Express server that retrieves a document from CouchDB.

```javascript
// examples/express.js
const express = require('express');
const db = require('nano')('http://localhost:5984/my_couch');
const app = express();

app.get('/', (req, res) => {
  db.get('foo', (error, body, headers) => {
    if (error) {
      res.status(error.statusCode).send(error.message);
    } else {
      res.status(200).send(body);
    }
  });
});

app.listen(3333);
console.log('Server is running on port 3333');
```

### 3. Lazy Database Creation and Replication

Automatically creates databases and replicates data with retry logic.

```javascript
// examples/lazy_db_creation_and_replication.js
const nano = require('nano');

const couch = {
  master: 'http://localhost:5984/landing_m',
  replica: 'http://localhost:5984/landing_r'
};

function insert_with_retry(db, email, retries, callback) {
  if (typeof retries === 'function') {
    callback = retries;
    retries = 0;
  }
  db.insert(email, (err, resp, head) => {
    if (err && err.message === 'no_db_file' && retries < 1) {
      const db_name = db.config.db;
      const server = nano(db.config.url);
      server.db.create(db_name, (err2, resp2, head2) => {
        if (err2) return callback(err2, resp2, head2);
        insert_with_retry(db, email, retries + 1, callback);
      });
    } else {
      callback(err, resp, head);
    }
  });
}

function replicate_with_retry(master_uri, replica_uri, retries, callback) {
  if (typeof retries === 'function') {
    callback = retries;
    retries = 0;
  }
  const master = nano(couch.master);
  master.replicate(couch.replica, (err, resp, head) => {
    if (err && err['error'] === 'db_not_found' && retries < 1) {
      const replica = nano(couch.replica);
      const db_name = replica.config.db;
      const server = nano(replica.config.url);
      server.db.create(db_name, (err2, resp2, head2) => {
        if (err2) return callback(err2, resp2, head2);
        replicate_with_retry(master_uri, replica_uri, retries + 1, callback);
      });
    } else {
      callback(err, resp, head);
    }
  });
}

module.exports = { insert: insert_with_retry, replicate: replicate_with_retry };
```

---

## Contributing

We welcome contributions to improve `nano`! Please follow these steps:

1. Fork the repository on GitHub.
2. Create a new feature branch (`feature/your-feature-name`).
3. Commit your changes with clear, descriptive messages.
4. Push to the branch and open a pull request.

Please ensure your code:
- Follows the existing code style (JavaScript, consistent indentation)
- Includes tests where applicable
- Is documented with comments
- Passes all existing tests (`npm test`)

For bug reports or feature requests, please open an issue in the [GitHub Issues](https://github.com/apache/couchdb-nano/issues).

> See the [CONTRIBUTING.md](CONTRIBUTING.md) file for detailed guidelines.

---

## License

This project is licensed under the **Apache License, Version 2.0**. See the [LICENSE](LICENSE) file for details.

---

## Contact / Authors

**Project Maintainers**: Apache CouchDB Team  
Email: `dev@couchdb.apache.org`  
Website: [http://couchdb.apache.org](http://couchdb.apache.org)

For questions or support, please reach out to the Apache CouchDB community via:
- [Apache CouchDB Mailing Lists](https://lists.apache.org/list.html?couchdb)
- [GitHub Issues](https://github.com/apache/couchdb-nano/issues)
- [Apache CouchDB Slack Community](https://couchdb.apache.org/slack)

> This project is part of the Apache CouchDB ecosystem and is maintained under the Apache Software Foundation.