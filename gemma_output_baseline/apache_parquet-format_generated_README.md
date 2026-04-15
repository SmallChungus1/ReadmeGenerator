```markdown
# Apache Parquet Format

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Description

Apache Parquet is a columnar storage format designed for efficient data storage and retrieval. This project provides the metadata code generation and specifications for the Parquet format, enabling interoperability and optimized data processing. It's intended for developers and data engineers working with big data systems like Hadoop, Spark, and others.

## Features

*   **Columnar Storage:** Optimized for analytical queries that typically access only a subset of columns.
*   **Schema Evolution:** Supports adding, removing, or modifying columns without rewriting the entire dataset.
*   **Compression and Encoding:** Offers various compression algorithms (Snappy, GZIP, LZO, Brotli, LZ4, ZSTD) and encoding schemes to reduce storage costs and improve I/O performance.
*   **Data Types:** Supports a wide range of data types, including primitive types, nested structures, and logical types like dates, times, and decimals.
*   **Metadata Management:** Provides comprehensive metadata for efficient data access and filtering.
*   **Encryption Support:** Includes support for encrypting data at rest.
*   **Bloom Filter Support:** Enables efficient filtering of data based on specific criteria.

## Table of Contents

1.  [Prerequisites / Requirements](#prerequisites--requirements)
2.  [Installation](#installation)
3.  [Usage](#usage)
4.  [Contributing](#contributing)
5.  [License](#license)
6.  [Contact / Authors](#contact--authors)

## Prerequisites / Requirements

*   Java Development Kit (JDK) 8 or later
*   Maven 3.x
*   Thrift compiler (version 0.22.0)
*   Git

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/apache/parquet-format.git
    cd parquet-format
    ```

2.  Build the project using Maven:

    ```bash
    mvn clean install
    ```

## Usage

This project primarily provides code generation and specifications.  The generated code is used by Parquet libraries in various languages (Java, C++, etc.).  To use the Parquet format, you would typically integrate a Parquet library into your application.

The `thrift` target in the `Makefile` can be used to generate code from the `parquet.thrift` definition:

```bash
make thrift
```

This will generate C++ and Java code in the `generated` directory.

## Contributing

We welcome contributions to the Apache Parquet Format project! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for detailed guidelines on how to contribute, report bugs, or submit feature requests.

## License

Apache Parquet Format is licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Contact / Authors

*   **Organization:** The Apache Software Foundation
*   **Website:** [https://parquet.apache.org/](https://parquet.apache.org/)
*   **Issue Tracker:** [https://github.com/apache/parquet-format/issues](https://github.com/apache/parquet-format/issues)
*   **Mailing Lists:**
    *   Dev Mailing List: dev@parquet.apache.org (subscribe: dev-subscribe@parquet.apache.org, unsubscribe: dev-unsubscribe@parquet.apache.org)
    *   Commits Mailing List: commits@parquet.apache.org (subscribe: commits-subscribe@parquet.apache.org, unsubscribe: commits-unsubscribe@parquet.apache.org)