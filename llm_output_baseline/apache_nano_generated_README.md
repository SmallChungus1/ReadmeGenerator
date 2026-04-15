# nano.js — The Official CouchDB Client for Node.js

![Build Status](https://img.shields.io/travis/apache/couchdb-nano/master.svg?style=flat-square)
![Version](https://img.shields.io/npm/v/nano.svg?style=flat-square)
![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=flat-square)

> A lightweight, powerful, and reliable client for interacting with CouchDB from Node.js applications.

---

## Description

**nano.js** is the official Node.js client for [Apache CouchDB](https://couchdb.apache.org/). It provides a simple, intuitive, and feature-rich API for performing common database operations such as creating and managing databases, storing and retrieving documents, running views, and replicating data across servers.

Designed with simplicity and performance in mind, nano.js abstracts the complexity of HTTP requests and JSON payloads, allowing developers to focus on building robust data-driven applications. Whether you're building a microservice, a content management system, or a real-time data pipeline, nano.js offers the tools you need to work seamlessly with CouchDB.

---

## Features

- ✅ **Full CouchDB API support**: Create, read, update, and delete documents and databases.
- ✅ **View operations**: Query data using map/reduce views, spatial views, and search views.
- ✅ **Bulk operations**: Efficiently insert, update, or delete multiple documents at once.
- ✅ **Attachments**: Store and retrieve binary data (e.g., images, files) with full HTTP support.
- ✅ **Replication**: Synchronize data between CouchDB instances with retry logic.
- ✅ **Lazy database creation**: Automatically create databases when first accessed.
- ✅ **Error handling and logging**: Built-in error management and customizable logging strategies.
- ✅ **Cross-platform compatibility**: Works on all Node.js versions ≥ 0.8.0.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Prerequisites

- **Node.js** v0.8.0 or higher
- A running CouchDB instance (typically accessible at `http://localhost:5984`)
- Basic familiarity with JavaScript and asynchronous programming

> Note: The package is compatible with older Node.js versions, making it suitable for legacy systems and microservices.

---

## Installation

Install nano.js via npm:

```bash
npm install nano
```

To use it in your project, require the module:

```javascript
const nano = require('nano')('http://localhost:5984');
```

> Replace `http://localhost:5984` with your CouchDB server URL (e.g., `http://your-server:5984`).

---

## Usage Examples

### 1. Basic Document Operations

```javascript
const nano = require('nano')('http://localhost:5984');

// Insert a document
nano.insert({ _id: 'user-123', name: 'Alice', email: 'alice@example.com' }, function(err, response) {
  if (err) console.error('Error:', err);
  else console.log('Document inserted:', response);
});

// Retrieve a document
nano.get('user-123', function(err, doc) {
  if (err) console.error('Error:', err);
  else console.log('Document:', doc);
});
```

### 2. Using Views

```javascript
const nano = require('nano')('http://localhost:5984');

// Define a view
nano.db.create('users', function(err) {
  if (err) return console.error(err);
  
  nano.db.use('users').view('by-email', 'users', { 
    keys: ['alice@example.com'] 
  }, function(err, result) {
    if (err) return console.error(err);
    console.log('View result:', result);
  });
});
```

### 3. Bulk Operations

```javascript
const nano = require('nano')('http://localhost:5984');

const docs = [
  { _id: 'doc1', value: 1 },
  { _id: 'doc2', value: 2 },
  { _id: 'doc3', value: 3 }
];

nano.bulk(docs, function(err, response) {
  if (err) console.error('Bulk error:', err);
  else console.log('Bulk operation succeeded:', response);
});
```

### 4. Lazy Database Creation & Replication

```javascript
const nano = require('nano')('http://localhost:5984');

// Insert with retry (creates DB if missing)
const db = nano.use('my-db');
db.insert({ name: 'John' }, function(err, response) {
  if (err && err.message === 'no_db_file') {
    console.log('Database not found — creating...');
    // DB will be created automatically
  }
});

// Replicate data between servers
const master = nano('http://localhost:5984/master');
const replica = nano('http://localhost:5984/replica');
master.replicate(replica, function(err, response) {
  if (err) console.error('Replication failed:', err);
  else console.log('Replication successful:', response);
});
```

> See the full examples in the `examples/` directory for more advanced use cases.

---

## Contributing

We welcome contributions from the community! If you'd like to help improve nano.js, please follow these steps:

1. **Fork the repository** on GitHub.
2. **Create a feature branch** for your changes.
3. **Write tests** to validate your changes (see `tests/` directory).
4. **Submit a pull request** with a clear description of your changes.

Please ensure your code follows the project's style guidelines:
- Use **JSHint** and **JSCS** for code quality.
- Maintain consistent formatting and naming.
- Include unit tests for new features.

For reporting bugs or requesting features, please open an issue in the [GitHub Issues](https://github.com/apache/couchdb-nano/issues) section.

> 📚 See the [CONTRIBUTING.md](CONTRIBUTING.md) file for detailed contribution guidelines.

---

## License

This project is licensed under the **Apache License, Version 2.0**.

See the [LICENSE](LICENSE) file for details.

---

## Contact / Authors

- **Project Maintainers**: Apache CouchDB Team  
- **Email**: dev@couchdb.apache.org  
- **Website**: [https://couchdb.apache.org](https://couchdb.apache.org)  
- **GitHub Repository**: [https://github.com/apache/couchdb-nano](https://github.com/apache/couchdb-nano)

For questions, feedback, or support, please reach out to the Apache CouchDB community via the official channels or open an issue on GitHub.