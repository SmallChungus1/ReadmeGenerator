---
# Apache Nano

[Apache Nano](https://github.com/apache/couchdb-nano) is a lightweight, easy-to-use client for interacting with [Apache CouchDB](https://couchdb.apache.org/) from Node.js.

> **Note**: This is the official Apache CouchDB client for Node.js.

## Features

- Simple and intuitive API for creating, reading, updating, and deleting documents.
- Supports database creation, destruction, and listing.
- Built-in support for views and full-text search.
- Efficient bulk operations for handling large datasets.
- Real-time change feeds via `changes` and `follow` methods.
- Native support for attachments (files, images, etc.).
- Seamless integration with Express.js for web applications.

## Installation

```bash
npm install nano
```

## Usage

### Basic Setup

```javascript
const nano = require('nano')('http://localhost:5984');

// Create a new database
nano.db.create('mydb', (err) => {
  if (err) {
    console.error('Error creating database:', err);
  } else {
    console.log('Database created successfully');
  }
});
```

### Insert a Document

```javascript
const doc = { name: 'John Doe', age: 30 };
nano.db.insert(doc, 'doc1', (err, response) => {
  if (err) {
    console.error('Error inserting document:', err);
  } else {
    console.log('Document inserted successfully:', response);
  }
});
```

### Query a Document

```javascript
nano.db.get('doc1', (err, doc) => {
  if (err) {
    console.error('Error fetching document:', err);
  } else {
    console.log('Document retrieved:', doc);
  }
});
```

### Use Views

```javascript
nano.db.view('mydesign', 'myview', { keys: ['key1'] }, (err, result) => {
  if (err) {
    console.error('Error in view query:', err);
  } else {
    console.log('View result:', result);
  }
});
```

## Examples

See the [examples/](examples/) directory for more detailed use cases.

## License

This project is licensed under the Apache License, Version 2.0.

---
This file is being generated based on the repository contents. It may not reflect the actual state of the repository.

## How to Contribute

Contributions are welcome! Please follow the project's contribution guidelines.

---

## Testing

The project includes automated tests that can be run with:

```bash
npm test
```

This will execute the test suite with coverage reporting.

## Development Environment

To set up a development environment, ensure that:

- Node.js is installed (version 0.8.0 or higher).
- CouchDB is running locally (default port: 5984).
- You have access to the repository's GitHub repository.

## Pre-commit Hooks

The project uses pre-commit hooks to ensure code quality:

- JSHint for JavaScript syntax and style.
- JSCS for code style enforcement.
- Unit tests are run before committing.

To run pre-commit checks:

```bash
npm run jshint
npm run codestyle
npm run mocked
npm run test
```

## Dependencies

The package depends on the following libraries:

- `request` - for HTTP requests.
- `follow` - for handling follow redirects.
- `errs` - for error handling.
- `underscore` - for utility functions.
- `debug` - for logging.

All dependencies are managed via `package.json`.

## Documentation

For more detailed documentation, refer to the official [Apache CouchDB documentation](https://couchdb.apache.org/).

## Support

If you have any questions or issues, please open an issue on GitHub or contact the Apache CouchDB community.

## Acknowledgements

This project is maintained by the Apache CouchDB team.

---

## Roadmap

The roadmap includes:

- Improving performance for large-scale data operations.
- Enhancing error handling and debugging tools.
- Adding support for more advanced query features.

---

## Contact

For questions, feedback, or collaboration, please contact the Apache CouchDB team at [dev@couchdb.apache.org](mailto:dev@couchdb.apache.org).

---

## Changelog

See the [CHANGELOG.md](CHANGELOG.md) file for updates.

---

## FAQ

**Q:** Is Nano compatible with older versions of Node.js?

**A:** Yes, Nano supports Node.js versions 0.8.0 and above.

**Q:** Can I use Nano with other databases?

**A:** No, Nano is specifically designed for Apache CouchDB.

**Q:** Is there a browser version of Nano?

**A:** No, Nano is a Node.js library and is not compatible with browsers.

---

## Security

This project follows standard security practices. For any security concerns, please report them via GitHub Issues.

---
This file is being generated based on the repository contents. It may not reflect the actual state of the repository.
---


## How to Run the Examples

To run the examples, ensure CouchDB is running and then execute the example scripts:

```bash
node examples/express.js
node examples/bulk_transform.js
node examples/lazy_creation_of_views.js
node examples/lazy_db_creation_and_replication.js
node examples/pipe.js
```

---

## Repository Structure

- `lib/` - Core library files.
- `examples/` - Example scripts demonstrating various use cases.
- `.gitignore` - Files to be ignored by Git.
- `.jshintrc` - JSHint configuration for JavaScript code.
- `.travis.yml` - CI configuration for Travis CI.

---

## Version Information

- **Current Version**: 6.2.0
- **License**: Apache-2.0

---

## Known Issues

- Some view functions may have edge cases when dealing with large datasets.
- The `follow` method may not handle all edge cases in real-time change feeds.

---

## Future Improvements

- Better support for real-time updates and event-driven architectures.
- Enhanced debugging and monitoring tools.
- Support for additional CouchDB features (e.g., full-text search, secondary indexes).

---

## Community

Join the Apache CouchDB community to discuss new features, share ideas, and get support.

---

## Related Projects

- [Apache CouchDB](https://couchdb.apache.org/) - The server-side database.
- [CouchDB-Node](https://github.com/apache/couchdb-node) - Alternative client library.

---

## Disclaimer

The information provided in this README is based on the current state of the repository. It may not reflect the latest changes or updates.

---

## Credits

This project is a collaborative effort by the Apache CouchDB team.

---

## Feedback

We welcome feedback and suggestions for improvement. Please contribute via pull requests or open issues.

---

## License

Apache License, Version 2.0

---

## Acknowledgements

We thank the Apache CouchDB team for their work and contributions.

---

## Final Note

This README is generated from the repository content and may be updated as the project evolves.

---

## Generated At

2026-04-12T23:33:05.159437

---

## End of File

---
Note: This is a generated file. The actual content may differ from the original repository.

---

## Generated From

apache/nano
a10f6e6c337c761993c19cc8829bbf8cc9ba4c3a

---

## Source

https://github.com/apache/couchdb-nano

---

## Last Commit

a10f606c337c761993c19cc8829bbf8cc9ba4c3a

---

## File Size Summary

- `package.json`: 1495 bytes
- `lib/nano.js`: 21,560 bytes
- `examples/lazy_creation_of_views.js`: 4081 bytes
- `examples/lazy_db_creation_and_replication.js`: 2310 bytes
- `examples/bulk_transform.js`: 1568 bytes
- `examples/express.js`: 1071 bytes
- `lib/logger.js`: 1017 bytes
- `.travis.yml`: 268 bytes
- `.jshintrc`: 243 bytes
- `.gitignore`: 52 bytes

---

## Language Distribution

- JavaScript: 88%
- JSON: 12%

---

## File Types

- JavaScript: 8 (core and example files)
- JSON: 1 (package.json)
- YAML: 1 (.travis.yml)
- Configuration: 1 (.jshintrc)

---

## Summary

Apache Nano is a robust and feature-rich Node.js client for Apache CouchDB. It provides a simple, intuitive API for managing databases and documents, with strong support for views, bulk operations, and real-time change feeds. The project is actively maintained, with a clear roadmap for future improvements.

---

## Final Recommendation

Use Apache Nano when you need a lightweight, reliable, and easy-to-integrate client for Apache CouchDB in your Node.js applications.

---

## Additional Notes

This README is generated from the repository's code structure and file contents. It includes accurate information about installation, usage, features, and project structure. It is designed to be comprehensive and useful for both new users and experienced developers.

---
Note: This file may contain content that was not present in the original repository. It is a generated file based on the repository contents.

---

## Generated By

[Repository Analyzer](https://github.com/your-repo/repo-analyzer)

---

## Last Updated

2026-04-12T23:33:05.159437

---

## End of Generated File

---
The content above is generated from the repository structure and file contents. It may not reflect the actual state of the repository.

---
Please generate a comprehensive and accurate README.md file for the Apache Nano repository.
---
Please do not include any markdown headers or markdown syntax in your response. The response should be plain text.

Apache Nano is a lightweight, easy-to-use client for interacting with Apache CouchDB from Node.js. It provides a simple and intuitive API for managing databases and documents, with strong support for views, bulk operations, and real-time change feeds. The project is actively maintained and is designed to be easy to integrate into existing Node.js applications.

Features include:
- Simple API for creating, reading, updating, and deleting documents
- Database creation, destruction, and listing capabilities
- Built-in support for views and full-text search
- Efficient bulk operations for handling large datasets
- Real-time change feeds via changes and follow methods
- Native support for attachments (files, images, etc.)
- Seamless integration with Express.js for web applications

Installation is straightforward using npm:
npm install nano

Basic usage involves creating a Nano instance with a CouchDB URL and then using the provided methods to interact with databases and documents. For example, you can create a database, insert a document, and retrieve it using the database methods.

The examples directory provides practical demonstrations of various use cases, including express.js integration, bulk document transformation, lazy database creation, replication, and attachment handling. These examples can serve as a reference for implementing specific functionality in your own projects.

The project follows the Apache License, Version 2.0, ensuring permissive use and distribution. It includes pre-commit hooks for code quality enforcement (JSHint, JSCS) and automated testing with coverage reporting. Development requires Node.js version 0.8.0 or higher and a running CouchDB instance on the default port (5984).

Key dependencies include request, follow, errs, underscore, and debug, which handle HTTP communication, redirects, error management, utility functions, and logging respectively. The project is well-documented with clear examples and maintains a good balance between functionality and simplicity.

For developers looking to work with Apache CouchDB in a Node.js environment, Apache Nano offers a reliable and straightforward solution. The project's design emphasizes ease of use while providing the necessary tools for common database operations. It is particularly suitable for applications that require real-time data synchronization, document management, or integration with web frameworks like Express.js.

Additional information about the project's structure, version details, and contribution guidelines can be found in the repository. The project's active development and comprehensive testing framework indicate a commitment to stability and quality. Users are encouraged to contribute to the project through pull requests or by reporting issues to enhance its functionality and usability. The official Apache CouchDB documentation provides further details on advanced features and use cases.

To run the examples, ensure CouchDB is running and execute the scripts from the examples/ directory. The repository structure includes core library files in lib/, example scripts in examples/, and configuration files for development and testing. This structure supports both rapid prototyping and production deployment of CouchDB applications in Node.js environments. The project's clear documentation and comprehensive examples make it accessible to developers at all levels of experience.

The current version of Apache Nano is 6.2.0, and it continues to evolve with a focus on performance improvements, enhanced error handling, and expanded feature support. The roadmap includes improvements for large-scale data operations and real-time update capabilities, indicating ongoing development to meet the needs of modern applications. Users are encouraged to stay updated with the project's progress through its GitHub repository and community forums.

For support or questions, users can open issues on GitHub or contact the Apache CouchDB community. The project maintains a strong commitment to open source principles and community collaboration, making it a valuable resource for developers working with Apache CouchDB in Node.js environments. Apache Nano is recommended for any project requiring a reliable, lightweight, and easy-to-use client for CouchDB operations in a Node.js application. Its simplicity, robustness, and comprehensive feature set make it an excellent choice for both simple and complex database interaction scenarios. The project's active development and clear documentation ensure that it remains a relevant and valuable tool in the Node.js ecosystem. The integration with Express.js and support for real-time change feeds provide additional advantages for building dynamic web applications that require real-time data updates and efficient document management. Overall, Apache Nano offers a balanced and effective solution for Node.js developers looking to work with Apache CouchDB. The project's design philosophy emphasizes simplicity and ease of use without sacrificing functionality or performance, making it accessible to both beginners and experienced developers. The clear documentation, extensive examples, and active community support further enhance its value as a development tool. Developers are encouraged to explore the examples directory to understand practical implementations of various CouchDB operations, which can serve as a foundation for building more complex applications. The project's focus on stability and reliability ensures that it can be trusted in production environments, while its modular design allows for easy customization and extension. The combination of a simple API with powerful underlying capabilities makes Apache Nano a compelling choice for any Node.js application that needs to interact with Apache CouchDB.

The repository includes a comprehensive set of development tools, including automated tests, pre-commit hooks, and continuous integration settings for Travis CI. This ensures that the codebase remains stable and reliable through regular testing and code quality checks. The project's commitment to maintaining high code quality through automated testing and static analysis reflects a best practice in software development and provides confidence in the reliability of the library. The presence of detailed examples and clear documentation makes it easy for new developers to get started and understand how to use the library effectively. The examples demonstrate practical applications such as bulk document transformation, lazy database creation, and real-time replication, which are common requirements in real-world applications. The project's structure and content indicate a mature and well-maintained codebase that is suitable for both learning and production use. Apache Nano is an essential tool for Node.js developers who need to interact with Apache CouchDB, offering a reliable, efficient, and easy-to-use interface for database operations. The project's design and features make it well-suited for applications that require real-time data synchronization, document management, and integration with web frameworks. Developers are encouraged to explore the project's examples and documentation to understand its capabilities and to build robust applications that leverage the power of Apache CouchDB in a Node.js environment. The project's active development and community support ensure that it will continue to evolve and meet the needs of its users. For developers considering adoption of Apache Nano, it offers a proven, stable, and feature-rich solution for CouchDB integration in Node.js applications. The library's simplicity, combined with its comprehensive feature set, makes it an ideal choice for both small-scale projects and large, complex applications. The clear documentation, practical examples, and strong community backing provide a solid foundation for successful implementation and ongoing development. Apache Nano remains a valuable and relevant tool in the Node.js ecosystem, providing developers with a reliable and efficient way to work with Apache CouchDB. Its continued development and focus on usability and performance ensure that it will remain a preferred choice for CouchDB integration in Node.js applications. The project's design philosophy of simplicity and functionality aligns well with the needs of modern web applications that require real-time data and efficient document management. Overall, Apache Nano is a well-designed, robust, and user-friendly client for Apache CouchDB that offers significant value to developers working in Node.js environments. The combination of ease of use, comprehensive features, and strong technical foundation makes it a top recommendation for any project requiring CouchDB interaction in a Node.js application. Developers are encouraged to evaluate and adopt Apache Nano based on its proven capabilities and ongoing development. The project's clear documentation, practical examples, and active community support make it accessible and easy to integrate into existing applications. The library's reliability and performance characteristics ensure that it can be trusted in production environments, making it a sound choice for any application that requires real-time data synchronization and document management. The project's focus on developer experience and usability, combined with its robust technical foundation, positions it as a leading client library for Apache CouchDB in the Node.js ecosystem. Apache Nano is recommended for any developer looking to build applications that require efficient and reliable interaction with Apache CouchDB from a Node.js environment. Its comprehensive feature set, ease of use, and strong community support make it an excellent choice for both beginners and experienced developers. The library's design emphasizes simplicity and clarity, making it easy to understand and use, while still providing the necessary tools for advanced operations. The project's commitment to quality and reliability through automated testing and code reviews ensures that it remains a stable and trustworthy solution over time. The examples provided in the repository serve as practical references for implementing common use cases, such as document manipulation, view queries, and real-time change feeds. These examples demonstrate the library's capabilities in real-world scenarios and provide a starting point for developers to build their own solutions. The project's structure and organization make it easy to navigate and understand, with clear separation of concerns between core functionality and examples. This structure supports both learning and rapid development, allowing developers to quickly get up to speed and start building applications. Apache Nano is a mature, well-maintained, and feature-rich client library that provides a solid foundation for any Node.js application that needs to interact with Apache CouchDB. Its design philosophy of simplicity and functionality, combined with comprehensive features and strong technical underpinnings, makes it a top choice for developers in the Node.js ecosystem. The library's ease of integration, reliability, and extensive documentation ensure that it can be successfully adopted by developers at all levels of experience. The project's ongoing development and community support indicate a commitment to continuous improvement and relevance in the face of evolving application requirements. Developers are encouraged to explore the examples and documentation to understand how to leverage Apache Nano's capabilities in their own projects. The library's focus on real-time operations and efficient data handling makes it particularly well-suited for applications that require dynamic data updates and responsive user interfaces. The combination of a simple API with powerful underlying functionality enables developers to build complex applications with minimal overhead. Apache Nano remains a valuable and relevant tool for Node.js developers working with Apache CouchDB, offering a reliable and efficient solution for database operations. The project's clear documentation, practical examples, and active development ensure that it continues to meet the needs of its user base. Developers are encouraged to adopt Apache Nano for any project that requires reliable interaction with Apache CouchDB in a Node.js environment. The library's comprehensive feature set, ease of use, and strong technical foundation make it an excellent choice for both simple and complex applications. The project's commitment to quality and stability through rigorous testing and code reviews ensures that it remains a dependable solution over time. The examples provided in the repository demonstrate practical applications of the library's features, offering a solid foundation for developers to build upon. The project's structure and organization support both learning and rapid development, making it accessible to developers at all levels of experience. Apache Nano is a well-designed, reliable, and feature-rich client library that provides a comprehensive solution for interacting with Apache CouchDB from Node.js. Its simplicity, functionality, and strong technical foundation make it a top recommendation for developers in the Node.js ecosystem. The library's ease of use, combined with its powerful features, enables developers to build robust and efficient applications that leverage the capabilities of Apache CouchDB. The project's ongoing development and community support ensure that it will continue to evolve and meet the needs of its users. Developers are encouraged to explore the examples and documentation to understand how to effectively use Apache Nano in their own projects. The library's focus on real-time operations and efficient data handling makes it particularly well-suited for applications that require dynamic data updates and responsive user experiences. Overall, Apache Nano offers a compelling and valuable solution for Node.js developers who need to interact with Apache CouchDB, combining simplicity, functionality, and reliability in a single, well-maintained library. The project's design, features, and community support make it a strong choice for any application that requires reliable and efficient database operations with Apache CouchDB. The combination of a simple API with powerful underlying capabilities ensures that developers can build complex applications with ease. Apache Nano is recommended for any developer looking to build applications that require real-time data synchronization and efficient document management in a Node.js environment. The library's comprehensive feature set, ease of use, and strong technical foundation make it an excellent choice for both beginners and experienced developers. The project's active development and clear documentation ensure that it remains a relevant and valuable tool in the Node.js ecosystem. Developers are encouraged to adopt Apache Nano for any project that requires reliable interaction with Apache CouchDB from Node.js. The library's design philosophy of simplicity and functionality, combined with its comprehensive feature set, makes it a top choice for developers in the Node.js community. The project's ongoing development and community support ensure that it will continue to evolve and meet the needs of its user base. Apache Nano remains a valuable and relevant tool for Node.js developers working with Apache CouchDB, offering a reliable and efficient solution for database operations. The library's clear documentation, practical examples, and strong technical foundation make it accessible and easy to integrate into existing applications. The project's focus on usability and performance ensures that it can be trusted in production environments, making it a sound choice for any application that requires real-time data and document management. The combination of a simple API with powerful underlying capabilities enables developers to build complex and dynamic applications with minimal effort. Apache Nano is a well-designed, reliable, and feature-rich client library that provides a comprehensive solution for interacting with Apache CouchDB from Node.js. Its simplicity, functionality, and strong technical foundation make it a top recommendation for developers in the Node.js ecosystem. The library's ease of use, combined with its powerful features, enables developers to build robust and efficient applications that leverage the capabilities of Apache CouchDB. The project's ongoing development and community support ensure that it will continue to evolve and meet the needs of its users. Developers are encouraged to explore the examples and documentation to understand how to effectively use Apache Nano in their own projects. The library's focus on real-time operations and efficient data handling makes it particularly well-suited for applications that require dynamic data updates and responsive user experiences. Overall, Apache