# Apache RocketMQ Docker

A comprehensive Docker and Kubernetes toolkit for deploying and managing Apache RocketMQ, including support for standalone, Docker Compose, Kubernetes Helm, and TLS configurations.

## Description

Apache RocketMQ Docker provides a complete set of tools and configurations to deploy, run, and manage Apache RocketMQ in various environments. This repository includes:

- Docker images built for multiple base images (Alpine, Ubuntu, CentOS)
- Docker Compose configurations for quick local setup
- Kubernetes Helm charts for production-grade deployments
- Configuration templates for brokers, nameservers, and proxies
- Support for TLS encryption and Dledger (Raft) cluster configurations
- Scripts for easy testing and development

The toolkit enables developers and operations teams to rapidly deploy RocketMQ in local development, testing, or production environments with minimal configuration.

## Features

- ✅ **Multi-platform support**: Docker images built for Alpine, Ubuntu, and CentOS base images
- ✅ **Docker Compose**: Easy-to-use `docker-compose.yml` files for local development and testing
- ✅ **Kubernetes Helm**: Production-ready Helm charts for Kubernetes deployments
- ✅ **TLS support**: Built-in SSL/TLS configuration with certificate management
- ✅ **Dledger (Raft) clusters**: Support for distributed, fault-tolerant broker clusters
- ✅ **Dashboard integration**: RocketMQ Dashboard for monitoring and management
- ✅ **Configuration flexibility**: Multiple broker configurations (async, sync, no-slave, trace)
- ✅ **Automated image building**: Scripts to build and push images to Docker registries
- ✅ **Version management**: Automatic version detection and templating

## Installation

### Prerequisites

- Docker (Docker Engine or Docker Desktop)
- Docker Compose (version 2.0 or later)
- `git` for cloning the repository
- `curl` and `wget` for downloading files
- Java 8 or 11 (required by RocketMQ)

### Clone the Repository

```bash
git clone https://github.com/apache/rocketmq-docker.git
cd rocketmq-docker
```

### Build Docker Images

Build and tag RocketMQ images for a specific version and base image:

```bash
# Build for Ubuntu (default)
sh image-build/build-image.sh 4.5.0 ubuntu

# Build for Alpine
sh image-build/build-image.sh 4.5.0 alpine

# Build for CentOS
sh image-build/build-image.sh 4.5.0 centos
```

> **Note**: The version must be in `X.X.X` format (e.g., `4.5.0`). The latest version can be found at [https://archive.apache.org/dist/rocketmq/](https://archive.apache.org/dist/rocketmq/).

### Build RocketMQ Dashboard (Optional)

```bash
sh image-build/build-image-dashboard.sh 4.5.0 centos
```

This builds the RocketMQ Dashboard image for CentOS.

## Usage

### Quick Start with Docker Compose

1. **Create a directory** for your RocketMQ setup:

```bash
mkdir rocketmq-demo && cd rocketmq-demo
```

2. **Copy the configuration files** from the templates:

```bash
cp ../templates/docker-compose/rmq4-docker-compose.yml .
cp ../templates/data/broker/conf/broker.conf .
```

3. **Start RocketMQ services**:

```bash
sh templates/play-docker.sh ubuntu
```

> This script starts a nameserver and broker with default configuration.

### Run with Custom Configuration

Use the `start-broker.sh` script to start a broker with custom configuration:

```bash
sh product/start-broker.sh ./data 4.5.0 127.0.0.1:9876 broker-a.properties ubuntu
```

This starts a broker with:
- Data directory: `./data`
- RocketMQ version: `4.5.0`
- Nameserver address: `127.0.0.1:9876`
- Broker configuration: `broker-a.properties`
- Base image: `ubuntu`

### Run with TLS Encryption

Start RocketMQ with TLS enabled:

```bash
sh templates/play-docker-tls.sh ubuntu
```

This starts a nameserver and broker with TLS configuration using certificates from the `templates/ssl/` directory.

### Run with Dledger (Raft) Cluster

Start a distributed broker cluster:

```bash
sh templates/play-docker-dledger.sh
```

This creates a 3-node Dledger cluster with:
- A nameserver
- Three brokers configured for Raft consensus
- Network bridge for inter-node communication

### Kubernetes Deployment

Deploy RocketMQ to Kubernetes using Helm:

```bash
# Apply the Helm chart
helm install rocketmq ./rocketmq-k8s-helm --namespace rocketmq-system
```

The Helm chart includes:
- Nameserver (with 1 replica)
- Broker (with 1 replica)
- Proxy (with 1 replica)
- Controller (with 3 replicas for Raft)

### Access the Dashboard

After starting the RocketMQ services, access the dashboard at:

```
http://localhost:6765
```

To start the dashboard:

```bash
sh product/start-dashboard.sh 4.5.0
```

> The dashboard is available on port 8080, mapped to port 6765.

### Testing with Producer/Consumer

Test message flow with the provided scripts:

```bash
# Start producer
sh templates/play-producer.sh

# Start consumer
sh templates/play-consumer.sh
```

These scripts use the built-in RocketMQ tools to send and receive messages.

---

> **Note**: All configuration files in the `product/conf/` directory are examples and require manual replacement of `REPLACE_IT` placeholders with actual IP addresses or hostnames.