# Apache Parquet Format

[![Build Status](https://img.shields.io/github/workflow/status/apache/parquet-format/build?logo=github)](https://github.com/apache/parquet-format/actions)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0.txt)
[![Apache Software Foundation](https://img.shields.io/badge/organization-Apache%20Software%20Foundation-000000.svg)](https://apache.org)

> **Apache Parquet Format** is a columnar storage format designed for efficient data compression, fast query performance, and interoperability across data processing systems. It enables high-performance analytics on large datasets by storing data in a columnar structure with rich metadata and support for complex data types.

This repository contains the official specification and generated code for the Apache Parquet file format. It defines the schema, data types, encodings, compression algorithms, and metadata structures used in Parquet files. The format is widely adopted in big data ecosystems including Apache Spark, Apache Hive, Apache Pig, and many others.

---

## Description

The Apache Parquet Format is a binary columnar storage format that optimizes data storage and retrieval by organizing data into columns rather than rows. This design enables efficient compression, fast random access, and superior performance for analytical queries.

This repository provides the formal specification of the Parquet format, including:

- Data types (e.g., INT32, DOUBLE, BYTE_ARRAY)
- Logical types (e.g., DATE, TIMESTAMP, DECIMAL)
- Encodings (e.g., PLAIN, RLE, DELTA_BINARY_PACKED)
- Compression algorithms (e.g., SNAPPY, GZIP, ZSTD)
- Metadata structures (e.g., FileMetaData, ColumnMetaData, RowGroup)

The format is designed to be both efficient and extensible, supporting nested data structures, nullability, and advanced features like Bloom filters, encryption, and geospatial types.

This project serves as the authoritative reference for developers, data engineers, and tooling vendors who need to implement or parse Parquet files.

---

## Features

- ✅ **Columnar Storage**: Optimized for analytical queries with fast reads and efficient compression.
- ✅ **Rich Data Types**: Supports primitive types (INT32, DOUBLE), complex types (MAP, LIST, STRUCT), and logical types (DATE, TIMESTAMP, DECIMAL).
- ✅ **Flexible Encodings**: Multiple encoding strategies (PLAIN, RLE, DELTA_BINARY_PACKED, BYTE_STREAM_SPLIT) for optimal compression and performance.
- ✅ **Compression Support**: Built-in support for SNAPPY, GZIP, LZO, BROTLI, LZ4, and ZSTD.
- ✅ **Metadata & Statistics**: Comprehensive metadata including null counts, min/max values, histograms, and size estimates.
- ✅ **Geospatial Types**: Full support for GEOMETRY and GEOGRAPHY types with bounding boxes and edge interpolation.
- ✅ **Encryption**: Support for AES-GCM encryption with optional AAD prefixes and footer-based encryption.
- ✅ **Bloom Filters**: Optional Bloom filters for fast filtering of data in large datasets.
- ✅ **Sorting & Indexing**: Row-level sorting and column-level index support for efficient query execution.
- ✅ **Cross-Platform Compatibility**: Designed to work across languages and platforms including Java, C++, Python, and more.

---

## Table of Contents

- [Project Title](#project-title)
- [Description](#description)
- [Features](#features)
- [Table of Contents](#table-of-contents)
- [Prerequisites / Requirements](#prerequisites--requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

---

## Prerequisites / Requirements

To work with this repository, you will need the following:

- **Thrift Compiler (v0.22.0 or later)**: Required to generate code from the `.thrift` schema.
- **Java 8 or later**: Required to build and run the project (via Maven).
- **Maven**: Version 3.6 or later for building the project.
- **Git**: For cloning and managing version control.
- **Linux/macOS/WSL**: Recommended for development. Windows support is limited.

> ⚠️ This repository is primarily a specification and metadata repository. It does not contain executable applications or user-facing tools. It is intended for developers building Parquet readers/writers or data processing frameworks.

---

## Installation

This repository does not require installation in the traditional sense. It is a specification and reference codebase.

To work with the Parquet format specification locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/apache/parquet-format.git
   cd parquet-format
   ```

2. **Install required tools**:
   - Install [Thrift](https://thrift.apache.org/) version 0.22.0 or later.
   - Install [Maven](https://maven.apache.org/) 3.6+.
   - Ensure Java 8 or later is installed.

3. **Generate code from the Thrift schema**:
   ```bash
   make thrift
   ```
   This command generates C++ and Java code from `src/main/thrift/parquet.thrift`.

4. **Build the project**:
   ```bash
   mvn clean install
   ```
   This compiles the project and generates the JAR artifact.

> 💡 The generated code is used by Parquet implementations to parse and write Parquet files. This repository serves as the foundation for all Parquet implementations.

---

## Usage

The Parquet format is used internally by data processing frameworks. Below are examples of how the schema is used in practice.

### 1. Reading a Parquet File

When a reader parses a Parquet file, it uses the `FileMetaData` structure to understand the schema, row groups, and column metadata.

```thrift
struct FileMetaData {
  1: required i32 version
  2: required list<SchemaElement> schema
  3: required i64 num_rows
  4: required list<RowGroup> row_groups
}
```

The reader uses the `schema` field to map column names to their types and logical types, and the `row_groups` to determine how to access data.

### 2. Writing a Parquet File

A writer uses the `ColumnMetaData` structure to define the encoding, compression, and statistics for each column.

```thrift
struct ColumnMetaData {
  1: required Type type
  2: required list<Encoding> encodings
  3: required list<string> path_in_schema
  4: required CompressionCodec codec
  5: required i64 num_values
  6: required i64 total_uncompressed_size
  7: required i64 total_compressed_size
  8: optional list<KeyValue> key_value_metadata
}
```

The writer selects an encoding (e.g., `DELTA_BINARY_PACKED`) based on data distribution and applies compression (e.g., `SNAPPY`) to reduce storage footprint.

### 3. Handling Logical Types

For complex types like `TIMESTAMP_MILLIS`, the writer uses the `TimestampType` structure:

```thrift
struct TimestampType {
  1: required bool isAdjustedToUTC
  2: required TimeUnit unit
}
```

This allows the reader to interpret timestamps correctly, including timezone adjustments and unit conversion.

---

## Contributing

We welcome contributions to the Apache Parquet Format specification and implementation. Please follow these guidelines:

- **Report bugs** via GitHub Issues at [https://github.com/apache/parquet-format/issues](https://github.com/apache/parquet-format/issues)
- **Submit feature requests** through the same issue tracker.
- **Contribute code** by submitting pull requests to the `main` branch.
- **Review changes** using the Apache Software Foundation's contribution guidelines.

All contributions must comply with the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0.txt) and follow the project's code style and documentation standards.

> 🔍 The Parquet format specification is maintained by the Apache Parquet community. Changes to the format require consensus and are reviewed by the Parquet PMC.

For more information on contributing, see the [Apache Parquet Contributing Guide](https://cwiki.apache.org/confluence/display/Parquet/Contributing).

---

## License

This project is licensed under the **Apache License, Version 2.0**.

See the [LICENSE](./licenses) file for details.

> By using this project, you agree to the terms of the Apache License 2.0.

---

## Contact / Authors

The Apache Parquet Format is maintained by the **Apache Software Foundation**.

- **Project Home**: [https://parquet.apache.org](https://parquet.apache.org)
- **Development Mailing List**: [dev@parquet.apache.org](mailto:dev@parquet.apache.org)
- **Commits Mailing List**: [commits@parquet.apache.org](mailto:commits@parquet.apache.org)
- **Issue Tracker**: [GitHub Issues](https://github.com/apache/parquet-format/issues)
- **Documentation**: [parquet.apache.org/docs](https://parquet.apache.org/docs)

For questions or feedback, please reach out to the community via the mailing lists or open an issue on GitHub.

> 💬 The Parquet project is open and collaborative. We welcome your input and contributions to improve the format and its ecosystem.