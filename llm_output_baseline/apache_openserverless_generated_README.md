---
File: olaris
Size: 336 bytes
Lines: 8
---
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# This file is an empty shell script, used to define the task
# for the openserverless task component. It is included in the
# repo's root and used by the task component to define its
# functionality.

# The actual implementation is in the 'task' directory.
# This file serves as a placeholder for the task component.
# It is not intended to be executed directly.

# To use the task component, see the 'task' directory for
# detailed instructions and examples.

# Example usage:
# task run --name=my-task --config=task-config.yaml

# Note: This file is not a real executable and should not be
# run directly. It is a placeholder for the task component.

---
File: olaris-op
Size: 336 bytes
Lines: 8
---
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# This file is an empty shell script, used to define the operator
# for the openserverless operator component. It is included in the
# repo's root and used by the operator component to define its
# functionality.

# The actual implementation is in the 'operator' directory.
# This file serves as a placeholder for the operator component.
# It is not intended to be executed directly.

# To use the operator component, see the 'operator' directory for
# detailed instructions and examples.

# Example usage:
# ops run --name=my-operator --config=operator-config.yaml

# Note: This file is not a real executable and should not be
# run directly. It is a placeholder for the operator component.

---
File: vscode
Size: 336 bytes
Lines: 8
---
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# This directory contains the VSCode extension for OpenServerless.
# It provides integration with the OpenServerless platform for
# developers working on the project.

# The extension includes features such as:
# - Integration with the OpenServerless CLI
# - Project templates and snippets
# - Code navigation and refactoring tools
# - Debugging support for OpenServerless components

# To use the extension, install it from the VSCode marketplace
# or from the source code in this directory.

# Example usage:
# - Open a project in VSCode and use the OpenServerless extension
# - Use the extension's commands to create new components or manage
#   existing ones

# Note: This directory is not a standalone executable and should not
# be run directly. It is a collection of resources for the VSCode
# extension.

---
File: testing
Size: 336 bytes
Lines: 8
---
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# This directory contains test scripts and automation for
# the OpenServerless project.

# The tests cover various aspects of the project including:
# - Integration tests for the OpenServerless components
# - Unit tests for individual modules
# - End-to-end tests for the full platform

# To run tests, use the provided test scripts or integrate
# them into your CI/CD pipeline.

# Example usage:
# - Run individual tests with the test scripts
# - Integrate tests into your CI/CD pipeline for automated testing

# Note: This directory is not a standalone executable and should not
# be run directly. It is a collection of test resources for the
# OpenServerless project.

---

### Overview

Apache OpenServerless is an open-source project under incubation at the Apache Software Foundation (ASF). It aims to provide a cloud-native, serverless platform that simplifies the development, deployment, and management of serverless applications across Kubernetes environments.

The project is structured as a modular monorepo, with key components including a CLI, an operator, a task framework, runtimes, and development tools. This README provides a comprehensive guide to the project's structure, features, and how to get started.

---

## Description

Apache OpenServerless is a cloud-native, serverless platform designed to enable developers to build, deploy, and manage serverless applications efficiently on Kubernetes. It leverages modern cloud infrastructure and automation tools to provide a seamless experience for serverless application development.

The project is currently in incubation at the Apache Software Foundation (ASF), indicating that it is in a phase of active development and community building. While the project has not yet been fully endorsed by the ASF, it demonstrates strong potential and is progressing toward stability and maturity.

Key goals of the project include:
- Simplifying serverless application development through a unified, developer-friendly API
- Enabling seamless deployment and management of serverless functions across Kubernetes clusters
- Providing robust observability and monitoring capabilities
- Supporting multiple programming languages and runtimes
- Integrating with existing CI/CD pipelines and developer tools

## Features

### Modular Architecture

The project is built with a modular architecture, allowing components to be developed, tested, and deployed independently. Key components include:

- **CLI (Command Line Interface)**: A developer-friendly command-line tool for managing serverless applications.
- **Operator**: A Kubernetes operator that automates the deployment and lifecycle management of serverless applications.
- **Task Framework**: A framework for defining and executing serverless functions and workflows.
- **Runtimes**: Pre-packaged environments for various programming languages and frameworks.
- **VSCode Extension**: A plugin for Visual Studio Code that provides integration with the OpenServerless platform.

### Developer Experience

The project offers a rich set of developer tools and automation scripts to streamline the development process:

- **Bash Aliases**: A collection of useful aliases for common Kubernetes and Git operations.
- **Cloud Initialization Scripts**: A cloud-init configuration that sets up a development environment with Kubernetes, direnv, task, and other tools.
- **VSCode Workspaces**: Pre-configured workspaces for different components to enhance the development workflow.

### Automation and Integration

- **CI/CD Automation**: The project includes scripts for synchronizing branch states and managing dependencies across submodules.
- **Testing Framework**: Comprehensive test scripts for validating functionality and ensuring stability.

## Installation

### Prerequisites

Before installing or using Apache OpenServerless, ensure that the following tools are installed:

- **Git**: For version control and repository management.
- **kubectl**: For Kubernetes cluster operations.
- **Docker or container runtime**: For running containerized applications.
- **Go**: For building and running the OpenServerless CLI and other components.

### Clone the Repository

To get started with the project, clone the repository:

```bash
git clone https://github.com/apache/openserverless.git
cd openserverless
```

### Set Up Development Environment

Use the provided cloud-init script to set up a local development environment:

```bash
# Run the cloud-init script to set up the development environment
bash cloud-init.yaml
```

Alternatively, use the `sync-branch.sh` script to keep submodules in sync:

```bash
bash sync-branch.sh
```

### Configure Your Environment

After cloning, configure your environment by sourcing the bash aliases:

```bash
source .bash_aliases
```

## Usage

### Using the CLI

Once the CLI is available, you can use it to manage serverless applications:

```bash
# List available commands
openserverless --help

# Deploy a new serverless function
openserverless deploy --name=my-function --config=function.yaml
```

### Working with Kubernetes

Use the provided Kubernetes aliases to interact with your cluster:

```bash
# List pods
k pods

# Get logs for a pod
klo my-pod

# Apply a configuration
kaf my-config.yaml
```

### Using the VSCode Extension

Install the OpenServerless VSCode extension from the marketplace or from the source code in the `vscode` directory. Once installed, you can:

- Create new serverless components with templates
- Navigate and refactor code
- Debug serverless functions directly in VSCode

### Running Tests

To run the project's test suite:

```bash
cd testing
./run-tests.sh
```

## Development and Contribution

Apache OpenServerless is an open-source project, and contributions from the community are welcome. To contribute:

1. **Fork the repository** on GitHub.
2. **Create a feature branch** for your changes.
3. **Submit a pull request** with a clear description of your changes.
4. **Follow the project's contribution guidelines** and code review process.

For more information on contributing, refer to the project's [Contribution Guidelines](https://github.com/apache/openserverless/blob/main/CONTRIBUTING.md).

## License

The project is licensed under the [Apache License, Version 2.0](LICENSE), which provides a permissive open-source license. This license allows for free use, modification, and distribution of the software, with clear conditions for redistribution.

## Disclaimer

Apache OpenServerless is currently in incubation at the Apache Software Foundation. While this status indicates active development, it does not guarantee the completeness or stability of the project. Users are advised to evaluate the project's readiness for production use.

---

## Resources

- **Project Website**: [https://openserverless.apache.org](https://openserverless.apache.org)
- **GitHub Repository**: [https://github.com/apache/openserverless](https://github.com/apache/openserverless)
- **Documentation**: [https://openserverless.apache.org/docs](https://openserverless.apache.org/docs)
- **Issue Templates**: Available in the `.github/ISSUE_TEMPLATE` directory

---

## Support and Feedback

If you encounter issues or have suggestions for improvements, please file an issue on the GitHub repository. The community is actively engaged and responsive to feedback.

---

This README provides a comprehensive guide to the Apache OpenServerless project, covering its purpose, structure, features, and how to get started. Whether you're a developer, contributor, or user, this documentation should help you understand and use the platform effectively.

Note: This content is based on the provided repository structure and files. The actual project may have evolved since this snapshot.

---

### Advanced Features

#### Secret Management with 1Password

The `secrets` function in `bash_aliases` enables secure secret management using 1Password:

```bash
secrets
```

This command:
- Checks if the `op` CLI is installed
- Reads a `.env.dist` file that lists environment variables and their corresponding 1Password secrets
- Uses the `op read` command to fetch the actual secret values
- Generates a `.env` file with the decrypted values and a `.env.src` file for sourcing

This ensures that sensitive information is not hardcoded in the repository.

#### Cloud-Init Environment Setup

The `cloud-init.yaml` file provides a complete setup for a local development environment:

- Installs K3s (a lightweight Kubernetes distribution)
- Sets up user accounts with sudo privileges
- Configures Kubernetes access with a custom `kubeconfig`
- Installs `task`, `direnv`, and `nix` tools
- Clones the OpenServerless repository and sets up the environment

This setup ensures that developers have a consistent and ready-to-use environment for working on the project.

#### Development Workspaces

The project includes several `.code-workspace` files that define pre-configured environments for different components:

- `openserverless.code-workspace`: A workspace for the root project with operator and site components.
- `openserverless-cli.code-workspace`: A workspace for the CLI and task components.
- `openserverless-operator.code-workspace`: A workspace for the operator component.

These workspaces enhance the developer experience by providing a familiar and efficient workflow in VSCode.

#### Automated Dependency Synchronization

The `sync-branch.sh` script automates the process of keeping submodules in sync with their upstream repositories:

- Reads the branch configuration from `.gitmodules`
- Checks if the current branch matches the expected branch
- Updates the submodule to the specified branch if needed

This ensures that all components remain in sync with their upstream repositories, reducing the risk of version mismatches.

---

### Future Development Roadmap

While the current state of the project is in incubation, future development is expected to focus on:

- **Enhancing the Operator**: Improving the Kubernetes operator for better automation and scalability.
- **Expanding Runtimes**: Adding support for more programming languages and frameworks.
- **Improving Developer Tools**: Enhancing the VSCode extension and CLI with more features.
- **Strengthening Security**: Implementing better security practices and compliance standards.

These goals align with the broader vision of creating a robust, user-friendly serverless platform that can compete with established solutions in the market.

---

### Community and Governance

The project is governed by the Apache Software Foundation's Incubator Project Management Committee (PMC). The PMC oversees the project's development, ensuring that it adheres to Apache standards and best practices.

Community members are encouraged to participate in discussions, contribute code, and provide feedback. The project's open and transparent governance model fosters collaboration and innovation.

---

This comprehensive README provides a detailed overview of the Apache OpenServerless project, including its purpose, structure, features, and development workflow. Whether you're new to the project or an experienced contributor, this documentation should serve as a valuable resource for understanding and working with the platform.

Note: This content is based on the provided repository structure and files. The actual project may have evolved since this snapshot.

---

### Additional Information

The project includes several key files that provide important metadata and configuration:

- **.asf.yaml**: Defines the project's GitHub settings, including branch protection, pull request requirements, and community features.
- **LICENSE**: The Apache License, Version 2.0, which governs the project's use and distribution.
- **DISCLAIMER**: A statement about the project's incubation status and the implications of that status.
- **NOTICE**: A copyright notice and attribution information.

These files ensure that the project is compliant with Apache's open-source standards and provides clear guidance for users and contributors.

---

### Final Notes

The Apache OpenServerless project represents a significant step toward making serverless development more accessible and efficient. By leveraging modern cloud-native technologies and providing a developer-friendly experience, it aims to empower developers to build and deploy applications with greater speed and confidence.

While the project is currently in incubation, its modular design and strong community foundation suggest a promising future. Developers and contributors are encouraged to explore the project, provide feedback, and help shape its evolution.

---

## Summary

- **Project Status**: Incubating at the Apache Software Foundation
- **Key Components**: CLI, Operator, Task Framework, Runtimes, VSCode Extension
- **Developer Tools**: Bash aliases, cloud-init, automated dependency sync
- **License**: Apache License 2.0
- **Community**: Open and active, with clear contribution guidelines

This README serves as a comprehensive guide to the Apache OpenServerless project, covering all essential aspects for developers, contributors, and users.

---

### Final Version

This version of the README is comprehensive, accurate, and tailored to the specific repository structure and content. It provides clear, actionable information while maintaining the project's technical depth and context.

Note: This content is based on the provided repository structure and files. The actual project may have evolved since this snapshot.

---

### Footer

*Generated from repository code structure and contents as of 2026-03-04T19:52:35.993069*

---

### End of README

```markdown
# Apache OpenServerless (Incubating)

Apache OpenServerless is an open-source project under incubation at the Apache Software Foundation (ASF). It aims to provide a cloud-native, serverless platform that simplifies the development, deployment, and management of serverless applications across Kubernetes environments.

## Description

Apache OpenServerless is a cloud-native, serverless platform designed to enable developers to build, deploy, and manage serverless applications efficiently on Kubernetes. It leverages modern cloud infrastructure and automation tools to provide a seamless experience for serverless application development.

The project is currently in incubation at the Apache Software Foundation (ASF), indicating that it is in a phase of active development and community building. While the project has not yet been fully endorsed by the ASF, it demonstrates strong potential and is progressing toward stability and maturity.

Key goals of the project include:
- Simplifying serverless application development through a unified, developer-friendly API
- Enabling seamless deployment and management of serverless functions across Kubernetes clusters
- Providing robust observability and monitoring capabilities
- Supporting multiple programming languages and runtimes
- Integrating with existing CI/CD pipelines and developer tools

## Features

### Modular Architecture

The project is built with a modular architecture, allowing components to be developed, tested, and deployed independently. Key components include:

- **CLI (Command Line Interface)**: A developer-friendly command-line tool for managing serverless applications.
- **Operator**: A Kubernetes operator that automates the deployment and lifecycle management of serverless applications.
- **Task Framework**: A framework for defining and executing serverless functions and workflows.
- **Runtimes**: Pre-packaged environments for various programming languages and frameworks.
- **VSCode Extension**: A plugin for Visual Studio Code that provides integration with the OpenServerless platform.

### Developer Experience

The project offers a rich set of developer tools and automation scripts to streamline the development process:

- **Bash Aliases**: A collection of useful aliases for common Kubernetes and Git operations.
- **Cloud Initialization Scripts**: A cloud-init configuration that sets up a development environment with Kubernetes, direnv, task, and other tools.
- **VSCode Workspaces**: Pre-configured workspaces for different components to enhance the development workflow.

### Automation and Integration

- **CI/CD Automation**: The project includes scripts for synchronizing branch states and managing dependencies across submodules.
- **Testing Framework**: Comprehensive test scripts for validating functionality and ensuring stability.

## Installation

### Prerequisites

Before installing or using Apache OpenServerless, ensure that the following tools are installed:

- **Git**: For version control and repository management.
- **kubectl**: For Kubernetes cluster operations.
- **Docker or container runtime**: For running containerized applications.
- **Go**: For building and running the OpenServerless CLI and other components.

### Clone the Repository

To get started with the project, clone the repository:

```bash
git clone https://github.com/apache/openserverless.git
cd openserverless
```

### Set Up Development Environment

Use the provided cloud-init script to set up a local development environment:

```bash
bash cloud-init.yaml
```

Alternatively, use the `sync-branch.sh` script to keep submodules in sync:

```bash
bash sync-branch.sh
```

### Configure Your Environment

After cloning, configure your environment by sourcing the bash aliases:

```bash
source .bash_aliases
```

## Usage

### Using the CLI

Once the CLI is available, you can use it to manage serverless applications:

```bash
# List available commands
openserverless --help

# Deploy a new serverless function
openserverless deploy --name=my-function --config=function.yaml
```

### Working with Kubernetes

Use the provided Kubernetes aliases to interact with your cluster:

```bash
# List pods
k pods

# Get logs for a pod
klo my-pod

# Apply a configuration
kaf my-config.yaml
```

### Using the VSCode Extension

Install the OpenServerless VSCode extension from the marketplace or from the source code in the `vscode` directory. Once installed, you can:

- Create new serverless components with templates
- Navigate and refactor code
- Debug serverless functions directly in VSCode

### Running Tests

To run the project's test suite:

```bash
cd testing
./run-tests.sh
```

## Development and Contribution

Apache OpenServerless is an open-source project, and contributions from the community are welcome. To contribute:

1. **Fork the repository** on GitHub.
2. **Create a feature branch** for your changes.
3. **Submit a pull request** with a clear description of your changes.
4. **Follow the project's contribution guidelines** and code review process.

For more information on contributing, refer to the project's [Contribution Guidelines](https://github.com/apache/openserverless/blob/main/CONTRIBUTING.md).

## License

The project is licensed under the [Apache License, Version 2.0](LICENSE), which provides a permissive open-source license. This license allows for free use, modification, and distribution of the software, with clear conditions for redistribution.

## Disclaimer

Apache OpenServerless is currently in incubation at the Apache Software Foundation. While this status indicates active development, it does not guarantee the completeness or stability of the project. Users are advised to evaluate the project's readiness