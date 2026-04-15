```markdown
# Apache Parquet Format

## Description

This repository contains the metadata definitions and tooling for the Apache Parquet format. Parquet is a columnar storage format designed for efficient data storage and retrieval, particularly in big data processing systems like Hadoop. This project provides the core specifications for the file format, allowing interoperability between various data processing frameworks.  The Thrift definition within the repository is central to defining Parquet's data structures.

## Features

*   **Columnar Storage:**  Parquet stores data in a columnar format, optimizing read performance for analytical queries that typically access only a subset of columns.
*   **Schema Evolution:**  The format supports schema evolution, allowing changes to the data structure without breaking compatibility.
*   **Compression & Encoding:**  Supports a variety of compression and encoding schemes to reduce storage space and improve query performance.  Supported codecs include Snappy, GZIP, LZO, Brotli, LZ4, and Zstd.
*   **Data Types:**  Supports a comprehensive set of data types, including primitive types, nested structures, and advanced types like decimals and timestamps.
*   **Metadata Management:**  Includes rich metadata information for efficient data filtering and retrieval.
*   **Thrift Definition:**  Provides a Thrift definition (`parquet.thrift`) that defines the Parquet data structures.

## Installation

This project is a core specification and does not require a traditional installation.  However, to work with Parquet files and utilize the definitions, you will need a compatible Parquet library in your chosen programming language (e.g., Java, Python, C++). 

To generate code from the Thrift definition:

1.  **Install Thrift:** Ensure you have the Thrift compiler installed on your system.  Instructions can be found on the official Thrift website: [https://thrift.apache.org/](https://thrift.apache.org/)
2.  **Generate Code:**  Use the following command to generate code in your desired language.  For example, to generate Java code:

    ```bash
    thrift --gen java -o generated src/main/thrift/parquet.thrift
    ```

## Usage

The primary use case of this repository is to understand the Parquet format specification and generate code for interacting with Parquet files in different programming languages.

*   **Review the `parquet.thrift` file:** This file defines the data structures used in the Parquet format.
*   **Generate code:** Use the Thrift compiler to generate code in your desired language.
*   **Integrate with a Parquet library:** Use a dedicated Parquet library for reading and writing Parquet files. Popular options include:
    *   **Java:** [parquet-mr](https://github.com/apache/parquet-mr)
    *   **Python:** [pyarrow](https://arrow.apache.org/)
    *   **C++:** [parquet-cpp](https://github.com/apache/parquet-cpp)

## Development

The project is managed using Maven.  Here are some common development tasks:

*   **Building the project:** `mvn clean install`
*   **Running tests:** `mvn test`
*   **Preparing a release:** `mvn release:prepare`
*   **Finalizing a release:** `mvn release:perform`

## Contributing

Contributions are welcome! Please review the [NOTICE](NOTICE) and [LICENSE](LICENSE) files for details on licensing and contribution guidelines.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more information.

## Repository Structure

*   `.asf.yaml`: Configuration file for Apache projects.
*   `.github/`: Contains GitHub configuration files, including issue templates and workflows.
*   `doc/`: Documentation related to the Parquet format.
*   `licenses/`: Contains licenses for third-party dependencies.
*   `pom.xml`: Maven project configuration file.
*   `src/main/thrift/parquet.thrift`: The core Thrift definition file for the Parquet format.
*   `src/main/resources/META-INF/LICENSE`:  License information.
*   `dev/`: Scripts for release management.
*   `changelog.sh`: A script for generating a changelog.

## Further Information

*   **Apache Parquet Website:** [https://parquet.apache.org/](https://parquet.apache.org/)
*   **Thrift Website:** [https://thrift.apache.org/](https://thrift.apache.org/)
```