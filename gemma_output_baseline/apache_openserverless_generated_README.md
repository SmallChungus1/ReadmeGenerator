# Apache OpenServerless (Incubating)

![OpenServerless Logo](assets/logos/png/openserverless-logo.png)

## Description

Apache OpenServerless is an incubating project at the Apache Software Foundation dedicated to building a truly open and portable serverless platform. It aims to provide a Kubernetes-native foundation for serverless functions and applications, focusing on standards adherence and vendor neutrality. This repository serves as the central hub for the project, incorporating tools and components for developing, deploying, and managing serverless workloads.  This project is undergoing rapid development and is currently in the incubation phase.

## Features

*   **Kubernetes-Native:** Built on Kubernetes, leveraging its scalability, portability, and management capabilities.
*   **Open Standards:** Embraces open standards and avoids vendor lock-in.
*   **Multi-Runtime Support:** Supports various programming languages and runtimes. (Refer to the `runtimes` directory)
*   **Composable Architecture:**  Designed to be modular and extensible, allowing users to customize and integrate with their existing infrastructure.
*   **Developer-Friendly CLI:**  Includes a command-line interface (`cli`) for simplified development and deployment.
*   **Operator-Based Management:** Utilizes a Kubernetes Operator (`olaris-op`) for automated lifecycle management of serverless resources.
*   **Site:** Contains project documentation and website source (`site`).
*   **Testing Framework:** Comprehensive tests for reliability and stability (`testing`).

## Installation

1.  **Prerequisites:**
    *   Kubernetes cluster (e.g., Minikube, kind, cloud provider Kubernetes service).
    *   `kubectl` configured to connect to your cluster.
    *   `git`
    *   `nix` package manager.
    *   `direnv`

2. **Clone the Repository:**

    ```bash
    git clone https://github.com/apache/openserverless.git --recurse-submodules
    cd openserverless
    ```

3.  **Initialize and setup Environment using cloud-init:**
    While not intended for general use, copy the cloud-init file to setup a test environment.

    ```bash
    cp cloud-init.yaml <appropriate_cloud_provider_configuration>
    ```

4.  **Setup the Project:**

    ```bash
    bash direnv-init.sh # This initializes the environment
    ```
    Alternatively, to setup manually:

    ```bash
    curl -sL https://nixos.org/nix/install | sh
    curl -sL https://direnv.net/install.sh | sudo bash
    source .profile
    git clone https://github.com/nix-community/nix-direnv $HOME/nix-direnv
    mkdir -p $HOME/.config/direnv
    echo 'source $HOME/nix-direnv/direnvrc' >>$HOME/.config/direnv/direnvrc
    find . -name '.envrc' -execdir direnv allow . pwd  \;
    find . -name '.envrc' -execdir direnv exec . pwd  \;
    ```

## Usage

1.  **Explore the Components:**

    *   `cli`:  The OpenServerless command-line interface.  Use `ops --help` for usage information.
    *   `olaris-op`: The OpenServerless Operator.  Deploy using Kubernetes manifests (not included in this repo).
    *   `site`:  The project website source code.
    *   `runtimes`: Configuration files and documentation for supported runtimes.
    *    `testing`: unit and integration tests for OP.

2.  **Developing with OpenServerless:**

    Refer to the documentation on the [Apache OpenServerless website](https://openserverless.apache.org) for detailed guides on developing, deploying, and managing serverless functions and applications.

3.  **Contribution:**  Contributions are welcome!  Please follow the guidelines outlined in the `CONTRIBUTING.md` (not present in this repo, refer to the official documentation) file on the project website.

## Repository Structure

*   `.asf.yaml`: Apache Software Foundation project configuration.
*   `.github/ISSUE_TEMPLATE`: Template for creating new issues.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `.gitmodules`: Tracks submodules used by the project.
*   `DISCLAIMER`: Legal disclaimer regarding the project's status.
*   `LICENSE`: Apache 2.0 License.
*   `NOTICE`: Notices and attribution information.
*   `assets/logos`: Project logos in different formats.
*   `bash_aliases`: Useful shell aliases.
*   `cli`: Source code for the OpenServerless command-line interface.
*   `cloud-init.yaml`:  Cloud Initialization file for configuration.
*   `devcontainer`: Development Container configuration for VS Code.
*   `direnv-init.sh`: Script to initialize the development environment with direnv.
*   `get-diff.sh`: Script to identify diffs.
*   `olaris`: Contains various utilities and components.
*   `olaris-op`: Source code for the OpenServerless Operator.
*   `openserverless-cli.code-workspace`: VS Code workspace configuration for the CLI.
*   `openserverless-operator.code-workspace`: VS Code workspace configuration for the Operator.
*   `openserverless.code-workspace`: VS Code workspace configuration for the entire project.
*   `runtimes`: Specifies available runtimes.
*   `site`: Source code for the Apache OpenServerless website.
*   `sync-branch.sh`: This script synchronizes the specified branch.
*   `testing`: Unit and integration tests.
*   `update-tree.sh`:  Script for updating the repository tree.
*   `vscode`: VS Code extensions or configuration related files.

## Contributing

Please review the [CONTRIBUTING.md](https://github.com/apache/openserverless/blob/main/CONTRIBUTING.md) guidelines on the project website for more information about contributing to Apache OpenServerless.

## License

This project is licensed under the Apache License 2.0.  See [LICENSE](LICENSE) for details.