# Apache OpenServerless (Incubating)

Apache OpenServerless is an effort undergoing incubation at the Apache Software Foundation (ASF). It aims to provide a platform for building and deploying serverless applications on Kubernetes. This project is for developers and operators looking to leverage the benefits of serverless computing with the flexibility and control of Kubernetes.

## Description

Apache OpenServerless (incubating) is a cloud-native serverless framework built on Kubernetes. It allows developers to deploy and manage functions and applications without managing the underlying infrastructure. It provides a streamlined experience for building, deploying, and scaling serverless workloads.

## Features

*   Serverless Function Deployment: Deploy functions easily to a Kubernetes cluster.
*   Kubernetes Native: Built on top of Kubernetes, leveraging its scalability and robustness.
*   Submodule Structure: Organized with a submodule structure for modularity and maintainability.
*   Automated Configuration: Tools and scripts for automated configuration and setup.
*   Development Environment: Includes configurations for VS Code and DevContainers for a streamlined development experience.

## Table of Contents

*   [Prerequisites / Requirements](#prerequisites--requirements)
*   [Installation](#installation)
*   [Usage](#usage)
*   [Contributing](#contributing)
*   [License](#license)
*   [Contact / Authors](#contact--authors)

## Prerequisites / Requirements

*   Git
*   Kubernetes Cluster (e.g., Minikube, Kind, or a cloud provider's Kubernetes service)
*   kubectl
*   Go (for some components, as indicated in workspace settings)
*   Nix (for some components)
*   1Password CLI (for secret management)

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/apache/openserverless.git --recurse-submodules
    ```

2.  Navigate to the repository directory:

    ```bash
    cd openserverless
    ```

3.  Run the `sync-branch.sh` script to ensure submodules are on the correct branches:

    ```bash
    bash sync-branch.sh
    ```

4.  Initialize the development environment:

    ```bash
    bash direnv-init.sh
    ```

5.  Update the tree:

    ```bash
    bash update-tree.sh
    ```

## Usage

The project consists of several submodules, each with its own usage instructions.  The `cli`, `operator`, `site`, `task`, and `runtimes` directories contain the core components. 

For example, to run the task submodule:

```bash
cd task
```

Further instructions for each submodule can be found in their respective README files.

## Contributing

Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file (not present in the provided repository contents, but standard practice) for guidelines on how to contribute to the project, report bugs, or submit feature requests.

## License

Apache OpenServerless is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

## Contact / Authors

This project is an effort of the Apache OpenServerless community.  For more information, please visit the [Apache OpenServerless website](https://openserverless.apache.org).