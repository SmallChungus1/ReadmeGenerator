# SkyWalking Eyes

## Description
SkyWalking Eyes is a license compliance tool designed to check and fix license headers in source code files and resolve license dependencies to ensure compliance with open-source licensing requirements. It provides automated checks for license header presence, compatibility between dependencies, and helps maintain a clear and compliant codebase.

## Features
- **License Header Validation**: Checks that all source files contain the required license header.
- **Header Fixing**: Automatically inserts or updates license headers in files that are missing them.
- **Dependency License Resolution**: Identifies and analyzes license information for project dependencies.
- **License Compatibility Checking**: Determines if dependencies' licenses are compatible with each other.
- **Configuration-Driven**: Uses a flexible configuration system to define license headers, paths, and compatibility rules.
- **Cross-Language Support**: Supports multiple programming languages including Go, Java, and Node.js.

## Prerequisites / Requirements
- Go 1.25 or later
- A modern operating system (Linux, macOS, or Windows)
- Internet access for dependency resolution and license data lookup

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/apache/skywalking-eyes.git
   cd skywalking-eyes
   ```

2. Build the tool:
   ```bash
   make build
   ```

3. Install the binary (optional):
   ```bash
   make install
   ```

## Usage
### Check License Headers
```bash
license-eye header check
```

### Fix Missing Headers
```bash
license-eye header fix
```

### Check Dependency Licenses
```bash
license-eye dependency check
```

### Resolve Dependency Licenses
```bash
license-eye dependency resolve --summary dist/LICENSE.tpl
```

### Run with Custom Configuration
```bash
license-eye header check --config .licenserc.yaml --mode fix
```

### Use in CI/CD
The tool can be integrated into continuous integration pipelines using GitHub Actions:
```yaml
- name: Run License Eye
  run: |
    license-eye header check --config .licenserc.yaml
```

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear, descriptive messages.
4. Push to your fork and open a pull request.

For contributions related to license compatibility rules, ensure the changes are based on the official SPDX license compatibility matrix and properly cite the source.

## License
This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE-linguist) file for details.

## Contact / Authors
For questions or feedback, please contact the Apache Software Foundation team.

- Project Maintainers: Apache Software Foundation
- Documentation: https://skywalking.apache.org/
- Issue Tracker: https://github.com/apache/skywalking-eyes/issues