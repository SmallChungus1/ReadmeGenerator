# Apache Nano

[![Build Status](https://img.shields.io/travis/apache/nano/master.svg?style=for-the-badge)](https://travis-ci.org/apache/nano)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=for-the-badge)](https://www.apache.org/licenses/LICENSE-2.0)
[![Version](https://img.shields.io/npm/v/nano.svg?style=for-the-badge)](https://www.npmjs.com/package/nano)

**The official CouchDB client for Node.js.**  
A lightweight, powerful, and easy-to-use library for interacting with CouchDB databases from within Node.js applications.

---

## Description

Apache Nano is a native Node.js client designed to provide seamless access to CouchDB's RESTful API. It enables developers to perform common database operations such as creating, reading, updating, and deleting documents, managing views, replicating databases, and handling attachments—all with minimal code and maximum flexibility.

Whether you're building a simple data store, a real-time application, or a distributed system, Nano offers a clean, intuitive interface that works reliably across versions of CouchDB and Node.js.

This project is maintained by the Apache CouchDB community and is actively used in production environments for data persistence and synchronization.

---

## Features

- ✅ **Full CouchDB API support** including documents, views, attachments, and replication  
- ✅ **Automatic database creation** with fallback retry logic  
- ✅ **Bulk operations** for efficient document insertion and transformation  
- ✅ **View support** with full query capabilities (including spatial and search views)  
- ✅ **Streaming attachments** via `pipe()` for efficient file transfers  
- ✅ **Error handling and logging** with configurable debug output  
- ✅ **Lazy database creation** — databases are created only when needed  
- ✅ **Cross-platform compatibility** with Node.js v0.8+  
- ✅ **Extensible configuration** via custom request/follow agents and logging strategies  

---

## Table of Contents

- [Prerequisites / Requirements](#prerequisites--requirements)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

---

## Prerequisites / Requirements

- **Node.js** version `>= 0.8.0`
- **CouchDB** server running (default port: `5984`)
- Basic understanding of Node.js and asynchronous programming

> 💡 *Nano works with any CouchDB instance accessible via HTTP. No additional setup required beyond starting CouchDB.*

---

## Installation

Install Apache Nano using npm:

```bash
npm install nano
```

> ⚠️ Ensure that CouchDB is running locally or on a remote server before using Nano.

---

## Usage Examples

### 1. Basic Document Operations

```javascript
const nano = require('nano')('http://localhost:5984/mydb');

// Insert a document
nano.insert({ name: 'John Doe', age: 30 }, 'doc1', (err, body) => {
  if (err) console.error(err);
  else console.log('Document inserted:', body);
});

// Get a document
nano.get('doc1', (err, body) => {
  if (err) console.error(err);
  else console.log('Document retrieved:', body);
});

// Delete a document
nano.destroy('doc1', (err) => {
  if (err) console.error(err);
  else console.log('Document deleted');
});
```

---

### 2. Bulk Document Transformation

Transform and update multiple documents in bulk:

```javascript
const db = require('nano')('http://localhost:5984/emails');
const async = require('async');

function update_row(row, cb) {
  const doc = row.doc;
  delete doc.subject;
  db.insert(doc, doc._id, (err, data) => {
    if (err) {
      console.log('Error updating:', doc._id);
      cb(err);
    } else {
      console.log('Updated:', doc._id);
      cb();
    }
  });
}

function list(offset) {
  offset = offset || 0;
  db.list({ include_docs: true, limit: 10, skip: offset }, (err, data) => {
    if (err) {
      console.log('Error:', err.message);
      return;
    }

    const total = data.total_rows;
    const rows = data.rows;

    if (rows.length === 0 || offset >= total) {
      return;
    }

    async.forEach(rows, update_row, () => {
      list(offset + 10);
    });
  });
}

list();
```

---

### 3. Express.js Integration

Serve a simple Express server with CouchDB access:

```javascript
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
console.log('Server is running on http://localhost:3333');
```

---

### 4. Lazy Database Creation & Replication

Create databases and replicate data automatically on failure:

```javascript
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
  callback = callback || function() {};

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
  callback = callback || function() {};

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

We welcome contributions from the community! Please follow these guidelines:

- ✅ Open issues or feature requests on GitHub
- ✅ Submit pull requests with clear descriptions
- ✅ Ensure all code passes linting and tests
- ✅ Update documentation when adding new features

For detailed contribution workflows, please refer to our [CONTRIBUTING.md](CONTRIBUTING.md) file.

> 📝 **Note**: All contributions are subject to the [Apache License 2.0](LICENSE).

---

## License

Apache Nano is licensed under the **Apache License 2.0**.  
See the [LICENSE](LICENSE) file for details.

---

## Contact / Authors

**Project Maintainers**: Apache CouchDB Community  
**Email**: dev@couchdb.apache.org  
**Website**: [https://couchdb.apache.org](https://couchdb.apache.org)

For questions, feedback, or support:
- Visit the [Apache CouchDB GitHub Repository](https://github.com/apache/couchdb-nano)
- Join the [Apache CouchDB mailing list](https://lists.apache.org/list.html?dev@couchdb.apache.org)
- Follow us on [Twitter](https://twitter.com/apache_couchdb)

> This project is part of the Apache Software Foundation ecosystem and is developed and maintained by volunteers from the global CouchDB community.