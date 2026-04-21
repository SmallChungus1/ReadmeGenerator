# RocketMQ Docker Images

## Description

This repository provides Docker images for RocketMQ, including nameserver, broker, proxy, and controller components. It includes pre-built images and scripts for easy deployment and customization.  The images are based on Alpine Linux and CentOS, offering flexibility for different environments.

## Features

*   **Pre-built Images:** Ready-to-use Docker images for RocketMQ components.
*   **Customizable:** Scripts for customizing broker and controller configurations.
*   **Kubernetes Support:** Helm charts for deploying RocketMQ in Kubernetes.
*   **Multiple Base Images:**  Supports Alpine, CentOS, and Ubuntu base images.
*   **TLS Support:** Includes TLS configuration for secure communication.
*   **Dledger Support:**  Supports Dledger for data consistency.

## Prerequisites / Requirements

*   Docker installed and running.
*   Basic understanding of Docker and RocketMQ concepts.
*   (For Kubernetes deployment) A Kubernetes cluster.

## Installation

1.  **Build Images:**  Navigate to the `image-build` directory and run `bash build-image.sh <version> <base-image>`.  Replace `<version>` with the desired RocketMQ version (e.g., `4.5.0`) and `<base-image>` with the base image (e.g., `alpine`, `centos`, `ubuntu`).
2.  **Run Images:**  Use `docker run` to run the images.  Example: `docker run -d -p 9876:9876 apache/rocketmq:4.5.0-centos`
3.  **Deploy to Kubernetes:** Use the provided Helm charts to deploy RocketMQ in Kubernetes.  Follow the instructions in the `rocketmq-k8s-helm` directory.

## Usage

*   **Running a Single Broker:** `docker run -d -p 10911:10911 -v /path/to/data:/home/rocketmq/store apache/rocketmq:4.5.0`
*   **Running a Nameserver:** `docker run -d -p 9876:9876 apache/rocketmq:4.5.0`
*   **Running a Proxy:** `docker run -d -p 8080:8080 apache/rocketmq:4.5.0`
*   **Running a Controller:** `docker run -d ...` (Refer to the `image-build-ci` directory for controller customization).
*   **Deploying to Kubernetes:**  Use `helm install <release-name> ./rocketmq-k8s-helm` to deploy the RocketMQ cluster.

## Contributing

Contributions are welcome! Please follow these guidelines:

*   Fork the repository.
*   Create a new branch for your feature or bug fix.
*   Write tests for your changes.
*   Submit a pull request.

## License

This project is licensed under the Apache License, Version 2.0 - see the [LICENSE](LICENSE) file for details.