# Apache RocketMQ Docker

## Description

Apache RocketMQ Docker provides a comprehensive set of tools and configurations for deploying and managing Apache RocketMQ, a distributed messaging and event bus system. This repository includes Docker images for RocketMQ components (nameserver, broker, proxy), Kubernetes Helm charts, and scripts to facilitate quick setup and testing in various environments, including Docker Compose and Kubernetes.

The project supports multiple base images (Alpine, Ubuntu, CentOS) and offers both standard and secure (TLS) configurations. It includes pre-defined templates for common deployment scenarios such as asynchronous and synchronous replication, standalone brokers, and distributed clusters with DLedger support. The repository also provides a dashboard for monitoring and managing RocketMQ instances.

## Features

- **Multi-Platform Support**: Docker images built for Alpine, Ubuntu, and CentOS base images.
- **Secure Communication**: TLS/SSL support with certificate generation and configuration.
- **Docker Compose Templates**: Pre-configured `docker-compose.yml` files for common setups.
- **Kubernetes Helm Charts**: Full Kubernetes deployment support with configurable resources and networking.
- **Distributed Clusters**: Support for DLedger-based distributed brokers with automatic failover.
- **Dashboard Integration**: A standalone RocketMQ dashboard for monitoring and management.
- **Customizable Configurations**: Pre-defined configuration files for various deployment topologies.
- **Automated Image Building**: Scripts to build and push RocketMQ images to Docker registries.
- **Version Management**: Tools to stage and update templates with specific RocketMQ versions.

## Installation

### Prerequisites

- Docker installed and running
- Docker Compose installed (version 2.0 or later)
- `git` for cloning the repository
- Java 8 or 11 (required for RocketMQ runtime)

### Clone and Prepare the Repository

```bash
git clone https://github.com/apache/rocketmq-docker.git
cd rocketmq-docker
```

### Build Docker Images

Build RocketMQ images for specific base images (Alpine, Ubuntu, or CentOS):

```bash
# Build for Alpine
sh image-build/build-image.sh 4.5.0 alpine

# Build for Ubuntu
sh image-build/build-image.sh 4.5.0 ubuntu

# Build for CentOS
sh image-build/build-image.sh 4.5.0 centos
```

> **Note**: Replace `4.5.0` with the desired RocketMQ version. The version must follow the format `X.X.X`.

### Build Dashboard Image (Optional)

To build the RocketMQ Dashboard image:

```bash
sh image-build/build-image-dashboard.sh 4.5.0 centos
```

## Usage

### Run a Basic RocketMQ Cluster with Docker Compose

1. Create a directory for your project:
   ```bash
   mkdir rocketmq-demo && cd rocketmq-demo
   ```

2. Copy the `docker-compose.yml` file from the templates:
   ```bash
   cp ../templates/docker-compose/rmq4-docker-compose.yml .
   ```

3. Edit the `docker-compose.yml` file to specify your RocketMQ version:
   ```yaml
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

4. Start the services:
   ```bash
   docker compose up -d
   ```

### Run a Cluster with DLedger (Distributed Replication)

Use the `play-docker-dledger.sh` script to start a distributed broker cluster:

```bash
sh templates/play-docker-dledger.sh
```

This script:
- Removes existing containers
- Creates a custom network for DLedger
- Starts a nameserver and three brokers with DLedger configuration
- Sets up network communication between brokers

### Run with TLS Encryption

To enable secure communication between components:

```bash
sh templates/play-docker-tls.sh
```

This script:
- Mounts SSL certificates and properties
- Configures the nameserver and broker with TLS settings
- Enables mutual authentication between clients and brokers

### Deploy with Kubernetes Helm

1. Install Helm (if not already available):
   ```bash
   curl -fsSL https://get.helm.sh/helm-v3.14.0-linux-amd64.tar.gz | tar -xzf -
   sudo mv linux-amd64/helm /usr/local/bin/
   ```

2. Deploy RocketMQ using Helm:
   ```bash
   helm install rocketmq ./rocketmq-k8s-helm --set broker.replicaCount=3 --set nameserver.replicaCount=1
   ```

3. View the deployed resources:
   ```bash
   kubectl get pods -l app=rocketmq
   kubectl get services -l app=rocketmq
   ```

### Access the Dashboard

To access the RocketMQ dashboard:

```bash
sh product/start-dashboard.sh 4.5.0
```

This starts the dashboard container on port 6765 (mapped to 8080). Access it via `http://localhost:6765`.

### Run Production-Ready Broker Configuration

Use the `start-broker.sh` script to start a broker with custom configuration:

```bash
sh product/start-broker.sh ./data/broker 4.5.0 127.0.0.1:9876 broker-a.properties
```

This command:
- Starts a broker with a specific configuration file
- Maps logs and data directories
- Sets the nameserver address and broker configuration

> **Note**: Replace `broker-a.properties` with any of the provided configuration files (e.g., `broker-a-s.properties`, `broker-trace.properties`) for different deployment scenarios.

### Test Message Production and Consumption

After starting the cluster, use the provided scripts to test message flow:

```bash
sh templates/play-producer.sh
sh templates/play-consumer.sh
```

These scripts use the built-in RocketMQ example to produce and consume messages, verifying the cluster is operational.