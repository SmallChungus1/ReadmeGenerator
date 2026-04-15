```markdown
# RocketMQ Docker Images

This repository provides Docker images and related resources for running Apache RocketMQ. It includes configurations for various deployment scenarios, including single-node, master-slave, and Dledger-based deployments.

## Description

This project aims to simplify the deployment and management of Apache RocketMQ using Docker and Kubernetes. It provides pre-configured Docker images, Docker Compose files, and Kubernetes manifests to quickly get a RocketMQ cluster up and running. It supports different configurations for testing, development, and production environments.

## Features

*   **Pre-built Docker Images:** Provides readily available Docker images for RocketMQ, reducing the need for manual builds.
*   **Docker Compose Support:** Includes `docker-compose.yml` files for easy local development and testing.
*   **Kubernetes Manifests:** Offers Kubernetes deployment configurations for production environments.
*   **Multiple Deployment Scenarios:** Supports various deployment topologies, including single-node, master-slave, and Dledger-based deployments.
*   **Configuration Examples:** Provides example configuration files for different deployment scenarios.
*   **SSL/TLS Support:** Includes configurations for secure communication using SSL/TLS.
*   **Helm Chart:** Provides a Helm chart for streamlined Kubernetes deployments.

## Table of Contents

*   [Prerequisites / Requirements](#prerequisites--requirements)
*   [Installation](#installation)
*   [Usage](#usage)
*   [Contributing](#contributing)
*   [License](#license)
*   [Contact / Authors](#contact--authors)

## Prerequisites / Requirements

*   Docker: Version 20.0 or higher
*   Docker Compose: Version 1.29 or higher
*   Kubernetes (for Kubernetes deployments): Version 1.20 or higher
*   Helm (for Kubernetes deployments): Version 3.0 or higher
*   Java 8 or higher

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/apache/rocketmq-docker.git
    cd rocketmq-docker
    ```

2.  **Build the Docker images (optional):**

    If you want to build the images yourself, navigate to the `image-build` directory and run the appropriate build script. For example:

    ```bash
    ./build-image.sh 5.1.0 alpine
    ```

    Replace `5.1.0` with the desired RocketMQ version and `alpine` with the desired base image (e.g., `ubuntu`).

## Usage

### Docker Compose

To run RocketMQ using Docker Compose, navigate to the `templates/docker-compose` directory and run:

```bash
docker-compose up -d
```

This will start the RocketMQ nameserver and broker containers.

### Kubernetes

To deploy RocketMQ to Kubernetes, use the provided Helm chart:

```bash
helm install rocketmq rocketmq-k8s-helm
```

### Running Examples

Several example configurations are provided in the `product/conf` directory.  You can use these as a starting point for your own deployments.  The `templates` directory contains scripts to facilitate testing and demonstration deployments.

## Contributing

We welcome contributions to this project! Please follow these guidelines:

*   Fork the repository.
*   Create a new branch for your changes.
*   Make your changes and commit them with descriptive messages.
*   Submit a pull request.

See [CONTRIBUTING.md](CONTRIBUTING.md) for more detailed instructions.

## License

This project is licensed under the Apache License, Version 2.0 - see the [LICENSE](LICENSE) file for details.

## Contact / Authors

This project is maintained by the Apache RocketMQ community.  You can reach us through the following channels:

*   [Apache RocketMQ Website](https://rocketmq.apache.org/)
*   [GitHub Issues](https://github.com/apache/rocketmq-docker/issues)