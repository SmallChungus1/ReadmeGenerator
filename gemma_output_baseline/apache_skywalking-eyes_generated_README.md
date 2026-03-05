# README for Skywalking-Eyes

## Description

Skywalking-Eyes is a full-featured license tool designed to check and fix license headers and resolve dependencies' licenses. It's developed by the Apache community and is intended to help ensure that software projects comply with their licensing terms.  It provides functionalities for:

*   **License Header Checking:** Verifies that source code files contain the correct license headers.
*   **License Header Fixing:** Automatically adds or corrects license headers in source code files.
*   **Dependency License Resolution:** Identifies the licenses used by project dependencies and can generate reports.

## Features

*   **License Header Management:**  Checks for the presence and correctness of license headers in source code. Automatic fixing capabilities are also available.
*   **Dependency Analysis:** Resolves and reports the licenses used by project dependencies.
*   **Multiple Language Support:** Supports a wide range of programming languages.
*   **Configuration Options:** Highly configurable through a YAML configuration file (.licenserc.yaml).
*   **Command-Line Interface:** Easy to use from the command line.
*   **Integration with CI/CD:** Can be integrated into continuous integration/continuous delivery pipelines.
*   **Comprehensive License Database**:  Includes a large database of license identifiers and associated information.
*   **Summary Reports:** Generates summary reports of license compliance.
*   **Customizable Templates**: Allows for custom templates to be used for report generation.

## Installation

You can install Skywalking-Eyes in several ways:

**1. Pre-built Binary:**

Download a pre-built binary from the [releases page](https://github.com/apache/skywalking-eyes/releases).  Make sure download the version that corresponds to your operating system and architecture.

**2. Building from Source:**

   *   **Prerequisites:**
        *   Go 1.25 or higher
        *   Make
   *   **Steps:**
        ```bash
        git clone https://github.com/apache/skywalking-eyes.git
        cd skywalking-eyes
        make
        ```
        This will build the `license-eye` executable in the `bin` directory.

**3. Docker:**
   ```bash
   docker pull ghcr.io/apache/skywalking-eyes:latest
   ```

## Usage

Skywalking-Eyes is primarily used through a command-line interface. Here are some common examples:

*   **Check License Headers:**

    ```bash
    license-eye header check
    ```

*   **Fix License Headers:**

    ```bash
    license-eye header fix
    ```

*   **Resolve Dependencies Licenses:**

    ```bash
    license-eye dependency resolve
    ```

*   **Resolve Dependencies Licenses and Output Summary:**

    ```bash
    license-eye dependency resolve -s summary.tmpl
    ```
    This command will create a `LICENSE` file in the same directory as `summary.tmpl`.

*   **Help:**

    ```bash
    license-eye help
    license-eye header help
    license-eye dependency help
    ```

## Configuration

Skywalking-Eyes uses a configuration file named `.licenserc.yaml` to define licensing rules and settings. The configuration file allows you to:

*   Specify the license header template.
*   Define files or directories to exclude from the check.
*   Set the license compatibility rules.
*   Configure logging level.

Example `.licenserc.yaml`:

```yaml
header:
  license:
    spdx-id: Apache-2.0
  paths-ignore:
    - '**/*.md'
    - '**/*.json'
```

## Contribution

We welcome contributions to Skywalking-Eyes! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute.

## License

Skywalking-Eyes is licensed under the [Apache License 2.0](LICENSE).

## Resources

*   **GitHub Repository:** [https://github.com/apache/skywalking-eyes](https://github.com/apache/skywalking-eyes)
*   **Apache SkyWalking Website:** [https://skywalking.apache.org/](https://skywalking.apache.org/)

**Note:** This README is generated based on the files in the repository as of the specified commit and timestamp.  The files and features may have been updated since then.