# Apache OpenServerless (Incubating)

A serverless platform built on Kubernetes, enabling developers to build, deploy, and manage serverless applications with simplicity and scalability. OpenServerless provides a unified runtime, operator, CLI, and developer tools to streamline the serverless development lifecycle.

## Description

Apache OpenServerless is an incubating project under the Apache Software Foundation (ASF), designed to simplify serverless application development and operations in Kubernetes environments. It integrates a set of modular components—including a CLI, Kubernetes operator, runtime support, and developer tooling—into a cohesive ecosystem that enables rapid development, secure deployment, and observability.

The project is structured as a monorepo with submodules that manage independent components, such as the CLI, operator, runtimes, and developer extensions. It includes automated setup scripts, cloud-init configurations, and developer workflows to accelerate onboarding and reduce operational overhead.

## Features

- **Modular Architecture**: Decoupled components (CLI, operator, runtimes, VS Code extension) allow for independent development and deployment.
- **Developer Tooling**: Pre-configured environment setup via `cloud-init.yaml`, including k3s, direnv, task, and Go tooling.
- **Automated Setup**: Cloud-init script automates installation of core tools and configures Kubernetes access.
- **Secure Secrets Management**: `secrets` function integrates with 1Password to auto-generate environment variables from secure vaults.
- **Convenient CLI Aliases**: Custom `bash` aliases for common Kubernetes and Git operations (`k`, `kg`, `kns`, `gsnap`, etc.).
- **Integrated Development Workspaces**: VS Code workspaces for each component with custom color themes.
- **Submodule Syncing**: Automated branch synchronization across submodules to maintain consistency.
- **Observability & DevOps**: Includes SkyWalking Eyes for license compliance and monitoring.

## Installation

To set up Apache OpenServerless locally, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/apache/openserverless.git
cd openserverless
```

2. Initialize submodules:
```bash
git submodule update --init --recursive
```

3. Set up the development environment using cloud-init:
```bash
bash cloud-init.yaml
```

> **Note**: This script will install k3s, direnv, task, and Go, then clone the OpenServerless codebase and configure your environment.

4. Source the bash aliases for convenience:
```bash
source .bash_aliases
```

5. (Optional) Set up your VS Code environment:
```bash
code .
```

## Usage

### Running Kubernetes Commands
Use the provided aliases to simplify common operations:

```bash
# List pods, deployments, and services
kwa

# Get logs for a pod
klo my-pod

# Apply a configuration file
kaf deployment.yaml

# Switch to a namespace
kns dev
```

### Managing Secrets
Automatically generate environment variables from 1Password:

```bash
secrets
```

This command:
- Reads `.env.dist` to identify required secrets
- Logs into 1Password
- Fetches values using `op read`
- Generates `.env` and `.env.src` files with exported variables
- Sources the environment for use in scripts

### Synchronizing Submodules
Ensure all submodules are on the correct branch:

```bash
bash sync-branch.sh
```

This script:
- Checks the branch configuration in each submodule
- Updates to the specified branch if needed
- Ensures consistency across the monorepo

### Using the CLI
After setup, the OpenServerless CLI is available via the `ops` command:

```bash
ops -t          # Start the operator
ops -info       # Show operator info
ops config slim # Configure slim mode
ops config apihost <ip> # Set API host
ops setup cluster # Initialize the cluster
```

> **Note**: The `ops` CLI is installed via the `install-opsv.sh` script in the cloud-init configuration.