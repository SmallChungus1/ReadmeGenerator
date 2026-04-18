# SkyWalking Eyes: License Compliance & Dependency Analysis Tool

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Build Status](https://github.com/apache/skywalking-eyes/actions/workflows/ci.yml/badge.svg?branch=main)
![GitHub Issues](https://img.shields.io/github/issues/apache/skywalking-eyes.svg)

---

## Description

**SkyWalking Eyes** is a comprehensive open-source license compliance and dependency analysis tool designed to help developers and organizations ensure their software projects adhere to legal and licensing requirements. It provides two core capabilities:

1. **License Header Enforcement**: Automatically checks and fixes license headers in source code files to ensure compliance with project-specific licensing terms.
2. **Dependency License Analysis**: Resolves and analyzes the licenses of all project dependencies to detect potential compatibility issues and ensure adherence to open-source licensing policies.

SkyWalking Eyes is particularly valuable for large-scale projects, open-source contributions, and organizations that must comply with strict open-source licensing guidelines. It integrates seamlessly into CI/CD pipelines and development workflows to prevent license violations before code is merged or released.

---

## Features

- ✅ **License Header Compliance**: Automatically checks all source files for required license headers and fixes missing or incorrect ones.
- ✅ **Dependency License Resolution**: Analyzes project dependencies (Go, Java, Node.js, Ruby, Maven, etc.) to identify their licenses.
- ✅ **License Compatibility Checks**: Determines if dependencies' licenses are compatible with the project's primary license (e.g., Apache-2.0).
- ✅ **Flexible Configuration**: Customizable license headers, paths, and compatibility rules via configuration files.
- ✅ **CI/CD Integration**: Works with GitHub Actions, GitLab CI, and other platforms to enforce compliance automatically.
- ✅ **Multi-Language Support**: Supports Go, Java, Node.js, Ruby, and other common languages with built-in parsers.
- ✅ **Comprehensive Reporting**: Generates detailed reports on license compliance and dependency issues.
- ✅ **Actionable Feedback**: Provides clear, actionable feedback to developers during code reviews or PRs.

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
- **A modern terminal** (bash/zsh/sh)
- **Access to a Linux/Unix-like environment** (or WSL)
- **Basic understanding of open-source licensing** (recommended)

---

## Installation

### Option 1: Install via GitHub Actions (Recommended)

SkyWalking Eyes is designed to be used as a CI/CD tool. Install it directly in your workflow:

```bash
# Add to your GitHub Actions workflow
- name: Install License Eye
  run: |
    curl -sfL https://raw.githubusercontent.com/apache/skywalking-eyes/main/action.yml | \
    yq -r '.steps[0].run' | \
    bash -s
```

### Option 2: Build from Source

1. Clone the repository:
```bash
git clone https://github.com/apache/skywalking-eyes.git
cd skywalking-eyes
```

2. Build the tool:
```bash
make build
```

3. Install locally:
```bash
make install
```

> The tool will be installed to `~/.local/bin/license-eye`.

---

## Usage

### 1. Check License Headers

```bash
license-eye header check
```

This checks all files in the current directory (or defined in config) for the required license header. It reports any missing or mismatched headers.

### 2. Fix Missing Headers

```bash
license-eye header fix
```

Automatically inserts the required license header into files that are missing it.

### 3. Analyze Dependencies

```bash
license-eye dependency check
```

Checks if all project dependencies are compatible with the project's license (e.g., Apache-2.0).

```bash
license-eye dependency resolve --summary dist/LICENSE.tpl
```

Resolves all dependency licenses and generates a summary file in the `dist/` directory.

### 4. Configuration

The tool uses a configuration file (`license-eye.yaml` or `.licenserc.yaml`) to define:

- Required license header content
- Paths to check
- License compatibility rules
- Paths to ignore

Example configuration (`license-eye.yaml`):
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
  paths:
    - "**"
  paths-ignore:
    - "dist"
    - "licenses"
    - "**/*.md"
```

### 5. GitHub Actions Example

```yaml
name: License Compliance Check
on: [push, pull_request]

jobs:
  license-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install License Eye
        run: |
          make -C $GITHUB_ACTION_PATH install
      - name: Check license headers
        run: license-eye header check --config .licenserc.yaml
      - name: Check dependency licenses
        run: license-eye dependency check --config .licenserc.yaml
```

---

## Contributing

We welcome contributions to SkyWalking Eyes! Please follow these guidelines:

1. **Fork the repository** on GitHub
2. **Create a new feature branch** (e.g., `feature/license-header-regex`)
3. **Submit a pull request** with clear descriptions of changes
4. **Ensure all tests pass** before submitting
5. **Update documentation** as needed

For bug reports or feature requests, please open an issue in the repository.

> See the [CONTRIBUTING.md](https://github.com/apache/skywalking-eyes/blob/main/CONTRIBUTING.md) file for detailed contribution guidelines.

---

## License

SkyWalking Eyes is licensed under the **Apache License, Version 2.0**. See the [LICENSE](https://github.com/apache/skywalking-eyes/blob/main/LICENSE) file for details.

---

## Contact / Authors

- **Project Maintainers**: Apache Software Foundation (ASF)
- **Primary Developer**: Apache Open Source Community
- **Community Forum**: [Apache Software Foundation](https://www.apache.org/)
- **GitHub**: [apache/skywalking-eyes](https://github.com/apache/skywalking-eyes)
- **Documentation**: [SkyWalking Eyes Docs](https://skywalking.apache.org/docs/license-eye/)

For questions, feature requests, or bug reports, please open an issue on GitHub or contact the Apache Software Foundation directly.