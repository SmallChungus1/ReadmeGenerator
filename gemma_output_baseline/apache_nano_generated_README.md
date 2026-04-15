```markdown
# Apache CouchDB Nano

[![Build Status](https://travis-ci.org/apache/couchdb-nano.svg?branch=master)](https://travis-ci.org/apache/couchdb-nano)

## Description

CouchDB Nano is the official CouchDB client for Node.js. It provides a simple and expressive API for interacting with CouchDB databases, making it easy to perform common operations like creating databases, inserting documents, querying data, and more. It's designed to be lightweight and flexible, suitable for a wide range of applications.

## Features

* **Simple API:** Easy to learn and use for common CouchDB operations.
* **Promise Support:** Supports promises for asynchronous operations.
* **Database Management:** Create, read, update, and delete databases.
* **Document Management:** Insert, read, update, and delete documents.
* **View Queries:** Execute complex queries using MapReduce views.
* **Bulk Operations:**  Efficiently insert, update, or delete multiple documents.
* **Authentication:** Supports user authentication.
* **Attachment Handling:**  Manage attachments associated with documents.
* **Replication:** Replicate databases between CouchDB instances.
* **Extensible:** Customizable with options for request configuration and logging.
* **Compact Support:** Manage database compaction.
* **Changes Feed:** Listen for changes in a database.
* **Multipart Support:** Handle multipart requests for attachments.

## Installation

```bash
npm install nano
```

## Usage

```javascript
const nano = require('nano')('http://localhost:5984');

// Create a database
nano.db.create('mydb', function(err) {
  if (err) {
    console.error('Error creating database:', err);
    return;
  }
  console.log('Database created successfully!');

  // Get a database object
  const db = nano.use('mydb');

  // Insert a document
  db.insert({ 'foo': 'bar' }, 'someid', function(err, body) {
    if (err) {
      console.error('Error inserting document:', err);
      return;
    }
    console.log('Document inserted successfully:', body);

    // Get the document
    db.get('someid', function(err, body) {
      if (err) {
        console.error('Error getting document:', err);
        return;
      }
      console.log('Document retrieved successfully:', body);
    });

  });
});
```

## API Reference

The Nano API consists of the following main components:

* **`nano(url, options)`:** Initializes a Nano instance, connecting to the specified CouchDB URL.
* **`nano.db`:** Provides methods for database management (create, destroy, list).
* **`nano.use(dbName)`:**  Returns a database object for interacting with a specific database.
* **`db.insert(doc, docId, options, callback)`:** Inserts or updates a document in the database.
* **`db.get(docId, options, callback)`:** Retrieves a document from the database.
* **`db.destroy(docId, rev, callback)`:** Deletes a document from the database.
* **`db.bulk(docs, options, callback)`:** Performs bulk insertion, update, or deletion of documents.
* **`db.view(ddoc, viewName, options, callback)`:** Executes a view query.
* **`db.compact(callback)`:** Compacts the database.
* **`db.changes(qs, callback)`:** Fetches changes in the database.
* **`db.followUpdates(qs, callback)`:**  Streams updates from the database.
* **`db.replicate(source, target, options, callback)`:**  Replicates a database.

## Contributing

Feel free to contribute to CouchDB Nano by submitting issues and pull requests on [GitHub](https://github.com/apache/couchdb-nano).

## License

Apache License 2.0. See [LICENSE](LICENSE) for more information.

## Development Notes
This documentation is based on commit `a10f6e6c337c761993c19cc8829bbf8cc9ba4c3a` as of March 4, 2026.  The code base includes comprehensive integration and unit tests.  The project benefits from extensive documentation and examples. The tests are located in the `/tests` directory, split into `integration` and `unit` folders and are invaluable for understanding expected functionality.