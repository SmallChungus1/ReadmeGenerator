# Apache Nano

The official CouchDB client for Node.js — a lightweight, powerful, and reliable library for interacting with CouchDB databases from within JavaScript applications.

---

## Description

Apache Nano is a robust, production-ready client library that enables Node.js applications to connect to, query, and manipulate CouchDB databases. Built with simplicity and performance in mind, Nano provides a clean, intuitive API for common database operations such as document CRUD (create, read, update, delete), view queries, replication, and bulk operations. It leverages the `request` module under the hood to handle HTTP communication with CouchDB, ensuring compatibility with the full range of CouchDB features.

Nano is designed to work seamlessly with both local development environments and cloud-hosted CouchDB instances. It supports advanced features like lazy database creation, automatic error recovery, and streaming of large attachments via `pipe()`.

---

## Features

- ✅ Full support for CouchDB's REST API (documents, views, attachments, changes, replication)
- ✅ Lazy database creation — automatically creates a database if it doesn't exist
- ✅ Automatic error handling and retry logic for transient failures
- ✅ Built-in support for bulk operations (insert, update, delete)
- ✅ Streaming of large attachments using Node.js `stream.pipe()`
- ✅ View support including spatial, search, and list views
- ✅ Session management and authentication via username/password
- ✅ Configurable logging and request interception
- ✅ Works with both local and remote CouchDB servers
- ✅ Compatible with Node.js versions >= 0.8.0

---

## Installation

Install Apache Nano using npm:

```bash
npm install nano@6.2.0
```

> **Note**: The library is compatible with Node.js versions 0.8.0 and above.

---

## Usage

### Basic Connection

Create a database connection to a CouchDB instance:

```javascript
const nano = require('nano')('http://localhost:5984');

// List all databases
nano.listDbs((err, dbs) => {
  if (err) console.error('Error listing databases:', err);
  else console.log('Databases:', dbs);
});

// Create a new database
nano.db.create('my_database', (err) => {
  if (err) console.error('Error creating database:', err);
  else console.log('Database created successfully!');
});
```

### Document Operations

Insert, retrieve, and update documents:

```javascript
const db = nano.use('my_database');

// Insert a document
db.insert({ name: 'John Doe', age: 30 }, 'doc1', (err, res) => {
  if (err) console.error('Insert failed:', err);
  else console.log('Document inserted:', res);
});

// Retrieve a document
db.get('doc1', (err, doc) => {
  if (err) console.error('Get failed:', err);
  else console.log('Retrieved document:', doc);
});

// Update a document
db.insert({ name: 'Jane Doe', age: 28 }, 'doc1', (err, res) => {
  if (err) console.error('Update failed:', err);
  else console.log('Document updated:', res);
});
```

### View Queries

Query documents using views:

```javascript
db.view('my_design_doc', 'by_age', { startkey: '20', endkey: '30' }, (err, result) => {
  if (err) console.error('View query failed:', err);
  else console.log('View results:', result.rows);
});
```

### Replication

Replicate data between databases:

```javascript
const master = nano('http://localhost:5984/master');
const replica = nano('http://localhost:5984/replica');

master.replicate(replica, { live: true }, (err, res) => {
  if (err) console.error('Replication failed:', err);
  else console.log('Replication successful:', res);
});
```

### Streaming Attachments

Stream large attachments directly to HTTP responses:

```javascript
const express = require('express');
const nano = require('nano')('http://localhost:5984');
const app = express();

app.get('/attachment', (req, res) => {
  nano.use('test').attachment.get('new', 'logo.png').pipe(res);
});

app.listen(3333);
console.log('Server running on port 3333');
```

### Lazy Database Creation with Retry

Automatically create databases and retry on failure:

```javascript
const { insert_with_retry, replicate_with_retry } = require('./examples/lazy_db_creation_and_replication');

insert_with_retry(nano.use('landing_m'), 'test@example.com', 3, (err, resp) => {
  if (err) console.error('Insert failed:', err);
  else console.log('Insert successful:', resp);
});
```

> 💡 See the full examples in the `examples/` directory for more advanced use cases.