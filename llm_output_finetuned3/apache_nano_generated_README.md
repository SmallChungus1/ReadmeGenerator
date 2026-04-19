# nano

The official CouchDB client for Node.js.

## Description

`nano` is a lightweight client library for interacting with CouchDB from Node.js. It provides a simple API to perform common database operations such as creating, reading, updating, and deleting documents, managing databases, and executing views.

## Features

- Create, destroy, and list databases
- Insert, retrieve, update, and delete documents
- Execute views and view-related operations (including spatial, search, and list views)
- Support for bulk operations and multipart attachments
- Built-in support for replication between databases
- Lazy database creation with retry logic
- Integration with Express.js for web-based applications

## Prerequisites / Requirements

- Node.js version 0.8.0 or higher
- CouchDB server running (default port 5984)

## Installation

```bash
npm install nano
```

## Usage

### Basic Database Operations

```javascript
const nano = require('nano')('http://localhost:5984');

// Create a database
nano.db.create('mydb', (err, response) => {
  if (err) console.error(err);
  else console.log('Database created');
});

// Insert a document
nano.db.insert({ name: 'John' }, 'doc1', (err, response) => {
  if (err) console.error(err);
  else console.log('Document inserted');
});

// Get a document
nano.db.get('doc1', (err, body) => {
  if (err) console.error(err);
  else console.log(body);
});

// List databases
nano.db.list((err, response) => {
  if (err) console.error(err);
  else console.log(response);
});
```

### Using with Express.js

```javascript
const express = require('express');
const db = require('nano')('http://localhost:5984/my_couch');
const app = express();

app.get('/', (req, res) => {
  db.get('foo', (error, body, headers) => {
    if (error) {
      res.status(error.statusCode);
      return res.send(error.message);
    }
    res.status(200).send(body);
  });
});

app.listen(3333);
console.log('Server is running on port 3333');
```

### Replication Example

```javascript
const nano = require('nano')({
  url: 'http://localhost:5984'
});

const master = nano('http://localhost:5984/landing_m');
const replica = nano('http://localhost:5984/landing_r');

master.replicate(replica, (err, response) => {
  if (err) console.error(err);
  else console.log('Replication successful');
});
```

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

The project uses:
- JSHint for JavaScript linting
- JSCS for code style enforcement
- Tape for unit testing
- Travis CI for continuous integration

To run tests locally:
```bash
npm test
```

## License

Apache License, Version 2.0

## Contact / Authors

Apache CouchDB <dev@couchdb.apache.org>  
Project homepage: http://github.com/apache/couchdb-nano  
Repository: git://github.com/apache/couchdb-nano