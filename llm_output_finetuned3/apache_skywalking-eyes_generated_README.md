# Apache SkyWalking Eyes

## Description

Apache SkyWalking Eyes is a command-line tool designed to help developers and maintainers enforce license compliance in software projects. It provides two core capabilities:

1. **License Header Enforcement**: Checks and automatically fixes license headers in source code files to ensure they follow a standardized format.
2. **Dependency License Analysis**: Resolves and checks the compatibility of licenses in project dependencies, helping to avoid legal risks from combining incompatible open-source licenses.

The tool is built as a CLI application with support for multiple programming languages and integrates with GitHub Actions for automated license checks in pull requests.

## Features

- **License Header Checking and Fixing**: Validates that source files contain the required license header and automatically inserts it when missing.
- **Dependency License Analysis**: Analyzes project dependencies (Go, Java, Node.js) to determine license compatibility.
- **Configurable License Policies**: Supports custom license configurations through a configuration file (`.licenserc.yaml`).
- **Multiple Language Support**: Works with Go, Java, and Node.js projects.
- **GitHub Actions Integration**: Can be used as a GitHub Action to automatically check license compliance in pull requests.
- **License Compatibility Matrix**: Built-in compatibility rules for over 100 open-source licenses, including permissive and copyleft licenses.
- **Flexible Configuration**: Supports custom paths, comment styles, and license templates.

## Prerequisites / Requirements

- Go 1.25 or later
- A modern operating system (Linux, macOS, or Windows)
- A project with source code files that need license header enforcement
- Access to a Git repository (for GitHub Actions integration)

## Installation

### From Source

1. Clone the repository:
```bash
git clone https://github.com/apache/skywalking-eyes.git
cd skywalking-eyes
```

2. Build the tool:
```bash
make build
```

3. Install the binary:
```bash
make install
```

The binary will be installed to `/usr/local/bin/license-eye`.

### Using Docker

1. Pull the official image:
```bash
docker pull apache/skywalking-eyes:latest
```

2. Run the tool:
```bash
docker run --rm -v $(pwd):/github/workspace apache/skywalking-eyes:latest license-eye --help
```

## Usage

### License Header Checking and Fixing

```bash
# Check license headers in the current directory
license-eye header check

# Fix missing license headers in the current directory
license-eye header fix

# Check and fix headers in specific paths
license-eye header check path/to/dir
license-eye header fix path/to/dir
```

### Dependency License Analysis

```bash
# Check license compatibility in dependencies
license-eye dependency check

# Resolve and summarize dependency licenses
license-eye dependency resolve --summary dist/LICENSE.tpl --output dist/licenses/
```

### GitHub Actions Integration

The repository includes GitHub Actions workflows that can be used to automatically check license compliance in pull requests:

- `action.yml` defines a GitHub Action that runs license checks
- The action can be configured to comment on pull requests when license issues are found
- It supports both `check` and `fix` modes

To use in a repository:
1. Add the action to your `.github/workflows/license-check.yml` file
2. Configure the `token` and `config` parameters as needed

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Commit your changes with clear, descriptive messages
4. Push to the branch and open a pull request

For license compatibility rules, ensure your changes are consistent with the existing compatibility matrix and properly documented.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.

## Contact / Authors

Project maintained by the Apache Software Foundation.

For questions or issues, please open an issue on the GitHub repository.