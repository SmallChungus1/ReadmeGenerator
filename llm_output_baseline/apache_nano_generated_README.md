# nano

## Description

**nano** is the official Node.js client for Apache CouchDB. It provides a simple, powerful, and lightweight interface to interact with CouchDB databases, enabling developers to perform common operations such as creating, reading, updating, and deleting documents, managing views, and replicating data across servers.

Built with a clean API and designed for both simplicity and flexibility, nano abstracts the complexity of HTTP requests to CouchDB, allowing developers to work with data using familiar JavaScript syntax. It supports features like bulk operations, view queries, document attachments, and automatic database creation.

## Features

- **Database Operations**: Create, destroy, list, and get databases.
- **Document Management**: Insert, retrieve, update, delete, and copy documents with full revision tracking.
- **View Queries**: Query documents via map-reduce views, including spatial, search, and list views.
- **Bulk Operations**: Perform batch inserts and updates efficiently.
- **Attachments**: Store and retrieve binary attachments (e.g., images, files) with support for streaming.
- **Automatic Database Creation**: Automatically create databases if they don't exist.
- **Replication**: Replicate data between CouchDB instances with retry logic.
- **Error Handling**: Comprehensive error handling with meaningful messages and structured responses.
- **Flexible Configuration**: Customizable request settings, authentication, logging, and URL parsing.

## Installation

To install nano using npm:

```bash
npm install nano
```

> **Note**: This package requires **Node.js v0.8.0 or higher**.

## Usage

### Basic Setup and Document Operations

```javascript
const nano = require('nano')('http://localhost:5984');

// Create a database (if it doesn't exist)
nano.db.create('my_database', (err, response) => {
  if (err) {
    console.error('Error creating database:', err);
  } else {
    console.log('Database created successfully:', response);
  }
});

// Insert a document
const doc = { _id: 'doc1', name: 'John Doe', age: 30 };
nano.db.insert(doc, (err, response) => {
  if (err) {
    console.error('Error inserting document:', err);
  } else {
    console.log('Document inserted:', response);
  }
});

// Retrieve a document
nano.db.get('doc1', (err, body) => {
  if (err) {
    console.error('Error fetching document:', err);
  } else {
    console.log('Document retrieved:', body);
  }
});

// List all documents
nano.db.list({ include_docs: true }, (err, data) => {
  if (err) {
    console.error('Error listing documents:', err);
  } else {
    console.log('Documents:', data.rows);
  }
});
```

### Using Views

```javascript
// Define a view to count users by age group
nano.db.use('my_database').view('users', 'by_age', {
  keys: [18, 30, 45],
  reduce: true
}, (err, result) => {
  if (err) {
    console.error('Error querying view:', err);
  } else {
    console.log('View result:', result);
  }
});
```

### Bulk Operations

```javascript
const docs = [
  { _id: 'doc2', name: 'Jane Smith', age: 25 },
  { _id: 'doc3', name: 'Bob Johnson', age: 35 }
];

nano.db.bulkInsert(docs, (err, response) => {
  if (err) {
    console.error('Error in bulk insert:', err);
  } else {
    console.log('Bulk insert successful:', response);
  }
});
```

### Replication Example

```javascript
const source = nano('http://localhost:5984/source');
const target = nano('http://localhost:5984/target');

source.replicate(target, { create_target: true }, (err, response) => {
  if (err) {
    console.error('Replication failed:', err);
  } else {
    console.log('Replication successful:', response);
  }
});
```

### Streaming Attachments

```javascript
const app = require('express')();
const db = nano.use('test');

app.get('/attachment', (req, res) => {
  db.attachment.get('doc1', 'logo.png').pipe(res);
});

app.listen(3333);
console.log('Server running on port 3333');
```

> ✅ **Note**: All examples assume a running CouchDB instance accessible at `http://localhost:5984`. Adjust URLs and database names as needed for your environment.