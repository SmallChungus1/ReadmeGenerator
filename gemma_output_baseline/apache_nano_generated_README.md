```markdown
# nano

![Apache License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)

The official CouchDB client for Node.js.

## Description

nano is a lightweight and performant JavaScript library for interacting with Apache CouchDB databases. It provides a simple and intuitive API for common CouchDB operations, making it easy to build applications that leverage the power of NoSQL document storage.  It's designed for Node.js environments and simplifies tasks like database creation, document management, view querying, and replication.

## Features

*   **Simple API:**  Provides a clean and easy-to-use interface for interacting with CouchDB.
*   **Lightweight:** Minimal dependencies and a small footprint.
*   **Comprehensive Functionality:** Supports a wide range of CouchDB features, including document CRUD operations, view queries, replication, and more.
*   **Configuration Options:**  Allows customization of request settings, URL parsing, and logging.
*   **Error Handling:** Robust error handling with detailed error messages.
*   **Streaming Support:** Enables efficient handling of large attachments and data streams.

## Table of Contents

*   [Prerequisites / Requirements](#prerequisites--requirements)
*   [Installation](#installation)
*   [Usage](#usage)
*   [Contributing](#contributing)
*   [License](#license)
*   [Contact / Authors](#contact--authors)

## Prerequisites / Requirements

*   Node.js version 0.8.0 or higher.

## Installation

To install nano, use npm:

```bash
npm install nano
```

## Usage

Here are a few examples of how to use nano:

**1. Connecting to CouchDB:**

```javascript
var nano = require('nano')('http://localhost:5984');
```

**2. Creating a Database:**

```javascript
nano.db.create('my_database', function(err) {
  if (err) {
    console.error(err);
  } else {
    console.log('Database created successfully!');
  }
});
```

**3. Inserting a Document:**

```javascript
var db = nano.use('my_database');
var doc = {
  _id: 'my_document',
  title: 'Example Document',
  content: 'This is an example document in CouchDB.'
};

db.insert(doc, function(err, body, headers) {
  if (err) {
    console.error(err);
  } else {
    console.log('Document inserted successfully!');
  }
});
```

**4. Getting a Document:**

```javascript
db.get('my_document', function(err, body, headers) {
  if (err) {
    console.error(err);
  } else {
    console.log('Document retrieved successfully:', body);
  }
});
```

**5. Using Express.js with nano:**

```javascript
var express = require('express')
   , db    = require('nano')('http://localhost:5984/my_couch')
   , app     = module.exports = express();

app.get('/', function(req, res) {
   db.get('foo', function (error, body, headers) {
      if(error) {
         res.status(error.statusCode);
         return res.send(error.message);
      }
      res.status(200);
      res.send(body);
   });
});

app.listen(3333);
console.log('server is running. check expressjs.com for more cool tricks');
```

Refer to the **examples** directory in the repository for more detailed usage scenarios, including bulk transformations, lazy database creation, and piping attachments.

## Contributing

We welcome contributions to nano! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to report bugs, submit feature requests, and contribute code.

## License

This project is licensed under the [Apache License, Version 2.0](LICENSE).

## Contact / Authors

Created by [Apache CouchDB <dev@couchdb.apache.org>](http://couchdb.apache.org).

For questions or support, please visit the [Apache CouchDB website](http://couchdb.apache.org) or engage with the community.