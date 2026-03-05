# Apache Parquet Format

## Description

The Apache Parquet format is a columnar storage format designed for efficient data storage and retrieval. This repository contains the code and specifications related to the Parquet format, including metadata definitions, schema structures, and encoding mechanisms. It's optimized for analytical queries, providing benefits like reduced I/O, better compression, and improved query performance.

## Features

*   **Columnar Storage:** Stores data in columns rather than rows, enabling efficient retrieval of specific columns for analytic queries.
*   **Nested Data Support:**  Handles complex, nested data structures.
*   **Compression:** Supports various compression codecs (e.g., Snappy, GZIP, LZO, Brotli, ZSTD) to reduce storage space.
*   **Encoding:** Provides different encoding schemes to optimize data storage and retrieval.
*   **Schema Evolution:** Supports schema evolution allowing for changes to the data structure without breaking compatibility.
*   **Metadata:** Comprehensive metadata allows the reader to understand the schema, statistics, and characteristics of the data.
*   **Type System:** Defines a rich set of data types to represent a wide range of data formats.
*   **Bloom Filters:** Uses bloom filters to accelerate queries and reduce I/O.
*   **Encryption:** Supports encryption for securing data.

## Installation

This repository contains the core definitions and build configuration. To build and use the Parquet format, you'll typically use a Parquet library specific to your programming language. 

Here's a general outline of building the project if you intend to work with the source code directly (e.g. for contributing):

1.  **Prerequisites:**
    *   Java Development Kit (JDK) 8 or higher
    *   Maven
    *   Git
    *   Thrift Compiler (`thrift`)

2.  **Clone the Repository:**

    ```bash
    git clone https://github.com/apache/parquet-format.git
    cd parquet-format
    ```

3.  **Build the Project:**

    ```bash
    mvn clean install
    ```

Building uses Maven to manage dependencies and build the project.

## Usage

The primary usage of this repository is as a foundation for other projects that implement Parquet readers and writers. 

*   **Using Parquet Libraries:**  The common use case is to utilize existing Parquet libraries in your application.  Examples of popular libraries include:
    *   **Apache Arrow:** Provides a Parquet implementation in C++, Python, Java, and other languages.
    *   **Parquet4J:** A native Java implementation.
    *   **Spark/Hive:**  Spark and Hive have built-in Parquet support.
*   **Schema Definition:** To create Parquet files, you need to define a schema that specifies the data types and structure of your data. This schema is represented using `SchemaElement` structs.
*   **Writing Parquet Files:** Use a Parquet library to write data to files according to the defined schema and desired encoding/compression settings.
*   **Reading Parquet Files:** Use a Parquet library to read data from files and access the data according to the schema.
*  **Changelog:** To generate a change log use the included `changelog.sh` script:

    ```bash
    ./changelog.sh
    ```

## Repository Structure

*   `.asf.yaml`: Configuration file for Apache Software Foundation projects.
*   `.github/`: Contains GitHub configuration files.
*   `LICENSE`: The Apache License 2.0.
*   `NOTICE`: Describes copyright and attributions.
*   `src/main/thrift/parquet.thrift`: Thrift file defining the Parquet data structures.  This is used to generate code in various languages.
*   `src/main/resources/META-INF/LICENSE`: License information.
*   `pom.xml`: Maven project object model file, containing build configuration.
*   `doc/`: Documentation related to the Parquet format.
*   `dev/`: Scripts for release management and development tasks.

## Contributing

Please see the [CONTRIBUTING.md](https://github.com/apache/parquet-format/blob/master/CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the [Apache License, Version 2.0](LICENSE).

## Contact

*   **Website:** [https://parquet.apache.org/](https://parquet.apache.org/)
*   **Mailing Lists:** [https://parquet.apache.org/community/](https://parquet.apache.org/community/)