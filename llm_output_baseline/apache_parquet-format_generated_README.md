# Apache Parquet Format

## Description

Apache Parquet is a **columnar storage format** designed for efficient data processing and analytics. This repository defines the **core schema and data model** for the Parquet file format, providing a standardized way to store and retrieve structured data with high compression and performance. The format supports nested data structures, type annotations, encoding strategies, and metadata for efficient query execution.

The specification is defined in a Thrift IDL file (`parquet.thrift`), which generates code for various programming languages. This repository serves as the official format specification and is maintained by the Apache Software Foundation.

## Features

- **Columnar Storage**: Optimized for analytical queries by storing data by column rather than row.
- **Nested Data Support**: Full support for complex structures like lists, maps, and unions.
- **Flexible Data Types**: Includes primitive types (INT32, INT64, BOOLEAN), variable-length types (BYTE_ARRAY), and specialized types (DECIMAL, TIMESTAMP, DATE, TIME).
- **Logical Type Annotations**: Enables rich data semantics (e.g., UTF8, JSON, GEOGRAPHY) through `LogicalType` and `ConvertedType` enums.
- **Efficient Encoding**: Supports multiple encoding strategies (PLAIN, DELTA_BINARY_PACKED, RLE, BIT_PACKED, BYTE_STREAM_SPLIT) to optimize storage and compression.
- **Compression Algorithms**: Built-in support for GZIP, SNAPPY, LZ4, ZSTD, and BROTLI.
- **Metadata-Driven**: Comprehensive metadata including statistics (null counts, min/max values), size estimates, and sort orders for query optimization.
- **Encryption Support**: Full support for AES-GCM encryption with optional AAD (Additional Authenticated Data).
- **Schema Evolution**: Designed to support backward compatibility through versioning and metadata annotations.
- **Cross-Platform Compatibility**: Designed to work with all major data processing frameworks (e.g., Spark, Hive, Pig).

## Installation

This repository is not a software application to be installed in the traditional sense. It defines the **format specification** for Parquet files. To work with Parquet data:

1. **Install a Parquet-compatible data processing framework** such as Apache Spark, Apache Hive, or Pandas with PyArrow.
2. **Ensure Thrift is available** for generating code from the `.thrift` file (required for development and tooling).
3. **Clone the repository** to access the official format specification:

```bash
git clone https://github.com/apache/parquet-format.git
cd parquet-format
```

> **Note**: The `Makefile` includes a script to generate code from the Thrift schema:
>
> ```bash
> make thrift
> ```
>
> This generates C++ and Java code in the `generated/` directory.

## Usage

The Parquet format is used by data systems to store and read structured data. Below are examples of how to work with the specification:

### 1. Generate Code from Thrift Schema

To generate code for a specific language (e.g., Java or C++), run:

```bash
make thrift
```

This command will:
- Create a `generated/` directory.
- Generate C++ and Java code from `src/main/thrift/parquet.thrift`.

### 2. Understand Data Types and Logical Types

The `parquet.thrift` file defines core types and logical types. For example:

```thrift
enum Type {
  BOOLEAN = 0;
  INT32 = 1;
  INT64 = 2;
  FLOAT = 4;
  DOUBLE = 5;
  BYTE_ARRAY = 6;
  FIXED_LEN_BYTE_ARRAY = 7;
}

union LogicalType {
  1: StringType STRING
  2: MapType MAP
  3: ListType LIST
  4: EnumType ENUM
  5: DecimalType DECIMAL
  6: DateType DATE
  7: TimeType TIME
  8: TimestampType TIMESTAMP
}
```

This allows frameworks to interpret data with semantic meaning (e.g., a `STRING` field with `UTF8` logical type is interpreted as UTF-8 encoded text).

### 3. View File Metadata Structure

A Parquet file contains metadata defined in the `FileMetaData` struct, including:

- Schema (tree of `SchemaElement`s)
- Row groups with column chunks
- Statistics (null counts, min/max values)
- Sorting orders
- Encryption details

This metadata enables efficient filtering, projection, and query planning.

### 4. Build and Release Management

The repository includes scripts for managing releases:

- `dev/prepare-release.sh`: Prepares a release version with a specified RC number.
- `dev/finalize-release`: Finalizes the release by tagging and updating version numbers.
- `dev/source-release.sh`: Creates a signed tarball for distribution.

Example usage:

```bash
# Prepare a release candidate (e.g., 2.7.0-rc0)
./dev/prepare-release.sh 2.7.0 0

# Finalize the release and update version
./dev/finalize-release 2.7.0 0 2.8.0
```

> **Note**: These scripts are intended for Apache project maintainers and require proper access to the repository and build tools.

### 5. Documentation and Compliance

The project includes:
- A `doc/` directory with images and documentation.
- A `pom.xml` for Maven-based builds.
- Compliance with Apache Software Foundation standards (e.g., license, issue tracking, mailing lists).

For more details, visit the official documentation at: [https://parquet.apache.org/](https://parquet.apache.org/)