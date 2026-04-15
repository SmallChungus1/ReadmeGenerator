# Apache SkyWalking Eyes

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Build Status](https://github.com/apache/skywalking-eyes/actions/workflows/ci.yml/badge.svg?branch=main)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?logo=github)
![Apache Software Foundation](https://img.shields.io/badge/ASF-%23000000.svg?logo=apache)

> **Apache SkyWalking Eyes** is a powerful, open-source license compliance tool designed to automate the detection, analysis, and enforcement of license headers and dependencies in software projects. It ensures that all source code files have proper license headers and that the licenses of dependencies are compatible with the project's chosen license, helping developers avoid legal risks and maintain compliance with open-source licensing standards.

---

## Description

Apache SkyWalking Eyes is a full-featured license compliance tool that automates the process of checking and fixing license headers in source code files and analyzing the license compatibility of project dependencies. It is built to help developers, open-source contributors, and organizations maintain legal compliance with open-source licenses by:

- **Checking license headers**: Verifies that all source files have the required license header in the correct format and location.
- **Resolving dependency licenses**: Analyzes the licenses of dependencies (e.g., in `go.mod`, `pom.xml`, `Gemfile.lock`) and checks for compatibility with the project's primary license.
- **Enforcing compliance**: Can automatically fix missing or incorrect headers and report violations via pull requests or CI/CD pipelines.

This tool is especially valuable in large-scale open-source projects where manual license audits are impractical. It integrates seamlessly with modern development workflows, including GitHub Actions, GitLab CI, and local development environments.

---

## Features

- ✅ **License Header Validation**: Checks that all source files have the correct license header (e.g., Apache-2.0) in the specified format.
- ✅ **Dependency License Analysis**: Resolves and checks the compatibility of all dependencies (Go, Java, Node.js, Ruby, etc.) with the project's license.
- ✅ **Flexible Configuration**: Customize license headers, paths to check, and compatibility rules via a YAML configuration file.
- ✅ **Automated Fixing**: Automatically inserts or updates license headers in files that are missing them.
- ✅ **CI/CD Integration**: Works with GitHub Actions, GitLab CI, and other platforms to enforce compliance in pull requests.
- ✅ **Comprehensive License Compatibility Matrix**: Built-in compatibility rules for over 100 open-source licenses (e.g., Apache-2.0, MIT, GPL, LGPL, MPL).
- ✅ **Multi-language Support**: Supports Go, Java, Node.js, Ruby, and more.
- ✅ **Customizable Output**: Generates detailed reports and summaries of license compliance.

---

## Table of Contents

- [Prerequisites / Requirements](#prerequisites--requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

---

## Prerequisites / Requirements

- **Go 1.25+** (for building and running the CLI)
- **Git** (for version control and repository management)
- **Node.js** (optional, for Node.js project support)
- **Java JDK 11+** (optional, for Java project support)
- A modern operating system (Linux, macOS, or Windows)

> The tool is cross-platform and supports Windows, macOS, and Linux. Docker images are available for containerized deployment.

---

## Installation

### Option 1: Install via Binary (Recommended)

1. **Download the binary** from the [Apache SkyWalking Eyes Releases page](https://github.com/apache/skywalking-eyes/releases).
2. **Place the binary** in your `PATH` or run it directly.

```bash
# Example: Download and install on Linux/macOS
curl -L https://github.com/apache/skywalking-eyes/releases/download/v1.0.0/license-eye-linux-amd64 -o license-eye
chmod +x license-eye
sudo mv license-eye /usr/local/bin/
```

3. **Verify installation**:

```bash
license-eye --version
```

> The latest version is available in the [releases](https://github.com/apache/skywalking-eyes/releases) section.

---

### Option 2: Build from Source

1. **Clone the repository**:

```bash
git clone https://github.com/apache/skywalking-eyes.git
cd skywalking-eyes
```

2. **Install Go dependencies**:

```bash
go mod download
```

3. **Build the binary**:

```bash
make build
```

4. **Run the binary**:

```bash
./bin/linux/license-eye
```

> The build process includes a full test suite and generates binaries for multiple platforms.

---

### Option 3: Use Docker

Run the tool in a containerized environment:

```bash
docker run --rm -v $(pwd):/github/workspace apache/skywalking-eyes:latest license-eye check
```

For more advanced usage, see the [examples](./examples) directory.

---

## Usage

### 1. Check License Headers

Verify that all files in a directory have the correct license header:

```bash
license-eye header check
```

> This command scans all files (by default) and reports any missing or incorrect headers.

### 2. Fix Missing Headers

Automatically insert the correct license header into files that are missing it:

```bash
license-eye header fix
```

> This command will modify files in place and output a summary of changes.

### 3. Check Dependency License Compatibility

Analyze the licenses of dependencies and ensure they are compatible with the project's primary license:

```bash
license-eye dependency check
```

> This checks all dependencies (e.g., in `go.mod`, `pom.xml`) and reports any incompatible licenses.

### 4. Resolve and Generate Dependency Summary

Resolve all dependency licenses and generate a summary file (e.g., `LICENSE`):

```bash
license-eye dependency resolve --summary dist/LICENSE.tpl
```

> This creates a `dist/licenses/` directory with a summary of all dependency licenses.

### 5. Configure License Settings

Edit the configuration file `./.licenserc.yaml` to customize:

- The license header content
- Paths to check
- Paths to ignore
- Compatibility rules (e.g., only allow FSF-free licenses)

Example configuration:

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
  paths-ignore: ["dist", "**/*.md"]
```

---

## Contributing

We welcome contributions from the open-source community! Please follow these guidelines:

- ✅ Open issues or feature requests on [GitHub Issues](https://github.com/apache/skywalking-eyes/issues)
- ✅ Submit pull requests with clear descriptions and tests
- ✅ Follow the [Apache Software Foundation contribution guidelines](https://www.apache.org/foundation/contributing.html)
- ✅ Ensure all code changes are covered by unit tests and CI checks

> All contributions are reviewed by the Apache Software Foundation (ASF) team.

---

## License

Apache SkyWalking Eyes is licensed under the **Apache License, Version 2.0**.

> See the [LICENSE](./licenses/LICENSE-linguist) file for details.

---

## Contact / Authors

**Project Maintainers**:
- Apache Software Foundation (ASF)

**Project Website**: [https://skywalking.apache.org](https://skywalking.apache.org)

**GitHub Repository**: [https://github.com/apache/skywalking-eyes](https://github.com/apache/skywalking-eyes)

**Report Issues**: [https://github.com/apache/skywalking-eyes/issues](https://github.com/apache/skywalking-eyes/issues)

**Join the Community**: [Apache Software Foundation](https://www.apache.org)

> For questions or feedback, please reach out to the ASF team via the GitHub repository or community mailing lists.