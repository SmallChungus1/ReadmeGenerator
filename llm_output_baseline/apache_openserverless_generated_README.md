# Apache OpenServerless (Incubating)

![Apache License 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=flat&logo=github)
![Apache Software Foundation](https://img.shields.io/badge/organization-Apache%20Software%20Foundation-blue)

> A cloud-native, serverless platform built on Kubernetes to simplify the development, deployment, and management of serverless applications. OpenServerless provides a unified, open-source ecosystem for building and running functions across multiple runtimes, with tools for development, testing, and operations.

---

## Description

Apache OpenServerless is an incubating project under the Apache Software Foundation (ASF), designed to empower developers to build, deploy, and manage serverless applications using Kubernetes as the underlying infrastructure. The project provides a comprehensive toolchain that includes:

- A **developer-first CLI** for managing serverless functions and resources
- An **OpenServerless Operator** for declarative Kubernetes resource management
- A **modular runtime ecosystem** supporting multiple serverless runtimes
- Integrated development environments (IDEs) and local development workflows
- Automated setup and configuration via cloud-init and shell scripts

OpenServerless is ideal for developers and teams looking to adopt a modern, scalable, and portable approach to serverless computing—without vendor lock-in or complex infrastructure management.

---

## Features

- ✅ **Modular Architecture**: Decouples core functionality into reusable components (CLI, Operator, Runtimes, DevTools)
- ✅ **Developer-First Tooling**: Includes `task`, `ops`, `direnv`, and `k3s` for seamless local development
- ✅ **Kubernetes-First**: Fully compatible with Kubernetes clusters, enabling scalable, portable deployments
- ✅ **Integrated Security**: Uses `op` CLI to manage secrets via 1Password, with automated environment generation
- ✅ **Automated Setup**: Cloud-init scripts provision a full development environment with k3s, task, and Go tooling
- ✅ **Multi-Repository Structure**: Uses Git submodules to manage independent, versioned components
- ✅ **VS Code Integration**: Pre-configured workspaces for CLI, Operator, and core project development
- ✅ **Open-Source & Apache-Licensed**: Fully transparent, community-driven, and compliant with open standards

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

Before using Apache OpenServerless, ensure the following are installed:

- **Linux** (Ubuntu 20.04+ recommended)
- **Git** (v2.30+)
- **Node.js** (v16+ or v18+)
- **Go** (v1.19+)
- **kubectl** (Kubernetes CLI)
- **task** (serverless task runner)
- **1Password CLI** (for secret management)
- **VS Code** (recommended IDE)

> Note: The project uses a modular structure with submodules. All components are managed via Git submodules and require proper initialization.

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/apache/openserverless.git
cd openserverless
```

### Step 2: Initialize Submodules

```bash
git submodule update --init --recursive
```

> This will fetch all dependent repositories:
> - `cli` – OpenServerless CLI
> - `operator` – OpenServerless Operator
> - `runtimes` – Serverless runtime components
> - `vscode` – VS Code extension
> - `task` – Task runner for local execution
> - `testing` – Integration and CI/CD tools

### Step 3: Set Up Development Environment (via Cloud-Init)

The `cloud-init.yaml` script automates the setup of a local development environment. Run it manually or via cloud-init:

```bash
sudo cloud-init --config cloud-init.yaml
```

> This will:
> - Install k3s, direnv, and task
> - Configure Kubernetes access with dynamic IP binding
> - Set up environment variables and shell aliases
> - Clone the OpenServerless repository and run `sync-branch.sh`

### Step 4: Source Bash Aliases

Add the following to your shell profile (`~/.bashrc`):

```bash
source ~/.bash_aliases
```

> This enables convenient CLI shortcuts like:
> - `k` → `kubectl -n $KNS`
> - `t` → `task`
> - `kns <namespace>` → switch to a namespace
> - `klo <pod>` → view logs of a pod

---

## Usage

### Example: Managing Kubernetes Resources

```bash
# List all resources in current namespace
kwa

# View a resource in YAML format
kgy deployment/my-app

# Apply a manifest file
kaf ./manifests/deployment.yaml

# Describe a resource
kde pod/my-pod

# Delete a resource
kdel deployment/my-app
```

### Example: Using Task Runner

```bash
# List tasks in current directory
tt

# Run a task in parent directory
ttt

# Set a task with a description
task add "Deploy function" -d "deploy-function"
```

### Example: Managing Secrets with 1Password

```bash
# Generate environment variables from 1Password
secrets
```

> This reads `.env.dist` and populates `.env` and `.env.src` with values from 1Password, then sources them into the shell.

---

## Contributing

We welcome contributions from the community! Please follow these guidelines:

- **Report bugs** via GitHub Issues
- **Submit feature requests** in the Issues section
- **Contribute code** by forking the repository and submitting a pull request
- **Follow the Apache License 2.0** for all contributions

> All contributions are reviewed by the Apache Incubator PMC. See the [ASF Contributor Guide](https://www.apache.org/foundation/contributor/).

For detailed contribution workflows, refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file (to be created).

---

## License

Apache OpenServerless is licensed under the **Apache License, Version 2.0**.

> See the [LICENSE](LICENSE) file for full terms.

---

## Contact / Authors

- **Project Maintainers**: Apache Incubator PMC
- **Project Home**: https://openserverless.apache.org
- **GitHub Repository**: https://github.com/apache/openserverless
- **Community Forum**: Apache Incubator Community
- **Support**: Open issues or reach out via the ASF mailing lists

> For questions or feedback, please open an issue or contact the project maintainers directly.

> ⚠️ This project is in incubation. While actively developed, it is not yet fully endorsed by the Apache Software Foundation. Use at your own risk.