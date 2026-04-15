# Apache Parquet Format

![Apache License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Build Status](https://github.com/apache/parquet-format/workflows/CI/badge.svg?branch=main)
![Version](https://img.shields.io/badge/version-2.13.0--SNAPSHOT-blue.svg)

> **Apache Parquet Format** is a columnar storage format designed for efficient data processing and analytics. It enables high-performance reading and writing of large datasets by leveraging columnar storage, compression, and encoding techniques. This repository defines the core schema and specifications for the Parquet file format, serving as the foundation for all Parquet-based tools and libraries.

---

## Description

Apache Parquet is a widely adopted open-source columnar storage format that optimizes data storage and retrieval for analytical workloads. The format supports nested data structures, compression, encoding, and metadata annotations for advanced data processing. This project provides the official specification and schema definitions for the Parquet format, ensuring consistency and interoperability across all Parquet implementations.

The Parquet format is used by major data platforms including Apache Spark, Apache Hive, Apache Pig, and many others. It enables efficient data compression, fast query performance, and reduced I/O overhead by storing data in columns rather than rows.

This repository contains the **core schema definition** written in Thrift, which is used to generate the metadata and code for Parquet readers and writers. It defines the structure of Parquet files, including:
- Columnar schema (via `SchemaElement`)
- Data page and index structures
- Compression and encoding options
- Logical types (e.g., timestamps, decimals, dates)
- Encryption and metadata support

It is **not** a tool for reading/writing Parquet files directly, but rather the foundational specification that all Parquet implementations must adhere to.

---

## Features

- ✅ **Columnar storage** with efficient row and column access
- ✅ **Flexible data types** including primitive, nested, and logical types
- ✅ **Advanced encoding** (e.g., dictionary, delta, bit-packed) for optimal compression
- ✅ **Logical types** for specialized data (e.g., timestamps, decimals, dates)
- ✅ **Compression support** (SNAPPY, GZIP, ZSTD, LZ4, Brotli)
- ✅ **Metadata-rich schema** with statistics, null counts, and size estimates
- ✅ **Encryption support** (AES-GCM) with optional key metadata
- ✅ **Bloom filters** for efficient filtering and query optimization
- ✅ **Sorting and ordering** support for efficient range queries
- ✅ **Cross-platform compatibility** with consistent schema and format versioning

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

To understand or work with this project, you should have the following:

- **Thrift Compiler (0.22.0 or later)**: Required to generate code from the `parquet.thrift` schema.
- **Java 8 or later**: For building and running the Parquet format specification tools.
- **Git**: To clone and manage the repository.
- **Basic understanding of columnar storage and data formats**.

> ⚠️ This repository is a specification and not a runnable application. It does not require installation for end users. Developers and contributors use it as a reference for building Parquet readers/writers.

---

## Installation

This project is a specification and does not require installation in the traditional sense. It is maintained as a reference for the Parquet format. However, you can build the generated code using the following steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/apache/parquet-format.git
   cd parquet-format
   ```

2. **Install Thrift**:
   Ensure you have Thrift 0.22.0 or later installed:
   ```bash
   # On Ubuntu/Debian
   sudo apt-get install thrift

   # On macOS with Homebrew
   brew install thrift

   # On Windows (via Chocolatey)
   choco install thrift
   ```

3. **Generate code from Thrift schema**:
   ```bash
   make thrift
   ```
   This will generate C++ and Java code from `src/main/thrift/parquet.thrift` into the `generated/` directory.

4. **Build the project** (optional, for local development):
   ```bash
   mvn clean install
   ```

> Note: The generated code is used by downstream Parquet implementations (e.g., Spark, Hive), not directly by end users.

---

## Usage

This project is not used directly by end users. Instead, it serves as the **official specification** that all Parquet tools and engines must follow.

### How to Use the Specification

1. **Develop a Parquet reader/writer**:
   - Use the Thrift schema (`parquet.thrift`) to generate code for your language (Java, C++, Python, etc.).
   - Implement the schema to read/write Parquet files with full support for logical types, compression, and metadata.

2. **Validate Parquet files**:
   - Use tools like `parquet-tools` or `Apache Arrow` to parse and validate Parquet files against the schema defined here.

3. **Analyze data structure**:
   - Use the `ColumnMetaData`, `RowGroup`, and `FileMetaData` structures to understand schema, compression, and statistics.

### Example: Reading a Parquet File

```java
// Using generated Java code from parquet.thrift
ParquetFileReader reader = new ParquetFileReader("data.parquet");
Schema schema = reader.getSchema();
List<ColumnChunk> chunks = reader.getChunks();

for (ColumnChunk chunk : chunks) {
  System.out.println("Column: " + chunk.getMetaData().getPathInSchema());
  System.out.println("Total uncompressed size: " + chunk.getMetaData().getTotalUncompressedSize());
}
```

> This example assumes you have generated the Java code using the Thrift compiler.

---

## Contributing

Contributions to the Apache Parquet Format are welcome and encouraged. Please follow these guidelines:

- **Report issues** via [GitHub Issues](https://github.com/apache/parquet-format/issues)
- **Submit feature requests** in the same issue tracker
- **Propose changes** to the schema or format specification in the `proposals/` directory
- **Follow the Apache Contributor License Agreement (CLA)**

For detailed contribution guidelines, see the [CONTRIBUTING.md](CONTRIBUTING.md) file (to be created).

> The Parquet format is governed by the Apache Software Foundation. All contributions are subject to the Apache License 2.0 and the ASF's code of conduct.

---

## License

This project is licensed under the **Apache License, Version 2.0**.

See the [LICENSE](licenses/Apache-2.0.txt) file for details.

---

## Contact / Authors

- **Project Maintainers**: Apache Parquet Team
- **Project Homepage**: [https://parquet.apache.org](https://parquet.apache.org)
- **Mailing Lists**:
  - **Dev Mailing List**: [dev@parquet.apache.org](mailto:dev@parquet.apache.org)
  - **Commits Mailing List**: [commits@parquet.apache.org](mailto:commits@parquet.apache.org)
- **Issue Tracker**: [GitHub Issues](https://github.com/apache/parquet-format/issues)
- **Documentation**: [parquet.apache.org/doc](https://parquet.apache.org/doc)

For questions or feedback, please reach out to the community via the mailing lists or GitHub issues.

> This project is maintained by the Apache Software Foundation. All contributions are governed by the Apache License 2.0 and the ASF's governance model.