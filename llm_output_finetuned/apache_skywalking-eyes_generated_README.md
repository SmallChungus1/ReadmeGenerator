# Apache SkyWalking Eyes

## Description

Apache SkyWalking Eyes is a comprehensive open-source license management tool designed to automate the detection, verification, and enforcement of license compliance in software projects. It provides two core capabilities: **license header checking** and **dependency license analysis**. The tool ensures that all source files contain the required license headers and that the licenses of all project dependencies are compatible with the project's primary license, helping to prevent legal risks associated with copyleft or restrictive licenses.

Built as a command-line interface (CLI) tool, SkyWalking Eyes integrates seamlessly into development workflows, CI/CD pipelines, and pull request reviews. It supports multiple programming languages and offers both a standalone command-line experience and integration with GitHub Actions for automated license compliance checks.

## Features

- ✅ **License Header Verification**: Checks that all source files contain the correct license header as defined in the configuration.
- ✅ **License Header Fixing**: Automatically inserts or updates missing license headers in source files.
- ✅ **Dependency License Analysis**: Resolves and checks the compatibility of all project dependencies' licenses against the project's primary license.
- ✅ **License Compatibility Matrix**: Built-in compatibility rules for over 100 open-source licenses, including permissive (e.g., MIT, Apache-2.0) and copyleft (e.g., GPL, LGPL) licenses.
- ✅ **Flexible Configuration**: Customizable via a `.licenserc.yaml` file to define license headers, paths to check, and license compatibility rules.
- ✅ **Multi-Language Support**: Supports Go, Java, JavaScript/Node.js, and other common languages through language-specific dependency parsers.
- ✅ **CI/CD Integration**: Works with GitHub Actions to automatically check license compliance on pull requests.
- ✅ **Cross-Platform**: Available for Windows, macOS, and Linux via native binaries or Docker containers.
- ✅ **Comprehensive Reporting**: Generates detailed reports on license compliance, including failures and compatibility issues.

## Installation

### Option 1: Install via Docker (Recommended)

```bash
# Pull the latest image
docker pull apache/skywalking-eyes:latest

# Run the container
docker run --rm -v $(pwd):/github/workspace apache/skywalking-eyes:latest
```

### Option 2: Build from Source

1. Clone the repository:
```bash
git clone https://github.com/apache/skywalking-eyes.git
cd skywalking-eyes
```

2. Build the binary:
```bash
make build
```

3. Install the binary:
```bash
sudo make install
```

### Option 3: Install via Binary (Direct Download)

1. Download the binary for your platform:
```bash
# For Linux
wget https://github.com/apache/skywalking-eyes/releases/download/v1.0.0/skywalking-eyes-linux-amd64.tar.gz
tar -xzf skywalking-eyes-linux-amd64.tar.gz
```

2. Move to a system path:
```bash
sudo mv skywalking-eyes /usr/local/bin/
```

## Usage

### 1. Basic License Header Check

Verify that all files have the required license header:

```bash
license-eye header check
```

### 2. Fix Missing License Headers

Automatically insert license headers into missing files:

```bash
license-eye header fix
```

### 3. Check Dependency License Compatibility

Verify that all project dependencies are compatible with the project's license:

```bash
license-eye dependency check
```

### 4. Resolve Dependencies and Generate License Summary

Resolve all dependencies and generate a summary of licenses in a `LICENSE` file:

```bash
license-eye dependency resolve --summary dist/LICENSE.tpl --output dist/licenses/
```

### 5. GitHub Actions Integration

Add to your `.github/workflows/license.yml`:

```yaml
name: License Eye
on: [pull_request]

jobs:
  license-eye:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/setup-go@v6
        with:
          go-version: 1.25
      - name: Run license-eye
        run: |
          make -C $GITHUB_ACTION_PATH install
          license-eye -v info -c .licenserc.yaml header check
          license-eye -v info -c .licenserc.yaml dependency check
```

### 6. Example Configuration (`licenserc.yaml`)

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
  paths-ignore: ["dist", "**/*.md", "**/testdata/**"]

dependency:
  files:
    - go.mod
  licenses:
    - name: github.com/chzyer/logex
      version: v1.1.10
      license: MIT
```

> **Note**: The tool uses a standard Apache-2.0 license by default, which is permissive and compatible with many other open-source licenses. You can customize this in the configuration file.