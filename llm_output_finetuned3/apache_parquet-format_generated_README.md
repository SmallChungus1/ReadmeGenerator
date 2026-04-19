# Apache Parquet Format

## Description

The Apache Parquet format is a columnar storage format designed for efficient storage and querying of large datasets. It supports nested data structures and provides a rich set of features for data compression, encoding, and metadata management. This repository contains the formal specification of the Parquet file format, including schema definitions, encoding options, compression algorithms, and metadata structures.

The format is defined using Thrift, with a comprehensive set of data structures that describe how data is stored in Parquet files. These structures define the schema, column metadata, row groups, page headers, and various encoding and compression options.

## Features

- Columnar storage with support for nested data types
- Multiple encoding options (e.g., PLAIN, RLE, DELTA_BINARY_PACKED)
- Support for various compression algorithms (UNCOMPRESSED, SNAPPY, GZIP, LZO, BROTLI, ZSTD)
- Schema definition with support for logical types (e.g., DATE, TIMESTAMP, DECIMAL)
- Metadata for statistics, null counts, and size estimation
- Support for encryption with AES-GCM and other algorithms
- Optional features including Bloom filters, sorting, and geospatial types
- Versioning support with backward compatibility

## Prerequisites / Requirements

- Java 8 or later (required by Maven build)
- Thrift compiler (version 0.22.0 or later)
- Maven 3.6.0 or later
- Git for version control
- Access to Apache infrastructure for release operations

## Installation

This repository is a specification and does not require installation in the traditional sense. It contains the formal definition of the Parquet file format and is used by Parquet implementations (e.g., Apache Arrow, Apache Spark, Hive) to generate code and validate file formats.

To build the specification and generate code:

1. Clone the repository:
   ```bash
   git clone https://github.com/apache/parquet-format.git
   cd parquet-format
   ```

2. Ensure Thrift is installed and version 0.22.0 is available.

3. Build the project using Maven:
   ```bash
   mvn clean compile
   ```

This will generate code from the Thrift schema in `src/main/thrift/parquet.thrift` into the `generated` directory.

## Usage

The Parquet format is used by data processing frameworks to store and read columnar data. The specification in this repository is consumed by:

- Data processing engines (e.g., Spark, Hive, Presto)
- Data storage systems
- Tools that validate or parse Parquet files

To use the format, applications must:
- Define a schema using the `SchemaElement` structure
- Specify encoding, compression, and logical types for each column
- Write data to Parquet files using the defined structures
- Read data from Parquet files using the format specification

The generated code from the Thrift schema can be used to parse and serialize Parquet files in various programming languages.

## Contributing

Contributions to the Apache Parquet Format are welcome. Please follow the Apache Software Foundation contribution guidelines.

To contribute:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request with clear documentation and tests
4. Ensure all code changes are properly documented and follow the existing style

For release coordination, see the `dev/` directory which contains scripts for preparing and finalizing releases.

## License

This project is licensed under the Apache License, Version 2.0.

## Contact / Authors

For questions or issues, contact the Parquet community:

- **Dev Mailing List**: dev@parquet.apache.org
- **Commits Mailing List**: commits@parquet.apache.org
- **Issue Tracker**: https://github.com/apache/parquet-format/issues

The Apache Parquet Format is maintained by the Apache Software Foundation.