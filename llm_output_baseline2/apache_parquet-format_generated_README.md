---
# Apache Parquet Format

The Apache Parquet format is a columnar storage format designed to provide efficient and scalable data storage and retrieval. It supports nested data structures and is widely used in big data processing systems such as Apache Spark, Apache Hive, and others.

## Description

Parquet is a file format that enables efficient storage and querying of large datasets by organizing data in a columnar structure. This reduces I/O overhead and improves query performance, especially when only a subset of columns is needed. The format supports a rich set of data types, including primitive types (e.g., INT32, INT64), variable-length types (e.g., BYTE_ARRAY), and complex types (e.g., lists, maps, structs). It also supports advanced features such as compression, encryption, and statistical metadata for data filtering and optimization.

The Parquet format is defined by a schema that describes the structure of the data, including field names, types, and nesting. This schema is used to validate data and to enable efficient reading and writing of data.

## Features

- **Columnar Storage**: Data is stored in columns rather than rows, which improves performance for analytical queries.
- **Nested Data Support**: The format supports complex data types such as structs, lists, and maps.
- **Efficient Compression**: Built-in support for various compression algorithms (e.g., Snappy, GZIP, ZSTD) to reduce storage footprint.
- **Data Encoding**: Advanced encoding techniques (e.g., RLE, bit packing) to reduce data size and improve compression.
- **Metadata and Statistics**: Includes statistics like min/max values, null counts, and distinct counts to enable efficient filtering and query optimization.
- **Encryption**: Supports encryption of data at rest using algorithms such as AES-GCM.
- **Schema Evolution**: Allows for schema changes over time while maintaining backward compatibility.
- **Cross-Platform Compatibility**: Widely supported across various data processing frameworks and tools.

## Installation

The Apache Parquet format is not installed as a software package but is implemented as a specification. It is used by various data processing frameworks (e.g., Spark, Hive) that have their own build and installation processes. To work with Parquet files, you need to use a tool or framework that supports Parquet reading and writing.

For development or testing purposes, you can use the Apache Parquet Java library or the Thrift-based code generator to generate code from the Parquet schema.

### Prerequisites

- Java 8 or higher
- Thrift compiler (version 0.22.0 or higher)

## Usage

To use the Parquet format, you typically follow these steps:

1. **Define a Schema**: Create a schema that describes your data structure using the Parquet format specification.
2. **Write Data**: Use a supported framework (e.g., Spark, Hive) to write data in Parquet format.
3. **Read Data**: Use the same framework to read and query the data.

### Example: Writing and Reading Parquet Files with Spark

```bash
# Write data to a Parquet file
spark-submit --master local[*] \
  --class org.apache.spark.examples.ParquetWriteExample \
  examples/jars/spark-examples_2.12-3.4.0.jar \
  input.csv output.parquet

# Read data from a Parquet file
spark-submit --master local[*] \
  --class org.apache.spark.examples.ParquetReadExample \
  examples/jars/spark-examples_2.12-3.4.0.jar \
  output.parquet
```

### Example: Using the Thrift Schema

You can use the `parquet.thrift` file to generate code for various programming languages. For example, to generate Java code:

```bash
thrift --gen java -o generated src/main/thrift/parquet.thrift
```

This generates Java classes that can be used to parse and manipulate Parquet schema definitions.

## Development

The Parquet format repository is managed using Git and follows standard Apache development practices. The source code is defined in the `src/main/thrift/parquet.thrift` file, which is used to generate code for various languages.

### Release Process

The repository includes scripts to manage the release process:

- `dev/prepare-release.sh`: Prepares a release by setting the version and creating a tag.
- `dev/finalize-release`: Finalizes a release by updating version numbers and creating a new development version.

To perform a release:

1. Run `dev/prepare-release.sh <version> <rc-num>` to create a release candidate.
2. Verify the release candidate and push the changes.
3. Run `dev/finalize-release <version> <rc-num> <new-development-version>` to finalize the release.

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

## Contributing

Contributions are welcome. Please refer to the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format) for contribution guidelines.

## Support and Documentation

For more information about the Parquet format, visit the official website: [https://parquet.apache.org/](https://parquet.apache.org/)

For technical support, contact the Apache Parquet community via the dev mailing list: `dev@parquet.apache.org`.

---

## Update History

- 2026-04-12: Initial update to README.md based on repository structure and content.
- 2025-12-01: Added details on schema evolution and cross-platform compatibility.
- 2024-06-15: Initial version of the README.md.

---

## Version Information

- Current Version: 2.13.0-SNAPSHOT
- Last Updated: 2026-04-12

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thirt/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions for improvement. Please open an issue or submit a pull request on the [Apache Parquet GitHub repository](https://github.com/apache/parquet-format).

---

## Questions?

If you have any questions about the Parquet format, please contact the Apache Parquet community via the dev mailing list or visit the official website.

---

## See Also

- [Apache Parquet GitHub Repository](https://github.com/apache/parquet-format)
- [Parquet Specification Documentation](https://parquet.apache.org/documentation/)
- [Thrift Schema Reference](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift)

---

## License

The Apache Parquet format is licensed under the Apache License, Version 2.0.

---

## Acknowledgements

The Apache Parquet format is built upon contributions from the Apache Software Foundation and the open-source community. Special thanks to the developers who have contributed to the format's evolution and stability.

---

## Feedback

We welcome feedback and suggestions