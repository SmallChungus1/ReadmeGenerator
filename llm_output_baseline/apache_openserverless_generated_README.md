# Apache OpenServerless (Incubating)

## Description

Apache OpenServerless is an open-source project focused on enabling serverless computing in Kubernetes environments. It provides a unified, portable, and developer-friendly platform for building, deploying, and managing serverless applications. The project is currently in incubation at the Apache Software Foundation (ASF), indicating that it is under active development and undergoing review to ensure stability, governance, and community engagement.

OpenServerless leverages modular components such as a CLI, Kubernetes operator, runtimes, and developer tooling to offer a complete serverless development experience. It supports seamless integration with modern development workflows, including containerized runtimes, observability, and automated CI/CD pipelines.

## Features

- **Modular Architecture**: Built with independent, reusable components (CLI, operator, runtimes, VS Code extension).
- **Developer Tooling**: Includes `bash_aliases`, `direnv`, and `task` integration for streamlined development workflows.
- **Cloud-Ready Setup**: Cloud-init configuration automates setup of Kubernetes (k3s), SSH access, and developer tools on Ubuntu.
- **Integrated CLI and Operator**: Provides a command-line interface (`ops`) and Kubernetes operator for managing serverless workloads.
- **Automated Submodule Syncing**: Scripts like `sync-branch.sh` ensure all submodules are updated to the correct branches.
- **Secure Environment Management**: Uses `op` CLI to manage secrets via 1Password, with automated `.env` file generation.
- **VS Code Integration**: Pre-configured `.code-workspace` files for consistent development environments.
- **Automated Development Workflow**: Includes scripts for syncing code, setting up environments, and managing Kubernetes contexts.

## Installation

To set up the Apache OpenServerless development environment, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/apache/openserverless.git
   cd openserverless
   ```

2. **Set up the development environment using cloud-init**:
   The `cloud-init.yaml` file automates the setup of a development machine with k3s, direnv, task, and Go. This can be used with a cloud instance or local VM.

   ```bash
   # Apply cloud-init configuration (run on target machine)
   sudo cloud-init apply
   ```

3. **Install required tools**:
   ```bash
   # Install k3s, direnv, and task
   curl -sfL https://get.k3s.io | sh -
   curl -sL https://direnv.net/install.sh | sudo bash
   sudo snap install task --classic
   sudo snap install go --classic
   ```

4. **Set up the local development environment**:
   ```bash
   # Source the bash aliases for convenience
   source .bash_aliases

   # Initialize the project with submodules
   git submodule update --recursive --remote
   bash sync-branch.sh
   ```

5. **Configure your shell**:
   ```bash
   # Add to ~/.bashrc to enable aliases and environment variables
   echo 'source $HOME/.z.sh' >> ~/.bashrc
   echo 'source $HOME/.bash_aliases' >> ~/.bashrc
   source ~/.bashrc
   ```

## Usage

### Using the CLI and Kubernetes Operator

After setting up the environment, you can use the `ops` CLI to manage OpenServerless resources:

```bash
# List available operations
ops -info

# Configure the operator with a custom API host
ops config apihost <your-ip>.nip.io

# Setup a new cluster
ops setup cluster

# View running pods
klo my-pod-name
```

### Managing Kubernetes Resources

Use the `k` aliases to interact with Kubernetes resources:

```bash
# List all resources in the current namespace
kwa

# Get logs from a pod
klo my-pod

# Switch to a different namespace
kns development

# Apply a manifest file
kaf deployment.yaml
```

### Managing Secrets with 1Password

To securely manage environment variables:

```bash
# Generate environment variables from 1Password secrets
secrets
```

This command will:
- Read the `.env.dist` file
- Use the `op` CLI to fetch secrets from 1Password
- Generate a `.env` file with the actual values
- Create a `.env.src` file with export commands

### Working with Submodules

To ensure all submodules are up to date:

```bash
# Sync all submodules to their configured branches
bash sync-branch.sh

# Update the entire tree (pull + submodule update)
bash update-tree.sh
```

> **Note**: All submodules are managed via Git and are linked to specific repositories (e.g., `openserverless-cli`, `openserverless-operator`, `openserverless-runtimes`).

### VS Code Development Setup

Open the project in VS Code using the provided `.code-workspace` files:

```bash
# Open in VS Code
code .
```

The workspace files provide:
- Custom color themes for different components
- Pre-configured paths and settings
- Developer-friendly environments for CLI, operator, and site modules