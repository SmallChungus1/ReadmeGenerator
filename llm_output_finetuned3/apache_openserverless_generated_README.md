# Apache OpenServerless (Incubating)

## Description
Apache OpenServerless is an open-source project under incubation at the Apache Software Foundation (ASF). It aims to provide a serverless computing platform for Kubernetes, enabling developers to build, deploy, and manage serverless applications with minimal infrastructure overhead.

The repository serves as a central hub for the OpenServerless project, managing submodules that include the CLI, operator, runtimes, site, and development tools. It includes configuration scripts for setting up development environments, including Kubernetes clusters, task automation, and developer tooling.

## Features
- **Development Environment Setup**: Automates the setup of a local Kubernetes cluster (via k3s), installs essential tools (task, direnv, nix, Go), and configures developer workflows.
- **Submodule Management**: Uses Git submodules to manage external components such as the CLI, operator, runtimes, and VS Code extension.
- **Developer Tooling**: Includes bash aliases for common Kubernetes and Git operations, and integrates with 1Password for secure environment variable management.
- **Cloud-Init Configuration**: Provides a cloud-init script to automate the setup of Ubuntu-based instances with Kubernetes and developer tools.
- **VS Code Integration**: Offers pre-configured `.code-workspace` files for development environments in VS Code.

## Prerequisites / Requirements
- Git
- Bash (version 4.0 or later)
- A Linux-based operating system (Ubuntu is assumed)
- Access to a network with internet connectivity
- A local or remote machine capable of running a Kubernetes cluster (e.g., via k3s)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/apache/openserverless.git
   cd openserverless
   ```

2. Ensure submodules are initialized and updated:
   ```bash
   git submodule update --init --recursive
   ```

3. Optionally, update the submodule tree and sync branches:
   ```bash
   bash sync-branch.sh
   ```

4. Run the cloud-init script to set up the environment (on a target machine):
   - The script is included in `cloud-init.yaml` and can be applied via cloud-init or manually on a local machine.

## Usage
### Developer Environment Setup
After cloning the repository, the `cloud-init.yaml` script will:
- Install k3s, direnv, and task
- Configure Kubernetes access with a dynamically generated IP
- Install Go and the SkyWalking Eyes tool
- Set up the developer environment with bash aliases and environment variables

### Using Bash Aliases
The `bash_aliases` file defines common shortcuts:
- `k` and `kg` for kubectl commands in the default namespace
- `kns` to switch between namespaces
- `t` and `tt` for task command execution
- `secrets` to generate environment variables from 1Password

### Accessing Kubernetes Resources
Use the following aliases:
- `k` – kubectl in current namespace
- `kaf` – apply a Kubernetes manifest
- `klo` – get logs from a pod
- `kex` – execute a command in a pod
- `kwa`, `kwp`, `kws`, `kwc` – watch various Kubernetes resources

### Managing Environment Variables
Use the `secrets` function to:
- Read secrets from 1Password
- Generate `.env` and `.env.src` files
- Source environment variables into the shell

## Contributing
Contributions are welcome. Please follow the Apache Software Foundation's contribution guidelines.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes with clear messages.
4. Submit a pull request with a description of your changes.

All pull requests must pass the required status checks and have at least one approving review.

## License
Apache License 2.0

## Contact / Authors
This project is maintained by the Apache Incubator PMC. For questions or feedback, contact the Apache OpenServerless community via the project's official website or issue tracker.

Project website: https://openserverless.apache.org  
GitHub repository: https://github.com/apache/openserverless