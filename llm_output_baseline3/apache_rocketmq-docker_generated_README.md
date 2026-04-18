# Apache RocketMQ Docker

A comprehensive Docker and Kubernetes solution for deploying Apache RocketMQ, the distributed messaging system.

## Description

Apache RocketMQ Docker provides a complete, production-ready environment for deploying and managing Apache RocketMQ, a distributed messaging system designed for high-throughput, low-latency message delivery. This project offers multiple deployment options including Docker Compose, Kubernetes Helm charts, and standalone Docker images, enabling developers and operations teams to quickly set up, configure, and manage RocketMQ clusters in various environments.

The solution includes pre-configured templates for common use cases such as asynchronous and synchronous master-slave broker configurations, distributed ledger (DLedger) clusters, and secure TLS-enabled deployments. It also provides tools for testing and development, including scripts to start and stop services, produce and consume messages, and manage SSL/TLS certificates.

This project is ideal for developers, DevOps engineers, and operations teams who need a reliable, easy-to-deploy messaging infrastructure for building scalable, fault-tolerant applications.

## Features

- ✅ **Multiple Deployment Options**: Deploy RocketMQ using Docker Compose, Kubernetes Helm charts, or standalone Docker images.
- ✅ **Flexible Configuration**: Support for various broker topologies including master-slave, asynchronous/synchronous replication, and distributed ledger (DLedger) clusters.
- ✅ **Secure Communication**: Built-in support for TLS/SSL with certificate generation and configuration.
- ✅ **Pre-configured Templates**: Ready-to-use configuration files for common scenarios like 2M-2S async/sync, 2M-no-slave, and DLedger clusters.
- ✅ **Development & Testing Tools**: Scripts to start, stop, and test services with message producers and consumers.
- ✅ **Kubernetes Support**: Helm charts for deploying RocketMQ components as Kubernetes StatefulSets with proper resource management and health probes.
- ✅ **Cross-Platform Compatibility**: Supports multiple base images (Alpine, Ubuntu, CentOS) and operating systems.
- ✅ **Version Management**: Automatic versioning and build support for different RocketMQ releases.

## Table of Contents

- [Project Title](#project-title)
- [Description](#description)
- [Features](#features)
- [Prerequisites / Requirements](#prerequisites--requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

## Prerequisites / Requirements

- **Docker**: Version 18.06 or later (required for Docker Compose and containerized deployments).
- **Docker Compose**: Version 1.29 or later (required for local development and testing).
- **Kubernetes**: Version 1.16+ (for Kubernetes Helm chart deployments).
- **Helm**: Version 3.0+ (required for Kubernetes deployments).
- **Java 8 or 11**: Required for RocketMQ runtime (Java is bundled in Docker images).
- **Git**: For cloning the repository and managing version control.
- **Operating System**: Linux (Ubuntu, CentOS, or Alpine) or macOS with Docker Desktop.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/apache/rocketmq-docker.git
cd rocketmq-docker
```

### 2. Build Docker Images (Optional)

To build and push custom images to a registry:

```bash
# Build images for a specific version (e.g., 4.5.0)
sh image-build/build-image.sh 4.5.0 ubuntu

# Build and push to a private registry
sh image-build/build-image.sh 4.5.0 apache/rocketmq:custom
```

### 3. Update Images (Automated)

To automatically build and push the latest version:

```bash
sh image-build/update.sh
```

### 4. Deploy with Docker Compose

Create a `docker-compose.yml` file based on the templates:

```yaml
# templates/docker-compose/rmq4-docker-compose.yml
version: '2'
services:
  namesrv:
    image: apache/rocketmq:4.5.0
    ports:
      - 9876:9876
    volumes:
      - ./data/namesrv/logs:/home/rocketmq/logs
    command: sh mqnamesrv

  broker:
    image: apache/rocketmq:4.5.0
    ports:
      - 10909:10909
      - 10911:10911
      - 10912:10912
    environment:
      - NAMESRV_ADDR=namesrv:9876
    volumes:
      - ./data/broker/logs:/home/rocketmq/logs
      - ./data/broker/store:/home/rocketmq/store
      - ./data/broker/conf/broker.conf:/opt/rocketmq-4.5.0/conf/broker.conf
    command: sh mqbroker -c /opt/rocketmq-4.5.0/conf/broker.conf
```

### 5. Deploy with Kubernetes Helm

Deploy using Helm:

```bash
# Add the repository
helm repo add rocketmq https://github.com/apache/rocketmq-k8s-helm

# Update the repo
helm repo update

# Install the chart
helm install my-rocketmq rocketmq/rocketmq --set namespace=rocketmq
```

## Usage

### Starting a RocketMQ Cluster

#### Using Docker Compose

```bash
# Start a basic cluster
sh templates/play-docker.sh ubuntu
```

#### Using DLedger (Distributed Ledger)

```bash
sh templates/play-docker-dledger.sh
```

#### Using TLS/SSL

```bash
sh templates/play-docker-tls.sh
```

#### Using the Dashboard

```bash
# Start the RocketMQ Dashboard
sh product/start-dashboard.sh 4.5.0
```

### Producing and Consuming Messages

After starting the broker, use the provided scripts:

```bash
# Produce messages
sh templates/play-producer.sh

# Consume messages
sh templates/play-consumer.sh
```

### Configuring Brokers

Modify configuration files in the `product/conf/` directory:

- `broker-a.properties` - Master broker configuration
- `broker-b-s.properties` - Slave broker configuration
- `broker-trace.properties` - Trace-enabled broker configuration

Replace `REPLACE_IT` values with actual IP addresses or hostnames.

## Contributing

We welcome contributions to improve the RocketMQ Docker project. Please follow these guidelines:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear, descriptive messages.
4. Submit a pull request with a detailed description of your changes.

For reporting issues or suggesting new features, please open an issue in the repository. We will review and respond to all requests.

## License

This project is licensed under the **Apache License, Version 2.0**. See the [LICENSE](LICENSE) file for details.

## Contact / Authors

- **Project Maintainers**: Apache Software Foundation (ASF)
- **Primary Contact**: rocketmq-dev@apache.org
- **Community**: [Apache RocketMQ Community](https://rocketmq.apache.org)
- **GitHub**: [apache/rocketmq-docker](https://github.com/apache/rocketmq-docker)

For questions, feedback, or feature requests, please reach out to the community or open an issue in the repository.