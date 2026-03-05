# RocketMQ Docker Project - README

## Description

This repository provides Docker images and related resources for running Apache RocketMQ. It supports various base images (Alpine, CentOS, Ubuntu) and configurations. The repository aims to simplify the deployment and management of RocketMQ in containerized environments, with  support for Kubernetes deployments via Helm charts.  This repo provides several deployment options, including standalone, and clustered setups for development, testing, and production purposes.

## Features

*   **Multiple Base Images:** Offers Docker images based on Alpine Linux, CentOS, and Ubuntu, allowing you to choose the most suitable one based on your requirements (image size, compatibility, etc.).
*   **Helm Charts:** Includes Kubernetes Helm charts for easy deployment and management of RocketMQ in a Kubernetes cluster. This includes deployments for Namesrv, Broker and Controller.
*   **Docker Compose:**  Provides `docker-compose.yml` files for quick local development and testing.
*   **Dledger Support:** Includes configuration and examples showcasing the use of Dledger for distributed consensus and higher availability of message storage.
*   **TLS Support:** Configurations and scripts are provided to enable TLS/SSL for secure communication between RocketMQ components.
*   **Customizable Configurations:**  Offers example configuration files that can be customized to tailor RocketMQ behavior to specific needs.
*   **Automated Image builds:** GitHub Actions and makefiles automate Docker image building and publishing.
*   **Play Scripts:**  Includes scripts (`play-docker.sh`, `play-docker-dledger.sh`, etc.) to assist with local testing.

## Installation

1.  **Prerequisites:**
    *   Docker
    *   Docker Compose (for `docker-compose.yml` based deployments)
    *   kubectl (for Kubernetes deployments)
    *   Helm (for Kubernetes deployments)

2.  **Clone the Repository:**

    ```bash
    git clone https://github.com/apache/rocketmq-docker.git
    cd rocketmq-docker
    ```

## Usage

### 1. Docker Compose (Local Development)

1.  Navigate to the `templates` directory:

    ```bash
    cd templates
    ```

2.  Run the docker-compose file.  There are two available: `rmq4-docker-compose.yml` and `rmq5-docker-compose.yml`. The `rmq5` file uses RocketMQ 5.x. Choose one based on your needs:

    ```bash
    docker-compose -f rmq4-docker-compose.yml up -d
    ```

3.   Access the services:

    *   Nameserver: `http://localhost:9876`
    *   Broker: `http://localhost:10909`, `http://localhost:10911`, `http://localhost:10912`
    *   Proxy: `http://localhost:8080`

### 2.  Kubernetes Deployment (using Helm)

1.  Add the Helm repository (if needed):

    ```bash
    helm repo add apache https://apache.github.io/rocketmq-k8s-helm/
    helm repo update
    ```

2.  Install RocketMQ using Helm:

    ```bash
    helm install rocketmq apache/rocketmq
    ```

3.  Customize the deployment using the `values.yaml` file within the `rocketmq-k8s-helm` directory.  Adjust settings like replica counts, resource limits, and image tags as needed.

4.  Check the deployment status:

    ```bash
    kubectl get all -n default
    ```

### 3. Docker Image Build

1.  Navigate to the `image-build` directory:

    ```bash
    cd image-build
    ```
2.  To build an image for a specific version and base image, run the `build-image.sh`:
     ```bash
     ./build-image.sh <version> <base_image>
     ```
     Replace `<version>` with the desired RocketMQ version and `<base_image>` with either `alpine`, `ubuntu`, or `centos`.

### 4. Running play scripts

The `templates` folder contains several play scripts to demonstrate basic working configurations. For example, `play-docker-dledger.sh` creates a three-node RocketMQ cluster using Dledger consensus.

## Other Information

*   **Configuration Files:** The `product/conf` directory contains example configuration files for RocketMQ brokers and nameservers.  Adjust these files as needed for your specific environment.
*   **GitHub Actions:**  This repository utilizes GitHub Actions (defined in `.github/workflows/docker-publish.yml`) to automate Docker image building and publishing.
*   **License:**  This project is licensed under the Apache 2.0 License. See `LICENSE` for details.
*   **Documentation:**  Refer to the official Apache RocketMQ documentation for detailed information on configuring and using RocketMQ: [https://rocketmq.apache.org/](https://rocketmq.apache.org/)
*   **Contributing:** Contributions are welcome! Please see `CONTRIBUTING.md` for guidelines.