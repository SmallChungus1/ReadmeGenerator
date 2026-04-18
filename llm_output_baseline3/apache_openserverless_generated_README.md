# Apache OpenServerless (Incubating)

![Apache License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![GitHub](https://img.shields.io/badge/github-openserverless-blue.svg)
![Cloud](https://img.shields.io/badge/cloud-kubernetes-blue.svg)
![Serverless](https://img.shields.io/badge/serverless-true-green.svg)

Apache OpenServerless is an open-source, cloud-native platform designed to simplify the development, deployment, and management of serverless applications on Kubernetes. It provides a unified, developer-friendly ecosystem that integrates modern tooling, automation, and observability to accelerate serverless innovation.

> **Incubation Status**: This project is currently in incubation at the Apache Software Foundation (ASF). It is undergoing review to ensure its infrastructure, governance, and community processes meet the standards of other successful ASF projects.

---

## Description

Apache OpenServerless is a modular, extensible platform for building and managing serverless applications on Kubernetes. It combines a CLI, Kubernetes operator, runtime support, and developer tooling into a cohesive experience that enables rapid development, seamless deployment, and observability.

The project is structured as a collection of independent submodules, each focused on a specific component:
- **CLI**: Command-line interface for managing OpenServerless resources.
- **Operator**: Kubernetes operator for automating serverless workload lifecycle management.
- **Runtimes**: Support for various serverless runtimes (e.g., AWS Lambda, OpenFunction).
- **VSCode Extension**: Integrated development environment support.
- **Testing & DevTools**: Automated testing and developer workflows.

This modular architecture allows contributors to work on individual components while maintaining a shared vision for a unified serverless platform.

---

## Features

- ✅ **Modular Architecture**: Independent, composable components for flexible development.
- ✅ **Kubernetes Native**: Fully integrated with Kubernetes for deployment and orchestration.
- ✅ **Developer Tooling**: Built-in CLI, `task` automation, and `direnv` for environment management.
- ✅ **Automated Setup**: Cloud-init scripts automate environment provisioning (K3s, SSH, tools).
- ✅ **Secure Secrets Management**: Integration with 1Password via `secrets` alias.
- ✅ **VSCode & DevContainer Support**: Native integration with Visual Studio Code for development.
- ✅ **Automated Branch Syncing**: Ensures submodules stay in sync with upstream repositories.
- ✅ **Observability & Debugging**: Built-in `klo`, `kex`, and `kwa` aliases for Kubernetes debugging.

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

To use Apache OpenServerless, you will need:

- **Linux/macOS** (recommended)
- **Git** (v2.20+)
- **Node.js** (v16+ recommended)
- **Go** (v1.18+ for CLI and runtime components)
- **kubectl** (Kubernetes CLI)
- **Task** (for automated workflows)
- **1Password CLI** (for secret management)
- **Nix** (for environment configuration)
- **Docker or Kubernetes** (for runtime execution)

> Note: The project uses a modular structure with submodules. All submodules are managed via Git and are hosted separately.

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

> This will fetch all submodules including:
> - `cli`
> - `operator`
> - `runtimes`
> - `vscode`
> - `testing`
> - `task`

### Step 3: Set Up Your Environment

Run the cloud-init script to provision your local environment:

```bash
bash cloud-init.yaml
```

This script:
- Installs K3s (lightweight Kubernetes)
- Sets up `direnv`, `nix`, and `task`
- Configures your `~/.bashrc` with aliases and environment variables
- Clones the OpenServerless repository and runs `sync-branch.sh`

> ⚠️ **Note**: The script will prompt for your 1Password password during secret setup.

### Step 4: Configure VSCode (Optional)

Open the project in VSCode using one of the provided `.code-workspace` files:

```bash
code openserverless.code-workspace
```

This workspace includes:
- Custom color themes
- Go environment configuration
- Project folder structure

---

## Usage

### CLI Aliases (Available after sourcing `.bash_aliases`)

```bash
# Kubernetes commands
k            # kubectl -n $KNS
kg           # kubectl -n $KNS get
kgy          # kubectl -n $KNS get -o yaml
kaf          # kubectl -n $KNS apply -f
klo <name>   # kubectl logs for a pod
kex <name>   # exec into a pod
kns <name>   # switch to a namespace

# Git commands
ga           # git add
gst          # git status
glog         # git log --pretty=oneline
gsnap <msg>  # git commit -a -m <msg> and push

# Serverless tasks
t            # task command
tt           # task -d ..
ttt          # task -d ../..
```

### Managing Secrets with 1Password

```bash
secrets
```

This command:
1. Reads `.env.dist` file
2. Uses 1Password CLI to fetch secrets
3. Generates `.env` and `.env.src` files
4. Sources the environment variables into your shell

> Ensure you have the 1Password CLI installed: https://developer.1password.com/docs/cli/get-started/

### Viewing Code in VSCode

Use the `code` command to open the project in VSCode:

```bash
code openserverless.code-workspace
```

Or open specific components:

```bash
code openserverless-cli.code-workspace
code openserverless-operator.code-workspace
```

---

## Contributing

We welcome contributions to Apache OpenServerless! Please follow these guidelines:

- **Report Bugs**: Open an issue in the [GitHub Issues](https://github.com/apache/openserverless/issues) page.
- **Submit Feature Requests**: Create a new issue with detailed context.
- **Submit Pull Requests**: Ensure your changes follow the project's code style and are tested.
- **Follow the ASF Process**: All contributions must comply with the Apache Software Foundation's contribution guidelines.

> 🔗 See the full contributing guide in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

---

## License

Apache OpenServerless is licensed under the **Apache License, Version 2.0**.

> See the [LICENSE](LICENSE) file for details.

---

## Contact / Authors

- **Project Lead**: Apache OpenServerless Incubation Team
- **Community**: [Apache OpenServerless Community](https://openserverless.apache.org)
- **GitHub**: https://github.com/apache/openserverless
- **Website**: https://openserverless.apache.org
- **Discord**: Join the Apache OpenServerless community on Discord (link available on the website)

For questions or feedback, please open an issue or contact the project team directly via the Apache Incubator PMC.