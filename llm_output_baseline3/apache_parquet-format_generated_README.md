# Apache Parquet Format

## Description

The Apache Parquet format is a columnar storage format designed for efficient data storage and retrieval. It supports nested data structures and provides a rich set of features for encoding, compression, and metadata management. This repository contains the formal specification of the Parquet file format, including schema definitions, data page structures, and metadata elements.

## Features

- **Columnar storage** with support for nested data types
- **Flexible data types** including primitive types (BOOLEAN, INT32, INT64, etc.) and complex types (MAP, LIST, ENUM)
- **Logical types** for advanced data representation (e.g., DATE, TIMESTAMP, DECIMAL, JSON, BSON)
- **Encoding options** including PLAIN, RLE, DELTA_BINARY_PACKED, and BYTE_STREAM_SPLIT
- **Compression algorithms** such as SNAPPY, GZIP, LZ4, ZSTD, and BROTLI
- **Metadata support** for statistics, sorting, null handling, and bloom filters
- **Encryption support** with AES-GCM and AES-GCM-CTR algorithms
- **Versioning** with support for file version 1 and future versions

## Prerequisites / Requirements

- Thrift compiler (version 0.22.0) for generating code from the `.thrift` file
- Java 8 or higher (required by Maven build)
- Maven 3.6.0 or higher
- Git for version control
- GPG for signing release artifacts (used in release scripts)

## Installation

This repository is a specification and not a software package. It does not require installation in the traditional sense. The Parquet format is implemented in various data processing frameworks (e.g., Apache Spark, Hive, Presto).

To work with the specification:

1. Clone the repository:
   ```bash
   git clone https://github.com/apache/parquet-format.git
   ```

2. Ensure the Thrift compiler is installed and version 0.22.0 or higher is available in the system PATH.

3. Build the specification (generates Java and C++ code from the Thrift schema):
   ```bash
   cd parquet-format
   make thrift
   ```

## Usage

The Parquet format is used by data processing systems to store and read columnar data. The specification in this repository defines the structure of Parquet files and is used by tools and frameworks to implement reading and writing of Parquet data.

To generate code from the Parquet schema:
```bash
make thrift
```

This command generates Java and C++ code from the `parquet.thrift` file in the `src/main/thrift/` directory.

## Contributing

Contributions to the Parquet format specification are welcome. Please follow the Apache Software Foundation contribution guidelines.

For changes to the specification:
- Submit a pull request to the `apache/parquet-format` repository
- Ensure all changes are consistent with the existing format specification
- Update relevant documentation or examples as needed

For release-related changes:
- Follow the release workflow defined in the `dev/` directory
- Use the provided scripts (`prepare-release.sh`, `finalize-release`, `source-release.sh`) to manage release versions

## License

This project is licensed under the Apache License, Version 2.0.

## Contact / Authors

For questions or contributions, contact the Apache Parquet community:

- **Dev Mailing List**: dev@parquet.apache.org
- **Commits Mailing List**: commits@parquet.apache.org
- **Issue Tracker**: https://github.com/apache/parquet-format/issues

The Parquet format specification is maintained by the Apache Software Foundation.