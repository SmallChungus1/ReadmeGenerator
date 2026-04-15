```markdown
# Apache SkyWalking Eyes - License Management Tool

## Description

Apache SkyWalking Eyes is a command-line tool designed to manage licenses in your projects. It performs two core functions:

1. **Header Check:**  Verifies that source code files have the correct license headers.  This helps ensure proper attribution and legal compliance.
2. **Dependency Resolution:**  Scans your project's dependencies (e.g., Maven, npm, Go modules) and identifies the licenses associated with those dependencies.  It can generate reports and potentially flag incompatible licenses.

This repository contains the source code for the SkyWalking Eyes tool.

## Features

*   **License Header Verification:** Checks that files contain properly formatted license headers.
*   **License Header Fixing:** Automatically fixes missing or incorrect license headers.
*   **Dependency License Resolution:** Identifies the licenses used by your project's dependencies.
*   **Dependency License Reporting:** Generates reports on the identified dependency licenses.
*   **Configurable:**  Uses a YAML configuration file (`.licenserc.yaml`) to define project-specific settings, including license templates, excluded paths, and more.
*   **Multi-Language Support:** Supports a wide range of programming languages (see supported languages in the `.licenserc.yaml` file).
*   **GitHub Action Integration:**  Includes a GitHub action for automated license checks as part of CI/CD pipelines.
*   **Comprehensive License Database:** Contains a large database of known licenses to accurately identify licensing information.
*   **Template Support:** Allows using custom templates for generating license reports and summaries.

## Installation

**Prerequisites:**

*   Go 1.25 or later

**Installation Steps:**

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/apache/skywalking-eyes.git
    cd skywalking-eyes
    ```

2.  **Build the Binary:**
    ```bash
    make
    ```
    This will create an executable file named `license-eye` in the current directory.

3.  **Add to your PATH (optional):**
    You can move the `license-eye` executable to a directory included in your system's `PATH` environment variable to make it globally accessible.

4.  **Using Docker:** 
    You can use the predefined Docker image for easy execution, which avoids needing to install go and other tools:
    ```bash
    docker run --rm -v $(pwd):/github/workspace <image_name>
    ```
    Replace `<image_name>` by `docker.io/apache/skywalking-eyes:latest` (or a specific tag).

## Usage

**Basic Usage:**

```bash
license-eye header check
```
This will check for license headers in the current directory and its subdirectories based on the configuration in the `.licenserc.yaml` file.

**Common Commands:**

*   `license-eye header check`: Checks license headers.
*   `license-eye header fix`: Automatically fixes license headers.
*   `license-eye dependency resolve`: Resolves and reports on project dependencies and their licenses.
*   `license-eye dependency resolve -s <template_path>`: Resolves and reports on project dependencies and their licenses, with custom summary template.
*   `license-eye --help`: Displays help information.

**Configuration File (`.licenserc.yaml`):**

The tool is configured using a `.licenserc.yaml` file in the root of your project.  This file allows you to:

*   Define the license header template.
*   Specify paths to include or exclude from the check.
*   Define languages and file extensions to process.
*   Customize dependency resolution behavior.

A sample `.licenserc.yaml` file is provided in the repository.

## GitHub Action

The `.github/workflows/license-eye-check.yaml` file provides a GitHub Action that automatically runs the license header check on every pull request. This helps ensure that all contributions adhere to the project's licensing standards.  To use it, simply add this file to your repository.

## Summary Report

The tool generates a summary report of its findings and can output it to the console or to a file. A sample report, generated during the build process, includes the following information:

*   Total files scanned: 847
*   Files included: 839
*   Files skipped by rule: 7
*   Files skipped by size: 1
*   Detected languages count: 23
*   Top 15 largest included files: (list of files and their sizes)

## Known Issues and Limitations

*  Dependency resolution isn't compatible with all build tools or package managers.
*  The accuracy of the dependency license detection relies on the availability of accurate metadata for each dependency.

## Contributing

Contributions are welcome! Please follow the [Apache Contributor Guidelines](https://www.apache.org/dev/contributing.html) when submitting pull requests.

## License

This project is licensed under the [Apache License 2.0](LICENSE).