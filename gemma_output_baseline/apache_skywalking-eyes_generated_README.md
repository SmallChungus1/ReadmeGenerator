# Apache SkyWalking Eyes

[![Build Status](https://github.com/apache/skywalking-eyes/actions/workflows/ci.yml/badge.svg)](https://github.com/apache/skywalking-eyes/actions/workflows/ci.yml)

## Description

Apache SkyWalking Eyes is a full-featured license tool to check and fix license headers and resolve dependencies' licenses. It helps ensure compliance with software licenses in your projects.

## Features

*   Checks for missing or incorrect license headers in source code files.
*   Fixes license headers automatically.
*   Resolves dependencies and checks their licenses.
*   Supports a wide range of license types.
*   Configurable through a YAML configuration file.
*   Provides a command-line interface for easy use.

## Table of Contents

1.  [Prerequisites / Requirements](#prerequisites--requirements)
2.  [Installation](#installation)
3.  [Usage](#usage)
4.  [Contributing](#contributing)
5.  [License](#license)
6.  [Contact / Authors](#contact--authors)

## Prerequisites / Requirements

*   Go 1.25 or later
*   Docker (optional, for building and running in a container)

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/apache/skywalking-eyes.git
    cd skywalking-eyes
    ```

2.  Build the project:

    ```bash
    make
    ```

3.  Install the binary:

    ```bash
    make install
    ```

    This will install the `license-eye` executable in `/usr/local/bin`.

## Usage

```bash
license-eye header check
license-eye header fix
license-eye dependency check
```

### Example: Checking License Headers

```bash
license-eye header check
```

This command checks the license headers in the current directory and its subdirectories, based on the configuration in `.licenserc.yaml`.

### Example: Fixing License Headers

```bash
license-eye header fix
```

This command fixes the license headers in the current directory and its subdirectories, based on the configuration in `.licenserc.yaml`.

### Example: Checking Dependency Licenses

```bash
license-eye dependency check
```

This command resolves the dependencies of the project (e.g., Go modules) and checks their licenses.

## Contributing

Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to the project.

## License

This project is licensed under the [Apache License 2.0](LICENSE).

## Contact / Authors

*   Apache SkyWalking Community: [https://skywalking.apache.org/](https://skywalking.apache.org/)