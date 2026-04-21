# Apache OpenServerless (Incubating)

## Description
Apache OpenServerless is an open-source project under incubation at the Apache Software Foundation. It aims to provide a cloud-native, serverless computing platform built on Kubernetes, enabling developers to build, deploy, and manage serverless applications with ease.

The project uses a modular architecture with submodules for core components such as the CLI, operator, runtimes, and development tools. It includes automation scripts for setting up development environments and managing dependencies.

## Features
- Modular architecture with submodules for CLI, operator, runtimes, and development tools
- Development environment setup via cloud-init and cloud-init scripts
- Pre-configured bash aliases for common Kubernetes and Git operations
- Integration with `task`, `direnv`, and `nix` for development workflows
- Automated submodule synchronization via `sync-branch.sh`
- Support for managing secrets via `op` CLI with `.env.dist` templates
- Cloud-init configuration for K3s, SSH access, and environment setup
- VS Code development workspaces for different components

## Prerequisites / Requirements
- Git
- Bash (version 4.0 or later)
- `kubectl` (for Kubernetes operations)
- `task` CLI (for task management)
- `op` CLI (for secret management, optional)
- A Linux-based system (Ubuntu is used in cloud-init)
- Internet access for downloading tools and dependencies

## Installation
### Setup Development Environment
1. Clone the repository:
   ```bash
   git clone https://github.com/apache/openserverless.git
   cd openserverless
   ```

2. Set up the development environment using cloud-init:
   ```bash
   bash cloud-init.yaml
   ```

3. Install required tools:
   ```bash
   # Install K3s
   curl -sfL https://get.k3s.io | sh -

   # Install task and go
   sudo snap install task --classic
   sudo snap install go --classic
   go install github.com/apache/skywalking-eyes/cmd/license-eye@latest

   # Install direnv and nix
   curl -sL https://nixos.org/nix/install | sh
   source .profile
   curl -sL https://direnv.net/install.sh | sudo bash
   ```

4. Source the bash aliases:
   ```bash
   source .bash_aliases
   ```

### Update Submodules
To synchronize submodule branches:
```bash
bash sync-branch.sh
```

## Usage
### Common Aliases
- `k`: `kubectl -n $KNS`
- `kg`: `kubectl -n $KNS get`
- `kaf`: `kubectl -n $KNS apply -f`
- `klo <name>`: View logs of a pod
- `kex <name> [command]`: Execute a command in a pod
- `kns <namespace>`: Switch to a namespace
- `t`: Run `task`
- `lenv`: Load environment variables from `.env`

### Managing Secrets
To generate environment variables from 1Password:
```bash
secrets
```
This script reads `.env.dist` and generates `.env` and `.env.src` files using the `op` CLI.

### Viewing Changes
To view differences in a file:
```bash
get-diff.sh <file-path>
```

## Contributing
Contributions are welcome. Please follow the Apache Software Foundation's contribution guidelines.

1. Fork the repository
2. Create a feature branch
3. Commit your changes with descriptive messages
4. Push to the branch and open a pull request

The project uses a strict pull request review process:
- At least one approving review is required
- All PRs must have required status checks passed
- Required conversation resolution is enforced

## License
Apache License 2.0

## Contact / Authors
Project maintained by the Apache OpenServerless Incubation Team.  
For questions or feedback, contact the Apache Incubator PMC or open an issue in the repository.  
Project homepage: https://openserverless.apache.org