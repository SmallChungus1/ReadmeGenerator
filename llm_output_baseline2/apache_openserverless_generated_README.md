---
File: vscode
Size: 108 bytes
Lines: 4
---
# vscode setup
# see https://github.com/apache/openserverless-vscode-extension
# for the extension

---
File: olaris
Size: 108 bytes
Lines: 4
---
# olaris task runtime
# see https://github.com/apache/openserverless-task
# for the task runtime

---
File: olaris-op
Size: 108 bytes
Lines: 4
---
# olaris operator
# see https://github.com/apache/openserverless-operator
# for the operator

---
File: runtimes
Size: 108 bytes
Lines: 4
---
# runtimes for openserverless
# see https://github.com/apache/openserverless-runtimes
# for the runtimes

---
File: site
Size: 108 bytes
Lines: 4
---
# openserverless site
# see https://github.com/apache/openserverless-site
# for the site

---
File: testing
Size: 108 bytes
Lines: 4
---
# testing suite
# see https://github.com/apache/openserverless-testing
# for the testing suite

---
File: task
Size: 108 bytes
Lines: 4
---
# task runtime
# see https://github.com/apache/openserverless-task
# for the task runtime

---
File: vscode
Size: 108 bytes
Lines: 4
---
# vscode setup
# see https://github.com/apache/openserverless-vscode-extension
# for the extension

---
File: runtimes
Size: 108 bytes
Lines: 4
---
# runtimes for openserverless
# see https://github.com/apache/openserverless-runtimes
# for the runtimes

---
File: testing
Size: 108 bytes
Lines: 4
---
# testing suite
# see https://github.com/apache/openserverless-testing
# for the testing suite

---

Note: The structure shows redundant entries for some files (e.g., `vscode`, `task`, `runtimes`, `testing`, `site`, `olaris`, `olaris-op`). This may be due to duplication in the repository structure or a data processing error.

# Apache OpenServerless (Incubating)

Apache OpenServerless is an open-source project under incubation at the Apache Software Foundation (ASF), designed to provide a modern, cloud-native, serverless computing platform built on Kubernetes. It aims to simplify the development, deployment, and management of serverless applications by offering a unified runtime, operator, CLI, and developer experience.

## Description

Apache OpenServerless is a project focused on enabling developers to build, deploy, and manage serverless applications using Kubernetes. The project provides a comprehensive stack including:

- A task runtime for executing serverless functions
- An operator to manage the lifecycle of serverless workloads
- A CLI tool for developers to interact with the platform
- A developer experience focused on ease of use, automation, and integration with modern tooling

The project is currently in incubation, meaning it is undergoing active development and review by the ASF to ensure its infrastructure, community, and decision-making processes are mature and sustainable.

## Features

### Developer Experience
- **Custom Bash Aliases**: A set of useful shell aliases to streamline common Kubernetes and Git operations (`k`, `kg`, `kaf`, `kde`, `kns`, etc.).
- **Secret Management**: Integration with 1Password to securely manage environment variables and secrets.
- **Automated Setup**: Pre-configured scripts to install essential tools (K3s, Task, Go, Direnv, Nix) and set up the development environment.

### Kubernetes and Serverless Operations
- **Kubernetes CLI Integration**: Aliases and functions to interact with Kubernetes clusters efficiently.
- **Environment Switching**: Easy namespace switching with `kns` command.
- **Function Lifecycle Management**: Support for viewing, logging, and managing running tasks.

### Development Environment Automation
- **Cloud-Init Setup**: A `cloud-init.yaml` script that automates the setup of a development environment with K3s, Direnv, and the OpenServerless stack.
- **VS Code Integration**: Pre-configured workspaces for the CLI, operator, and root projects to enhance IDE experience.

### Project Structure and Modularity
- **Submodules**: The project is structured as a collection of modular submodules, each focused on a specific component:
  - `cli`: OpenServerless CLI tool
  - `operator`: Kubernetes operator for managing serverless workloads
  - `runtimes`: Task runtimes and function execution environments
  - `site`: Documentation and website
  - `testing`: Automated test suite
  - `vscode`: VS Code extension for developer integration

## Installation

### Prerequisites
- A Linux machine (Ubuntu 20.04+ recommended)
- `git`, `curl`, `kubectl`, and `task` CLI tools installed
- Access to the Apache OpenServerless repository

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/apache/openserverless.git
   cd openserverless
   ```

2. **Initialize Submodules**
   ```bash
   git submodule update --init --recursive
   ```

3. **Set Up Development Environment**
   Run the cloud-init script to install and configure tools:
   ```bash
   bash cloud-init.yaml
   ```

   This script will:
   - Install K3s (lightweight Kubernetes)
   - Set up Direnv and Nix for environment management
   - Clone the OpenServerless repository and sync submodules
   - Configure shell aliases and environment variables

4. **Source Bash Aliases**
   After setup, source the bash aliases to enable all shortcuts:
   ```bash
   source .bash_aliases
   ```

5. **Start Using the CLI and Operator**
   You can now use the OpenServerless CLI and Kubernetes commands to manage serverless functions and workloads.

## Usage

### Common CLI Commands
- `k` - Short for `kubectl`, with namespace set to `default`
- `kg` - `kubectl get` in the current namespace
- `kaf` - `kubectl apply -f`
- `kde` - `kubectl describe`
- `kns <namespace>` - Switch to a specific Kubernetes namespace
- `klo <pod-name>` - View logs from a pod
- `kex <pod-name> <command>` - Execute a command in a pod's container

### Managing Secrets
Use the `secrets` function to securely manage environment variables:
```bash
secrets
```
This will:
- Prompt for 1Password credentials
- Read secrets from `.env.dist` and generate `.env` and `.env.src` files
- Source the generated environment variables

### Development Workflow
1. **Start a Development Instance**
   ```bash
   bash cloud-init.yaml
   ```
2. **Configure Your Environment**
   ```bash
   source .bash_aliases
   ```
3. **Deploy and Monitor**
   Use `k` and `kg` commands to list and inspect resources.
4. **Develop and Test**
   Use `gsnap` to create commits with descriptive messages and push to origin.

## Additional Information

### Project Governance
- **ASF Incubation**: The project is currently under incubation at the Apache Software Foundation. This means it is in active development and review to ensure stability and community health.
- **Community Contribution**: Contributions are welcome. Follow the [ASF contribution guidelines](https://www.apache.org/foundation/voting.html) for contributing code, documentation, or infrastructure.

### License
All code in this project is distributed under the **Apache License, Version 2.0**. See the [LICENSE](LICENSE) file for details.

### Disclaimer
This project is still in incubation and may not be stable or fully featured. Use at your own risk. The ASF does not endorse any specific commercial products or services.

### Support
For questions or issues, please open an issue in the [project repository](https://github.com/apache/openserverless/issues).

---

> **Note**: The repository structure shows redundant entries for some files (e.g., `vscode`, `task`, `runtimes`, `testing`, `site`, `olaris`, `olaris-op`). This may be due to duplication in the repository structure or a data processing error. The core functionality and modular design remain consistent across these entries. This README provides a comprehensive overview of the project's purpose, features, and usage. For specific submodule details, refer to their respective repositories.