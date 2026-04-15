# Apache OpenServerless (Incubating)

![Apache License 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=for-the-badge)
![GitHub](https://img.shields.io/github/stars/apache/openserverless?style=for-the-badge&label=Stars)
![GitHub Issues](https://img.shields.io/github/issues/apache/openserverless?style=for-the-badge)
![GitHub](https://img.shields.io/github/last-commit/apache/openserverless?style=for-the-badge)

> **Apache OpenServerless** is an open-source, cloud-native platform for building and deploying serverless applications on Kubernetes. It provides a unified, developer-friendly experience across multiple runtimes, operators, and tooling — all governed by the Apache Software Foundation (ASF).

---

## Description

Apache OpenServerless is a **serverless computing platform** designed to simplify the development, deployment, and management of cloud-native applications using Kubernetes. It enables developers to build, test, and scale serverless functions with minimal infrastructure overhead.

This project is currently in **incubation** at the Apache Software Foundation. It is under active development with a focus on:

- A unified CLI for managing serverless functions
- A Kubernetes operator for automated deployment and lifecycle management
- Support for multiple runtimes (e.g., Node.js, Python, Java)
- Developer tooling (e.g., `task`, `direnv`, `skywalking-eyes`)
- Seamless integration with modern DevOps workflows

OpenServerless is ideal for developers, DevOps engineers, and cloud architects who want to adopt a serverless-first approach without sacrificing control, observability, or security.

---

## Features

- ✅ **Unified CLI** (`ops` and `task`) for managing serverless functions and Kubernetes resources  
- ✅ **Kubernetes Operator** (`openserverless-operator`) for automated deployment and lifecycle management  
- ✅ **Multi-runtime support** (Node.js, Python, Java, Go, etc.) via modular runtimes  
- ✅ **Developer tooling** including `task`, `direnv`, `nix`, and `skywalking-eyes`  
- ✅ **Automated setup** via `cloud-init.yaml` for local development environments  
- ✅ **Git integration** with branch synchronization and environment management  
- ✅ **Secure secrets management** via 1Password integration  
- ✅ **VS Code integration** with pre-configured workspaces and color themes  

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

| Requirement | Version |
|-----------|---------|
| **Linux OS** | Ubuntu 20.04 or later |
| **Node.js** | v16+ (for CLI tools) |
| **Go** | v1.18+ (for runtime builds) |
| **kubectl** | v1.28+ |
| **1Password CLI** | Required for secret management |
| **nix** | Optional, for advanced environment configuration |
| **task** | Optional, for task automation |

> 💡 The project includes a `cloud-init.yaml` script to automate setup on Ubuntu-based systems.

---

## Installation

### Option 1: Local Development Setup (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/apache/openserverless.git
   cd openserverless
   ```

2. **Initialize submodules**:
   ```bash
   git submodule update --init --recursive
   ```

3. **Run the cloud-init setup** (automatically runs on Ubuntu VMs or local machines):
   ```bash
   bash cloud-init.yaml
   ```

4. **Sync submodules to the correct branches**:
   ```bash
   bash sync-branch.sh
   ```

5. **Initialize developer environment**:
   ```bash
   bash direnv-init.sh
   ```

6. **Source the bash aliases**:
   ```bash
   source .bash_aliases
   ```

> ✅ This setup automatically installs:
> - K3s (lightweight Kubernetes)
> - `task`, `direnv`, `nix`, and `skywalking-eyes`
> - A custom `.bashrc` with useful aliases
> - A pre-configured `~/.env` and `~/.env.src` for secrets

---

### Option 2: Using Docker or VM (Advanced)

For containerized or VM-based development, use the `cloud-init.yaml` to provision a full development environment:

```yaml
# cloud-init.yaml
# See full config in the repo
```

> This script will:
> - Install K3s
> - Configure Kubernetes access via `~/.kube/config`
> - Set up `ops` CLI and `task` for function management
> - Launch a local development cluster

---

## Usage

### Basic CLI Commands

After setup, use the following aliases:

```bash
# List Kubernetes resources
kwa           # watch pods, deployments, services
kwp           # watch pods and deployments
kws           # watch services and ingress
kwc           # watch config maps and secrets

# Namespace switching
kns           # list namespaces or switch to a specific one
kns my-ns     # switch to namespace 'my-ns'

# Function lifecycle
t             # run a task
tt            # run task in parent directory
ttt           # run task in grandparent directory

# Logs and debugging
klo my-pod    # get logs from a pod
kex my-pod    # exec into a pod
kde my-pod    # describe a pod
```

### Managing Secrets

Use the `secrets` function to securely load environment variables from 1Password:

```bash
secrets
```

This will:
- Read `.env.dist` file
- Prompt for 1Password login
- Generate `.env` and `.env.src` files
- Source the environment variables into your shell

> 🔐 All secrets are encrypted and managed via 1Password.

### Git Workflow

Use the `gsnap` alias to create a commit message from arguments:

```bash
gsnap "Fix login issue in auth flow"
```

> This creates a commit with the message and pushes it to the remote.

---

## Contributing

We welcome contributions from the community! Please follow these guidelines:

- ✅ Open issues or feature requests on [GitHub Issues](https://github.com/apache/openserverless/issues)
- ✅ Submit pull requests with clear descriptions and test coverage
- ✅ Follow the [Apache Code of Conduct](https://www.apache.org/foundation/policies/conduct)
- ✅ Use the `sync-branch.sh` script to ensure submodules are up to date
- ✅ Run `update-tree.sh` to keep the project tree synchronized

> 📝 See the full [CONTRIBUTING.md](https://github.com/apache/openserverless/blob/main/CONTRIBUTING.md) for detailed contribution guidelines.

---

## License

Apache OpenServerless is licensed under the **Apache License, Version 2.0**.

> See [LICENSE](https://github.com/apache/openserverless/blob/main/LICENSE) for full terms.

---

## Contact / Authors

**Project Maintainers**:
- Apache Incubator PMC
- OpenServerless Community Team

**Project Website**: [https://openserverless.apache.org](https://openserverless.apache.org)

**GitHub Repository**: [https://github.com/apache/openserverless](https://github.com/apache/openserverless)

**Community Channels**:
- [Apache Incubator Slack](https://apache.org/slack)
- [GitHub Discussions](https://github.com/apache/openserverless/discussions)

**Feedback & Support**:
- Open an issue on GitHub
- Reach out via email: openserverless-dev@lists.apache.org

> 🚀 This project is incubating and under active development. Feedback is highly encouraged!