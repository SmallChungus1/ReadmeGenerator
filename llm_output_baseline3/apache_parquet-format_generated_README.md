# Apache Parquet Format

![Apache License 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
![Build Status](https://github.com/apache/parquet-format/workflows/CI/badge.svg?branch=main)
![Apache Software Foundation](https://img.shields.io/badge/Project-ASF-blue)

A specification for the **Parquet file format**, a columnar storage format designed for efficient data compression, fast query performance, and schema evolution. This repository defines the complete schema and structure of Parquet files, enabling interoperability across data processing frameworks like Apache Spark, Hive, Pig, and others.

> **Parquet** is the de facto standard for columnar storage in big data ecosystems. It provides a compact, efficient, and schema-aware format that supports nested data, complex types, and advanced encoding strategies.

---

## Description

The Apache Parquet Format specification defines the structure, metadata, and encoding rules for Parquet files. This project serves as the authoritative source for the format's schema, including:

- Data types (e.g., INT32, FLOAT, BOOLEAN, BYTE_ARRAY)
- Logical types (e.g., TIMESTAMP, DECIMAL, DATE, JSON)
- Encodings (e.g., PLAIN, DELTA_BINARY_PACKED, RLE)
- Compression algorithms (e.g., GZIP, SNAPPY, ZSTD)
- Row group and column chunk organization
- Metadata structures (e.g., `FileMetaData`, `ColumnMetaData`, `RowGroup`)

This specification is foundational to all Parquet implementations and ensures that data written by one tool can be read by any other, regardless of the underlying engine.

---

## Features

- ✅ **Columnar Storage**: Optimized for analytical queries with minimal I/O overhead.
- ✅ **Schema Evolution**: Supports backward and forward compatibility with nested structures.
- ✅ **Efficient Encoding**: Built-in support for run-length encoding (RLE), dictionary encoding, and delta encoding.
- ✅ **Logical Types**: Enables rich data types like timestamps, decimals, and JSON with semantic meaning.
- ✅ **Compression Support**: Multiple codecs (SNAPPY, GZIP, ZSTD, LZ4) for flexible storage optimization.
- ✅ **Metadata Richness**: Includes statistics, null counts, and size estimates for advanced query optimization.
- ✅ **Encryption Support**: Secure storage via AES-GCM and column-level encryption.
- ✅ **Cross-Platform Interoperability**: Standardized format used across Spark, Hive, Presto, and more.

---

## Table of Contents

- [Prerequisites / Requirements](#prerequisites--requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

---

## Prerequisites / Requirements

To work with or understand the Parquet format specification, the following is required:

- **Thrift Compiler (0.22.0 or later)**: Required to generate code from the `.thrift` schema.
- **Java 8 or later**: For building and running Parquet-related tools (though the specification itself is language-agnostic).
- **Git**: For version control and accessing the source code.
- **Basic Understanding of Columnar Storage**: Familiarity with concepts like row groups, pages, and schema trees.

> ⚠️ This repository contains the **format specification**, not a runtime library. It does not provide tools for reading/writing Parquet files. For that, refer to the Apache Parquet Java or Python libraries.

---

## Installation

This repository is a specification and not a software package. It does not require installation in the traditional sense. However, you can clone and inspect the source code locally:

```bash
git clone https://github.com/apache/parquet-format.git
cd parquet-format
```

To generate code from the Thrift schema (e.g., for development or testing), run:

```bash
make thrift
```

This command will:
- Create a `generated/` directory
- Generate C++ and Java code from `src/main/thrift/parquet.thrift`

> 🔍 The generated code is used by Parquet implementations to parse and validate Parquet files.

---

## Usage

The Parquet format is used by data processing systems to store and exchange structured data. While this repository does not provide a direct API, the schema defines how data is structured in Parquet files.

### Example: Understanding a Parquet File Structure

A Parquet file contains the following key components:

| Component | Purpose |
|--------|--------|
| `FileMetaData` | Top-level metadata including schema, row count, and column groupings |
| `RowGroup` | A group of rows with associated column chunks |
| `ColumnChunk` | A single column's data and metadata (including encoding, compression, and statistics) |
| `DataPage` | Stores actual column values with encoding (e.g., PLAIN, DELTA_BINARY_PACKED) |
| `IndexPage` | Enables fast access to data pages via offsets |
| `DictionaryPage` | Stores repeated values to reduce storage footprint |

### Schema Example (Simplified)

```thrift
struct SchemaElement {
  1: optional Type type;
  2: optional i32 type_length;
  3: optional FieldRepetitionType repetition_type;
  4: required string name;
  5: optional i32 num_children;
  6: optional ConvertedType converted_type;
  7: optional i32 scale;
  8: optional i32 precision;
  9: optional i32 field_id;
  10: optional LogicalType logicalType;
}
```

This schema defines how a column is described in a Parquet file, including its type, repetition level, and logical type (e.g., `TIMESTAMP_MICROS`).

> 📚 For detailed documentation on each structure, refer to the official Parquet documentation at [https://parquet.apache.org](https://parquet.apache.org).

---

## Contributing

Contributions to the Apache Parquet Format specification are welcome and encouraged. Please follow these guidelines:

1. **Submit Issues** via GitHub: Report bugs, ambiguities, or missing features at [https://github.com/apache/parquet-format/issues](https://github.com/apache/parquet-format/issues).
2. **Propose Changes** to the specification: Submit a pull request with clear rationale and examples.
3. **Review PRs**: Help maintainers evaluate new proposals by reviewing the technical impact and compatibility.

> ❗ The format specification is maintained by the Apache Parquet community. All contributions are subject to the [Apache License 2.0](LICENSE) and community review.

For detailed contribution guidelines, see the [CONTRIBUTING.md](CONTRIBUTING.md) file (not included in this repository).

---

## License

This project is licensed under the **Apache License, Version 2.0**.

> See the [LICENSE](licenses/Apache-2.0.txt) file for details.

---

## Contact / Authors

- **Project Maintainers**: Apache Parquet Team
- **Primary Contact**: `dev@parquet.apache.org` (for development discussions)
- **Commits List**: `commits@parquet.apache.org` (for release and commit announcements)
- **Issue Tracker**: [https://github.com/apache/parquet-format/issues](https://github.com/apache/parquet-format/issues)

Join the community on:
- **Apache Parquet Mailing Lists** (Dev & Commits)
- **Apache Software Foundation (ASF) Website**: [https://parquet.apache.org](https://parquet.apache.org)

For questions or feedback, please reach out to the dev mailing list or open an issue on GitHub.