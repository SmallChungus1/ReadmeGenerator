# Apache RocketMQ Docker

A comprehensive Docker and Kubernetes deployment solution for Apache RocketMQ, providing easy-to-use scripts and configurations for running RocketMQ in local environments, Docker Compose, and Kubernetes clusters.

---

## Description

Apache RocketMQ is a distributed messaging system designed for high-throughput, low-latency message delivery. This repository offers a complete Docker-based deployment solution that simplifies the setup, configuration, and management of RocketMQ components including **Nameserver**, **Broker**, **Proxy**, and **Dashboard**.

The project includes:
- **Docker images** built for multiple base OS images (Alpine, Ubuntu, CentOS)
- **Docker Compose** configurations for quick local testing
- **Kubernetes Helm charts** for production-grade deployments
- **SSL/TLS support** for secure communication
- **DLedger (Raft) mode** for high-availability clusters
- **Pre-configured examples** for common use cases (e.g., async/master, sync/master, no-slave)

This solution is ideal for developers, testers, and DevOps engineers who want to rapidly prototype or deploy RocketMQ without managing complex build or configuration processes.

---

## Features

- ✅ **Multiple Base Images**: Supports Alpine, Ubuntu, and CentOS for lightweight or feature-rich environments.
- ✅ **Docker Compose**: Easy setup with `play-docker-compose.sh` for local development.
- ✅ **Kubernetes Helm**: Deploy RocketMQ services (Nameserver, Broker, Proxy, Controller) via Helm charts.
- ✅ **SSL/TLS Support**: Secure communication using client/server certificates.
- ✅ **DLedger Raft Clusters**: High-availability broker clusters with automatic failover.
- ✅ **Dashboard Integration**: Visual monitoring of RocketMQ clusters via the RocketMQ Dashboard.
- ✅ **Pre-configured Scenarios**: Ready-to-use configurations for common topologies (async, sync, no-slave).
- ✅ **Customizable JVM Settings**: Tailored memory and GC options for performance tuning.
- ✅ **Auto-Update Scripts**: Automatically build and push images for the latest RocketMQ version.

---

## Table of Contents

- [Prerequisites / Requirements](#prerequisites--requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

---

## Prerequisites / Requirements

- **Docker** (v19.03+ recommended)
- **docker-compose** (v2.0+)
- **kubectl** (for Kubernetes operations)
- **Helm** (v3.0+ for Kubernetes deployment)
- **Java 8 or Java 11** (required for RocketMQ runtime)
- **Git** (to clone the repository)

> ⚠️ **Note**: The project uses the Apache RocketMQ source code from `https://archive.apache.org/dist/rocketmq/`. Ensure you have internet access to download the binaries.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/apache/rocketmq-docker.git
cd rocketmq-docker
```

### 2. Build Docker Images

Build and tag the RocketMQ images for your preferred base image:

#### For Alpine (lightweight):
```bash
sh image-build/build-image.sh 4.5.0 alpine
```

#### For Ubuntu:
```bash
sh image-build/build-image.sh 4.5.0 ubuntu
```

#### For CentOS:
```bash
sh image-build/build-image.sh 4.5.0 centos
```

> 🔍 Replace `4.5.0` with any valid version (e.g., `5.0.0`) in `X.X.X` format.

### 3. (Optional) Build RocketMQ Dashboard

To build the RocketMQ Dashboard (GUI):

```bash
sh image-build/build-image-dashboard.sh 4.5.0 centos
```

> This creates `apache/rocketmq-dashboard:4.5.0-centos`.

### 4. (Optional) Update to Latest Version

Automatically build and push the latest stable version:

```bash
sh image-build/update.sh
```

This script:
- Fetches the latest RocketMQ version from the Apache archive
- Builds images for Alpine and Ubuntu
- Pushes them to Docker Hub

---

## Usage

### 1. Run RocketMQ Locally with Docker Compose

#### Step 1: Prepare a directory
```bash
mkdir -p data/namesrv logs data/broker/store data/broker/logs
```

#### Step 2: Start with a single broker
```bash
sh templates/play-docker.sh ubuntu
```

> This starts a Nameserver and a Broker with default configuration.

#### Step 3: Start with Dledger (Raft) Cluster
```bash
sh templates/play-docker-dledger.sh
```

> Creates a 3-node Dledger cluster with automatic failover.

#### Step 4: Start with TLS Encryption
```bash
sh templates/play-docker-tls.sh
```

> Uses SSL certificates for secure broker-to-nameserver communication.

#### Step 5: Start with Dashboard
```bash
sh product/start-dashboard.sh 4.5.0
```

> Starts the RocketMQ Dashboard on port `6765` (accessible at `http://localhost:6765`).

---

### 2. Deploy to Kubernetes with Helm

#### Step 1: Install Helm (if not already installed)

```bash
curl -fsSL https://get.helm.sh/helm-v3.14.0-linux-amd64.tar.gz | tar -xzf -
sudo mv linux-amd64/helm /usr/local/bin/helm
```

#### Step 2: Deploy RocketMQ

```bash
helm install rocketmq ./rocketmq-k8s-helm --namespace rocketmq --create-namespace
```

> This deploys:
> - Nameserver (1 replica)
> - Broker (1 replica)
> - Proxy (1 replica)
> - Controller (3 replicas for Raft)

#### Step 3: View Services

```bash
kubectl get svc -n rocketmq
```

> Output includes services like `rocketmq-nameserver`, `rocketmq-broker`, and `rocketmq-proxy`.

#### Step 4: Access Dashboard (if enabled)

The Dashboard is not included in the default Helm chart. You must deploy it separately using:

```bash
docker run -d -it --name rocketmq-dashboard -p 6765:8080 apache/rocketmq-dashboard:4.5.0-centos
```

---

### 3. Use Pre-Configured Examples

The `product/conf/` directory contains ready-to-use configuration files:

| Scenario | Description |
|--------|-------------|
| `2m-2s-async` | 2 brokers, async master/slave |
| `2m-2s-sync` | 2 brokers, sync master/slave |
| `2m-noslave` | 2 brokers, no slave (standalone) |
| `broker-trace` | Broker with tracing enabled |

To use a configuration:

```bash
sh product/start-broker.sh ./data/broker 4.5.0 127.0.0.1:9876 broker-a.properties
```

> Replace paths and IPs as needed.

---

## Contributing

We welcome contributions from the community! Please follow these guidelines:

- Fork the repository
- Create a feature branch (`feature/your-feature`)
- Commit your changes with clear, descriptive messages
- Submit a pull request with a detailed description of your changes

For bug reports or feature requests, please open an issue in the GitHub repository.

> ❗ All contributions must comply with the Apache License 2.0 and follow the project's code style and documentation standards.

---

## License

This project is licensed under the **Apache License, Version 2.0**.

> See the [LICENSE](LICENSE) file for details.

---

## Contact / Authors

- **Project Maintainers**: Apache Software Foundation (ASF)
- **RocketMQ Team**: [https://rocketmq.apache.org](https://rocketmq.apache.org)
- **GitHub**: [https://github.com/apache/rocketmq-docker](https://github.com/apache/rocketmq-docker)
- **Discord**: [https://discord.gg/rocketmq](https://discord.gg/rocketmq)
- **Email**: rocketmq-dev@apache.org

For questions, feedback, or support, please reach out to the RocketMQ community via the official channels.

--- 

> 🚀 *Deploy RocketMQ with confidence — fast, secure, and scalable.*