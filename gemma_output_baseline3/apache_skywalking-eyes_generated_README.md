# Skywalking Eyes

## Description

Skywalking Eyes is a full-featured license tool to check and fix license headers and resolve dependencies' licenses.

## Features

*   License header checking and fixing
*   Dependency license resolution
*   Support for a wide range of license types
*   Automatic license compatibility checking

## Prerequisites / Requirements

*   Go 1.25 or later
*   Docker (for building and running the application)

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/apache/skywalking-eyes
    cd skywalking-eyes
    ```
2.  Install dependencies:
    ```bash
    go mod download
    ```
3.  Build the application:
    ```bash
    make
    ```

## Usage

To check license headers in a directory:

```bash
./skywalking-eyes check <directory>
```

To fix license headers in a directory:

```bash
./skywalking-eyes fix <directory>
```

To resolve dependencies' licenses:

```bash
./skywalking-eyes dependency check
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Write tests for your changes.
4.  Submit a pull request.

## License

This project is licensed under the Apache License, Version 2.0. See the `LICENSE` file for more information.

## Contact / Authors

Apache Skywalking Team