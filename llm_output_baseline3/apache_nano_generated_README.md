# nano

## Description

The official CouchDB client for Node.js. This library provides a simple and powerful interface to interact with CouchDB databases, including operations for creating, reading, updating, and deleting documents, managing views, and replicating data between databases.

## Features

- Connect to CouchDB instances via HTTP
- Create, read, update, and delete documents
- Manage databases (create, destroy, list)
- Perform view queries and spatial searches
- Support for bulk operations and multipart attachments
- Built-in logging and error handling
- Lazy database creation and replication with retry logic
- Integration with Express.js for web applications

## Prerequisites / Requirements

- Node.js version `>=0.8.0`
- A CouchDB server running on a reachable URL (default: `http://localhost:5984`)

## Installation

```bash
npm install nano
```

## Usage

### Basic Connection

```javascript
const nano = require('nano')('http://localhost:5984');

// List databases
nano.listDbs((err, dbs) => {
  if (err) console.error(err);
  else console.log(dbs);
});

// Get a database
nano.getDb('mydb', (err, db) => {
  if (err) console.error(err);
  else console.log('Connected to database');
});
```

### Document Operations

```javascript
const db = nano.use('mydb');

// Insert a document
db.insert({ _id: 'doc1', name: 'John' }, (err, response) => {
  if (err) console.error(err);
  else console.log('Document inserted:', response);
});

// Get a document
db.get('doc1', (err, doc) => {
  if (err) console.error(err);
  else console.log('Document:', doc);
});

// Update a document
db.put({ _id: 'doc1', name: 'Jane' }, (err, response) => {
  if (err) console.error(err);
  else console.log('Document updated:', response);
});
```

### View Queries

```javascript
// Query a view
db.view('mydesign', 'myview', { keys: ['key1'] }, (err, result) => {
  if (err) console.error(err);
  else console.log('View result:', result);
});
```

### Replication

```javascript
// Replicate a database
db.replicate('http://localhost:5984/source', 'http://localhost:5984/destination', (err, result) => {
  if (err) console.error(err);
  else console.log('Replication complete:', result);
});
```

### Example: Lazy Database Creation

```javascript
const { insert_with_retry, replicate_with_retry } = require('./examples/lazy_db_creation_and_replication');

// Insert document with retry on missing database
insert_with_retry('mydb', 'email@example.com', 3, (err, resp, head) => {
  if (err) console.error('Failed to insert:', err);
  else console.log('Document inserted successfully');
});

// Replicate databases with retry on missing database
replicate_with_retry('http://localhost:5984/master', 'http://localhost:5984/replica', 3, (err, resp, head) => {
  if (err) console.error('Replication failed:', err);
  else console.log('Replication complete');
});
```

## Contributing

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with descriptive messages.
4. Push to your branch and open a pull request.

The project uses:
- JSHint for JavaScript linting
- JSCS for code style enforcement
- Tape for unit tests
- Travis CI for continuous integration

To run tests locally:
```bash
npm test
```

## License

Apache-2.0

## Contact / Authors

Apache CouchDB <dev@couchdb.apache.org>  
Project homepage: http://github.com/apache/couchdb-nano  
Repository: git://github.com/apache/couchdb-nano  
Version: 6.2.0