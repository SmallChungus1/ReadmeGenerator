# SkyWalking Eyes: License Compliance Tool

## Description

SkyWalking Eyes is a comprehensive license compliance tool designed to automate the detection and enforcement of license headers and dependency licensing in software projects. It provides two core capabilities: checking and fixing license headers in source code files, and analyzing the compatibility of software dependencies to ensure they adhere to organizational licensing policies.

Built with a focus on developer experience, SkyWalking Eyes integrates seamlessly into CI/CD pipelines and supports multiple programming languages including Go, Java, and Node.js. Its modular architecture allows for flexible configuration, enabling teams to enforce strict compliance with specific license requirements while maintaining permissive compatibility with common open-source licenses.

## Features

- **License Header Enforcement**: Automatically scans source code files for missing or incorrect license headers and can automatically insert compliant headers.
- **Dependency Licensing Analysis**: Resolves and analyzes the licenses of all project dependencies to ensure compatibility with the project's primary license.
- **License Compatibility Checking**: Evaluates whether project dependencies are compatible with each other and with the project's primary license, based on established SPDX compatibility matrices.
- **Multi-Language Support**: Supports Go, Java, and Node.js projects through language-specific dependency parsing and header detection.
- **Configurable Rules**: Customizable rules for license header patterns, file paths, and dependency analysis through a flexible configuration system.
- **CI/CD Integration**: Designed to work seamlessly in GitHub Actions, Jenkins, and other CI/CD environments with built-in pull request commenting.
- **Compliance Reporting**: Generates detailed reports on license compliance status, including failure summaries and dependency compatibility analysis.

## Installation

### Prerequisites
- Go 1.25 or later
- Docker (optional, for containerized execution)

### Build from Source
```bash
# Clone the repository
git clone https://github.com/apache/skywalking-eyes.git
cd skywalking-eyes

# Build the tool
make build

# Install the binary globally (optional)
make install
```

### Install via Docker
```bash
# Pull the pre-built image
docker pull apache/skywalking-eyes:latest

# Run the tool in a container
docker run --rm -v $(pwd):/app apache/skywalking-eyes:latest license-eye --help
```

## Usage

### Check License Headers
```bash
# Check all files in the current directory
license-eye header check

# Check specific files or directories
license-eye header check ./src/main.go ./src/utils/

# Check and fix missing headers
license-eye header fix ./src
```

### Analyze Dependency Licenses
```bash
# Check dependency license compatibility
license-eye dependency check

# Resolve and generate a summary of dependency licenses
license-eye dependency resolve --summary dist/LICENSE.tpl --output dist/licenses/

# Check with specific flags
license-eye dependency check --fsf-free --osi-approved
```

### Configure License Settings
Create a `.licenserc.yaml` file in your project root with the following content:

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
  paths-ignore: ["dist", "licenses", "**/*.md"]

dependency:
  files:
    - go.mod
  licenses:
    - name: github.com/chzyer/logex
      version: v1.1.10
      license: MIT
```

### Run in CI/CD Pipeline (GitHub Actions)
```yaml
# .github/workflows/license-check.yml
name: License Compliance Check
on: [push, pull_request]

jobs:
  license-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Go
        uses: actions/setup-go@v6
        with:
          go-version: 1.25
      - name: License Compliance Check
        run: |
          license-eye header check --log=info --config=.licenserc.yaml
          license-eye dependency check --log=info --config=.licenserc.yaml
```

### Example: Go Project
```bash
# Navigate to your Go project
cd my-go-project

# Run license checks
license-eye header check
license-eye dependency check

# Generate a full license report
license-eye dependency resolve --summary LICENSE.md --output licenses/
```

The tool will scan your Go module's `go.mod` file, parse all dependencies, and check if they are compatible with the project's primary license (Apache-2.0 in this example). It will generate a detailed report showing which dependencies are compatible and which may require further review.