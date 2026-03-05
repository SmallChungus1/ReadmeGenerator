# Apache CouchDB Nano Client

[![Build Status](https://ci.apache.org/job/CouchDB/job/nano/badge/icon)](https://ci.apache.org/job/CouchDB/job/nano/)
[![Coverage Status](https://codecov.io/gh/apache/nano/branch/main/graph/badge.svg)](https://codecov.io/gh/apache/nano)

## Description

This repository contains the source code for the official CouchDB client for Node.js, known as `nano`.  It provides a fluent API for interacting with a CouchDB instance, simplifying tasks like database creation, document manipulation, view querying, and replication. Nano is designed for ease of use and integration into Node.js applications.  This version is based on the commit `a10f6e6c337c761993c19cc8829bbf8cc9ba4c3a` from March 4th, 2026.

## Features

*   **Fluent API:**  Easy-to-use methods for common CouchDB operations.
*   **Database Management:** Create, destroy, and manage CouchDB databases.
*   **Document Operations:** Insert, get, update, delete, and copy documents.
*   **View Querying:** Query CouchDB views with various options.
*   **Replication:**  Replicate databases between CouchDB instances.
*   **Attachment Handling:**  Manage attachments associated with documents.
*   **Bulk Operations:** Perform bulk inserts and updates for improved performance.
*   **Configuration:**  Customize the client with options like URL, request settings, and default headers.
*	**Middleware Support:**  Extensible with custom request middleware.
*   **Logging:** Built-in support for logging requests and responses.
*   **Support for cookie-based Authentication**
*  **Comprehensive testing suite** with both unit and integration tests.

## Installation

To install nano using npm:

```bash
npm install nano
```

## Usage

Here's a basic example of how to use nano:

```javascript
const nano = require('nano')('http://localhost:5984'); // Replace with your CouchDB URL

async function example() {
  try {
    // Create a database
    await nano.db.create('mydb');

    // Insert a document
    const response = await nano.db.insert('mydb', { name: 'John Doe', age: 30 });
    console.log('Document inserted:', response);

    // Get the document
    const doc = await nano.db.get('mydb', response.id);
    console.log('Document retrieved:', doc);

    // Destroy the database
    await nano.db.destroy('mydb');
  } catch (err) {
    console.error('Error:', err);
  }
}

example();
```

##  API Reference (Highlights)

*   `nano(url, [options])`: Creates a new nano client instance.
*   `nano.db.create(dbName, callback)`: Creates a database.
*   `nano.db.destroy(dbName, callback)`: Destroys a database.
*   `nano.db.insert(dbName, doc, callback)`: Inserts a document into a database.
*   `nano.db.get(dbName, docId, callback)`: Retrieves a document from a database.
*   `nano.db.list(dbName, options, callback)`: Lists all documents in a database.
*   `nano.db.view(dbName, viewName, options, callback)`: Queries a CouchDB view.
*   `nano.replicate(source, target, callback)`: Replicates a database.
*   `db.attachment.insert(dbName, docId, attName, data, contentType,callback)`: Inserts an attachment.

## Development

### Running Tests

To run the tests, execute:

```bash
npm test
```

This will run unit and integration tests.

### Contributing

Contributions are welcome! Please follow these guidelines:

*   Fork the repository.
*   Create a new branch for your feature or bug fix.
*   Write unit tests for your changes.
*   Submit a pull request.

## Dependencies

*   `request`: For making HTTP requests.
*   `errs`: For error handling.
*   `underscore`: For utility functions.
*   `debug`: For debugging output.
*   `follow`: For long polling
* `tape`/`tape-it`: For unit testing



## License

This project is licensed under the [Apache License 2.0](LICENSE).