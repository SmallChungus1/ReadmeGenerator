# Apache RocketMQ Docker Images - README

## Description

This repository provides Docker images and associated configurations for Apache RocketMQ. It aims to simplify the deployment and management of RocketMQ in containerized environments. The images are available for various base images (Alpine, CentOS, Ubuntu) and configurations. This repository also includes Helm charts for Kubernetes deployment.

## Features

*   **Multiple Base Images:** Provides images built on Alpine Linux, CentOS, and Ubuntu, catering to different size and dependency requirements.
*   **Pre-configured Images:**  Offers pre-configured images for Namesrv, Broker and Dashboard, simplifying deployment.
*   **Configuration Flexibility:** Includes a variety of configuration examples in the `product/conf` directory for different deployment scenarios (e.g., 2M-2S sync, 2M-2S async, no-slave).
*   **Docker Compose:** Contains `docker-compose.yml` files for quick local development and testing.
*   **Kubernetes Helm Charts:** Integrates with Kubernetes using Helm charts for easy deployment and scaling in production environments.
*   **Dledger Support:** Configurations included for running RocketMQ with Dledger.
*   **TLS Support:** SSL configurations present in the `templates/ssl` directory
*    **Build Scripts:** Provides build scripts for generating images customized for your needs.

## Installation

1.  **Docker:** Ensure you have Docker installed on your system.  See [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/) for installation instructions.

2.  **Kubectl (for Kubernetes deployments):** If you plan to deploy with Kubernetes, install `kubectl`. See [https://kubernetes.io/docs/tasks/tools/install-kubectl/](https://kubernetes.io/docs/tasks/tools/install-kubectl/).

3.  **Helm (for Kubernetes deployments):** To use the Helm charts, ensure you have Helm installed. See [https://helm.sh/docs/intro/install/](https://helm.sh/docs/intro/install/).

## Usage

### 1. Using Pre-built Docker Images

The project provides pre-built docker images in Docker Hub via the `apache/rocketmq` repository.

*   **Namesrv:** `apache/rocketmq:<version>` (e.g., `apache/rocketmq:5.1.0`)
*   **Broker:** `apache/rocketmq:<version>` (e.g., `apache/rocketmq:5.1.0`)
*   **Dashboard:** `apache/rocketmq-dashboard:<version>` (e.g., `apache/rocketmq-dashboard:0.1.2`)

To run a RocketMQ cluster, you can use the provided `docker-compose.yml`files (e.g., `rmq4-docker-compose.yml` or `rmq5-docker-compose.yml`) :

```bash
docker-compose -f docker-compose/rmq4-docker-compose.yml up -d
```

### 2. Building Docker Images Locally

If you want to build the images yourself (e.g., to customize them), you can use the provided build scripts:

```bash
# Build Alpine image
bash image-build/build-image.sh <version> alpine

# Build Ubuntu image
bash image-build/build-image.sh <version> ubuntu
```

Replace `<version>` with the desired RocketMQ version.

To build the dashboard image:

```bash
bash image-build/build-image-dashboard.sh <version> centos
```

### 3. Kubernetes Deployment with Helm

1.  **Add the Helm repository:**

    ```bash
    helm repo add rocketmq https://apache.github.io/rocketmq-helm/
    helm repo update
    ```

2.  **Install the chart:**

    ```bash
    helm install my-rocketmq rocketmq/rocketmq
    ```

3.  **Customize the deployment:**

    You can customize the deployment using values.yaml:

    ```bash
    helm install my-rocketmq rocketmq/rocketmq -f my-values.yaml
    ```

## Configuration

The `product/conf` directory contains various configuration files for different deployment scenarios.  You can customize these files and mount them as volumes when running the Docker containers.  Key configuration files include:

*   `broker.conf`: General Broker configuration.
*   `2m-2s-sync/broker-a.properties`: Configuration for a Broker in a 2 Master 2 Slave synchronous replication setup.
*   `2m-2s-async/broker-a.properties`: Configuration for a Broker in a 2 Master 2 Slave asynchronous replication setup.
*   `2m-noslave/broker-a.properties` Broker configuration with no slave

## Other Information

*   **License:** Apache License 2.0 (See `LICENSE` file).
*   **Contributing:** Contributions are welcome!  Please see the `CONTRIBUTING.md` file for details.
*   **GitHub Actions:** This repository uses GitHub Actions to automatically build and publish docker images.  The workflow is defined in `.github/workflows/docker-publish.yml`.
*   **Issue Template:** Use the issue template provided in `.github/ISSUE_TEMPLATE` when reporting bugs or requesting features.
*   **Known Issues :** Check the [issue tracker](https://github.com/apache/rocketmq-docker/issues).