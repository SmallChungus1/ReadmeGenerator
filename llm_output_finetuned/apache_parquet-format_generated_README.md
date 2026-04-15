# Apache Parquet Format

## Description

Apache Parquet is a columnar storage format designed for efficient data processing and analytics. This repository defines the **official schema and data model** for the Parquet file format, providing a comprehensive specification for how data is structured, encoded, and stored on disk. The format supports nested data, complex types, compression, encoding, and metadata, making it ideal for use in big data ecosystems such as Apache Hive, Apache Spark, and others.

The specification is written in Thrift, a language-agnostic interface definition language, and generates code for various programming languages. This repository serves as the authoritative source for the Parquet format's structure and semantics.

## Features

- **Columnar Storage**: Optimized for analytical queries by storing data column-wise.
- **Support for Nested Data Types**: Includes arrays, maps, structs, and unions.
- **Flexible Encoding Options**: Supports multiple encodings (e.g., PLAIN, RLE, DELTA_BINARY_PACKED) to optimize storage and performance.
- **Compression Algorithms**: Includes support for GZIP, SNAPPY, LZ4, ZSTD, and Brotli to reduce file size.
- **Metadata and Statistics**: Provides rich metadata including null counts, min/max values, and size statistics for efficient filtering and memory estimation.
- **Geospatial Support**: Includes types for `GEOMETRY` and `GEOGRAPHY` with bounding boxes and edge interpolation algorithms.
- **Logical Types**: Extends physical types with semantic meaning (e.g., `TIMESTAMP`, `DECIMAL`, `JSON`).
- **Encryption Support**: Supports AES-GCM encryption for secure data storage.
- **Bloom Filters**: Optional filters to accelerate data retrieval by reducing I/O.
- **Sorting and Indexing**: Supports row-level sorting and column-level indexing for efficient query execution.

## Installation

This repository contains the **format specification** and does not require installation in the traditional sense. It is intended to be used as a reference and by tools that generate Parquet-compatible code (e.g., Java, C++, Python).

To generate code from the Thrift schema, run the following commands:

```bash
# Generate C++ and Java code from the Thrift schema
make thrift
```

This will create generated code in the `generated/` directory.

To generate documentation from Markdown files:

```bash
# Convert Markdown files to HTML
make doc
```

## Usage

The Parquet format is used by data processing frameworks to store and read structured data efficiently. The Thrift schema (`parquet.thrift`) defines the structure of Parquet files and is used by tools such as:

- **Apache Spark** to read and write Parquet files
- **Apache Hive** to store and query data
- **Apache Pig** to process large datasets
- **Python libraries** like PyArrow and Pandas

### Example: Reading a Parquet File

While this repository does not contain executable code, here is a conceptual example of how a framework might use the schema:

```python
import pyarrow.parquet as pq

# Read a Parquet file
table = pq.read_table("data.parquet")
print(table.schema)
print(table.to_pandas())
```

### Example: Writing a Parquet File

```python
import pyarrow.parquet as pq
import pyarrow as pa

# Create a table with nested data
schema = pa.schema([
    ("name", pa.string()),
    ("age", pa.int32()),
    ("salary", pa.float64()),
    ("address", pa.struct([
        ("city", pa.string()),
        ("zip", pa.string())
    ]))
])

table = pa.table([
    ["Alice", "Bob", "Charlie"],
    [25, 30, 35],
    [75000.0, 80000.0, 90000.0],
    [
        ["New York", "Boston", "Chicago"],
        ["10001", "02108", "60601"]
    ]
], schema=schema)

# Write to Parquet
pq.write_table(table, "output.parquet")
```

> **Note**: The actual implementation of Parquet readers/writers is provided by external libraries (e.g., Apache Arrow, Parquet-Java) that consume this schema.

For release management, the following scripts are available in the `dev/` directory:

- `prepare-release.sh`: Prepares a release candidate (RC) with version and RC number.
- `finalize-release`: Finalizes a release and updates versioning.
- `source-release.sh`: Creates a signed source tarball for distribution.

Example usage of `prepare-release.sh`:

```bash
./dev/prepare-release.sh 2.7.0 0
```

This prepares a release candidate for version `2.7.0` with RC number `0`.