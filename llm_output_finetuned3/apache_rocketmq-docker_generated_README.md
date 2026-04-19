# Apache RocketMQ Docker

## Description
This repository provides Docker images and configuration files for Apache RocketMQ, a distributed messaging system. It includes Dockerfiles for building RocketMQ images on various base images (Alpine, Ubuntu, CentOS), Kubernetes Helm charts for deploying RocketMQ in Kubernetes clusters, and scripts for quickly starting and testing RocketMQ components.

The repository supports multiple deployment scenarios including standalone Docker containers, Kubernetes deployments, and RocketMQ with TLS encryption. It includes configuration templates for brokers, nameservers, and the RocketMQ dashboard.

## Features
- Docker images for RocketMQ on Alpine, Ubuntu, and CentOS base images
- Kubernetes Helm charts for deploying RocketMQ in Kubernetes clusters
- Docker Compose configuration for quick setup and testing
- Support for TLS encryption with certificate-based authentication
- Support for DLedger (Raft-based) cluster configuration
- Scripts for starting and testing RocketMQ components
- Configuration templates for various RocketMQ deployment scenarios

## Prerequisites / Requirements
- Docker or Docker Compose installed
- Kubernetes cluster (for Helm charts)
- Java 8 or Java 11 installed (required by RocketMQ)
- Access to the internet for downloading RocketMQ binaries from Apache's mirrors

## Installation
### Build RocketMQ Docker Images
Build RocketMQ images using the provided Dockerfiles:

```bash
# Build for Alpine
sh image-build/build-image.sh 4.5.0 alpine

# Build for Ubuntu
sh image-build/build-image.sh 4.5.0 ubuntu

# Build for CentOS
sh image-build/build-image.sh 4.5.0 centos
```

### Build RocketMQ Dashboard Image
Build the RocketMQ dashboard image:

```bash
sh image-build/build-image-dashboard.sh 4.5.0 centos
```

## Usage
### Run RocketMQ with Docker Compose
Start RocketMQ components using Docker Compose:

```bash
# Run with default configuration
sh templates/play-docker.sh ubuntu

# Run with TLS encryption
sh templates/play-docker-tls.sh ubuntu

# Run with DLedger cluster
sh templates/play-docker-dledger.sh
```

### Run RocketMQ in Kubernetes
Deploy RocketMQ using Helm:

```bash
# Install the Helm chart
helm install rocketmq apache/rocketmq-k8s-helm

# View deployed resources
kubectl get pods
```

### Start RocketMQ Components Manually
Start individual components using the provided scripts:

```bash
# Start nameserver
sh product/start-ns.sh ./data/namesrv 4.5.0 ubuntu

# Start broker
sh product/start-broker.sh ./data/broker 4.5.0 localhost:9876 broker.conf ubuntu

# Start RocketMQ dashboard
sh product/start-dashboard.sh 4.5.0
```

## Contributing
Contributions are welcome. Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Commit your changes with clear, descriptive messages
4. Push to the branch and open a pull request

Please ensure all changes are thoroughly tested and documented.

## License
Apache License 2.0

## Contact / Authors
This repository is maintained by the Apache Software Foundation. For questions or issues, please open an issue on GitHub or contact the Apache RocketMQ community.