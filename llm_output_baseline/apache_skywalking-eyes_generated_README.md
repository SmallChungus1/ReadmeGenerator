# SkyWalking Eyes: License Compliance & Dependency Analysis Tool

![Build Status](https://github.com/apache/skywalking-eyes/actions/workflows/build.yml/badge.svg)
![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)

---

## Description

**SkyWalking Eyes** is a comprehensive open-source license compliance tool designed to automate the detection, analysis, and enforcement of license headers and dependency licenses in software projects. Built on the Apache Software Foundation's principles, it helps developers and organizations ensure their code adheres to open-source licensing standards, reducing legal risk and promoting transparency.

At its core, SkyWalking Eyes provides two critical capabilities:
- **License Header Enforcement**: Automatically checks and fixes license headers in source files to ensure compliance with project-specific license requirements.
- **Dependency License Analysis**: Resolves and verifies the compatibility of third-party dependencies' licenses, preventing potential legal conflicts in software distribution.

This tool is ideal for open-source contributors, software maintainers, and compliance officers who need to ensure their codebase remains legally sound and adheres to community standards.

---

## Features

- ✅ **License Header Compliance**: Automatically scans source files for missing or incorrect license headers and fixes them with a configurable template.
- ✅ **Dependency License Resolution**: Analyzes project dependencies (Go, Java, Node.js, Ruby, Maven, etc.) to identify all used licenses and their compatibility.
- ✅ **License Compatibility Checking**: Uses a comprehensive compatibility matrix to determine if a project's license is compatible with its dependencies.
- ✅ **Configurable Rules**: Customize license headers, paths to scan, and dependency analysis settings via a flexible configuration file.
- ✅ **Integration with CI/CD**: Seamlessly integrates with GitHub Actions and other CI platforms to enforce license compliance automatically.
- ✅ **Cross-Platform Support**: Works on Windows, macOS, and Linux with native support for all major programming languages.
- ✅ **Automated Reporting**: Generates detailed reports on license compliance and dependency issues for audit and review.

---

## Table of Contents

- [Project Title](#project-title)
- [Description](#description)
- [Features](#features)
- [Prerequisites / Requirements](#prerequisites--requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

---

## Prerequisites / Requirements

- **Go 1.25+** (for building and running the tool)
- **Git** (for version control and repository management)
- **Docker** (optional, for containerized execution)
- A modern code editor or IDE (e.g., VS Code, IntelliJ, Vim)

> Note: The tool supports scanning and analyzing projects in multiple languages including Go, Java, Node.js, and Ruby through built-in parsers.

---

## Installation

### Option 1: Install via Binary (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/apache/skywalking-eyes.git
   cd skywalking-eyes
   ```

2. **Build the binary**:
   ```bash
   make build
   ```

3. **Install globally** (optional):
   ```bash
   make install
   ```

   This installs the `license-eye` binary to your system's `PATH`.

---

### Option 2: Use Docker

1. **Pull the image**:
   ```bash
   docker pull apache/skywalking-eyes:latest
   ```

2. **Run the tool**:
   ```bash
   docker run --rm -v $(pwd):/project apache/skywalking-eyes:latest license-eye check
   ```

---

### Option 3: Install via Package Manager (Linux/macOS)

On Debian/Ubuntu:
```bash
sudo apt-get install license-eye
```

On macOS (Homebrew):
```bash
brew install license-eye
```

---

## Usage

### Basic Commands

| Command | Description |
|--------|-------------|
| `license-eye header check` | Checks all files for license headers (no changes) |
| `license-eye header fix` | Automatically adds or fixes missing license headers |
| `license-eye dependency check` | Checks if all dependencies are compatible with the project license |
| `license-eye dependency resolve` | Resolves all dependency licenses and generates a summary |

---

### Example: Scan and Fix License Headers

```bash
# Check all files in the current directory
license-eye header check

# Fix missing headers in all files
license-eye header fix

# Show detailed output with file paths
license-eye header check --verbose
```

---

### Example: Analyze Dependencies

```bash
# Check license compatibility of all dependencies
license-eye dependency check --fsf-free

# Resolve all dependency licenses and save to a file
license-eye dependency resolve --summary dist/LICENSE.tpl --output dist/licenses/
```

> The tool will generate a comprehensive report showing which dependencies are compatible, which are not, and which require further review.

---

### Configuration File

The tool reads configuration from a `.licenserc.yaml` file located in the project root. Example configuration:

```yaml
header:
  license:
    spdx-id: Apache-2.0
    copyright-owner: Apache Software Foundation
    content: |
      Licensed to the Apache Software Foundation (ASF) under one
      or more contributor license agreements.  See the NOTICE file
      distributed with this work for additional information
      regarding copyright ownership.  The ASF licenses this file
      to you under the Apache License, Version 2.0 (the
      "License"); you may not use this file except in compliance
      with the License.  You may obtain a copy of the License at
      http://www.apache.org/licenses/LICENSE-2.0
      Unless required by applicable law or agreed to in writing,
      software distributed under the License is distributed on an
      "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
      KIND, either express or implied.  See the License for the
      specific language governing permissions and limitations
      under the License.

  paths: ["**"]
  paths-ignore: ["dist", "licenses", "*.md"]

dependency:
  files:
    - go.mod
  licenses:
    - name: github.com/chzyer/logex
      version: v1.1.10
      license: MIT
```

---

## Contributing

We welcome contributions from the open-source community! Please follow these guidelines:

1. **Fork the repository** on GitHub.
2. **Create a feature branch** for your changes.
3. **Submit a pull request** with a clear description of your changes.
4. **Run the test suite** before submitting:
   ```bash
   make test
   ```

> All contributions are reviewed under the Apache License 2.0. Please ensure your code follows the project's style and standards.

For bug reports or feature requests, please open an issue in the GitHub repository.

---

## License

This project is licensed under the **Apache License, Version 2.0**. See the [LICENSE](LICENSE) file for details.

---

## Contact / Authors

- **Project Maintainers**: Apache Software Foundation (ASF)
- **Primary Contact**: [license@apache.org](mailto:license@apache.org)
- **GitHub Repository**: [https://github.com/apache/skywalking-eyes](https://github.com/apache/skywalking-eyes)
- **Documentation**: [https://skywalking.apache.org/](https://skywalking.apache.org/)

For questions or feedback, please reach out to the community via the official Apache mailing lists or GitHub Issues.