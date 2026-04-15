# Apache RocketMQ Docker

![Apache License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![GitHub Stars](https://img.shields.io/github/stars/apache/rocketmq-docker?style=flat)
![Docker Hub](https://img.shields.io/docker/pulls/apache/rocketmq)

A comprehensive Docker and Kubernetes solution for deploying Apache RocketMQ, the high-performance, distributed messaging system.

---

## Description

Apache RocketMQ Docker provides a complete, production-ready environment for running Apache RocketMQ using Docker containers and Kubernetes Helm charts. This project enables developers and operations teams to quickly deploy, configure, and manage RocketMQ clusters across various environments — from local development to production Kubernetes clusters.

The solution includes:
- **Docker images** built for multiple base OSes (Alpine, Ubuntu, CentOS) with support for both standard and TLS-secured communication.
- **Docker Compose** templates for easy local development and testing.
- **Helm charts** for Kubernetes deployment with support for brokers, nameservers, controllers, and proxies.
- **Configuration templates** for different cluster topologies (e.g., master-slave, synchronous replication, Dledger Raft clusters).
- **SSL/TLS support** for secure messaging and client authentication.

This project is ideal for developers, DevOps engineers, and cloud architects who need a reliable, scalable messaging platform with minimal configuration overhead.

---

## Features

- ✅ **Multi-Platform Support**: Docker images built for Alpine, Ubuntu, and CentOS.
- ✅ **Flexible Deployment Options**: Deploy via Docker Compose or Kubernetes (Helm).
- ✅ **Secure Communication**: Built-in support for TLS/SSL with client and server certificate authentication.
- ✅ **Dledger Raft Clusters**: Support for distributed, fault-tolerant broker clusters.
- ✅ **Configurable Topologies**: Support for ASYNC_MASTER, SYNC_MASTER, and SLAVE broker roles.
- ✅ **Dashboard Integration**: Pre-built RocketMQ Dashboard for monitoring and management.
- ✅ **Automated Image Building**: Scripts to build and push RocketMQ images to Docker registries.
- ✅ **Customizable JVM Settings**: Fine-tuned memory and GC options for performance optimization.
- ✅ **Production-Grade Helm Charts**: Fully annotated Kubernetes manifests with readiness/liveness probes and resource limits.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Prerequisites

Before using this project, ensure the following are installed:

- **Docker** (v19.03+ or later) — for local containerization.
- **Docker Compose** (v2.0+ or later) — for running RocketMQ in local environments.
- **kubectl** (v1.20+ or later) — for Kubernetes operations (optional, for Helm usage).
- **Helm** (v3.0+ or later) — for deploying RocketMQ on Kubernetes clusters.
- **Java 8 or 11** — required for RocketMQ runtime.
- **Git** — to clone the repository.

> **Note**: The project supports multiple base images. For Docker, Alpine is lightweight and efficient; Ubuntu and CentOS offer more compatibility with older tools.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/apache/rocketmq-docker.git
cd rocketmq-docker
```

### 2. Build RocketMQ Docker Images (Optional)

To build and tag images for local use:

```bash
# Build for Alpine
sh image-build/build-image.sh 4.5.0 alpine

# Build for Ubuntu
sh image-build/build-image.sh 4.5.0 ubuntu
```

> **Note**: Replace `4.5.0` with the desired RocketMQ version. Valid versions must follow `X.X.X` format (e.g., `4.5.0`).

### 3. Build RocketMQ Dashboard (Optional)

```bash
sh image-build/build-image-dashboard.sh 4.5.0 centos
```

This builds the RocketMQ Dashboard image for CentOS-based environments.

---

## Usage Examples

### 1. Run RocketMQ Locally with Docker Compose

Create a local `docker-compose.yml` using the provided templates:

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

Start the services:

```bash
docker compose -f ./docker-compose/docker-compose.yml up -d
```

> **Tip**: For Dledger Raft clusters, use `play-docker-dledger.sh` to start a 3-node broker cluster with automatic peer discovery.

---

### 2. Deploy to Kubernetes with Helm

1. Install the Helm chart:

```bash
helm repo add rocketmq https://github.com/apache/rocketmq-k8s-helm
helm repo update
```

2. Deploy a basic broker cluster:

```bash
helm install my-rocketmq rocketmq/rocketmq \
  --set broker.replicaCount=1 \
  --set broker.image.tag=4.5.0
```

3. Access the dashboard (if enabled):

```bash
# After deployment, access the dashboard at http://<your-cluster-ip>:6765
```

> **Note**: For production, enable persistence, set resource limits, and configure TLS in `values.yaml`.

---

### 3. Use SSL/TLS for Secure Communication

To enable TLS, use the `play-docker-tls.sh` script:

```bash
sh templates/play-docker-tls.sh
```

This script:
- Starts the nameserver and broker with TLS enabled.
- Uses client/server certificates from the `templates/ssl/` directory.
- Requires the `ssl.properties` file to define certificate paths and trust settings.

> **Security Note**: Certificates are provided in the `templates/ssl/` folder. For production, use self-signed or CA-signed certificates.

---

### 4. Run the RocketMQ Dashboard

Start the dashboard with:

```bash
sh product/start-dashboard.sh 4.5.0
```

Access it at `http://localhost:6765`.

---

## Contributing

We welcome contributions to improve the documentation, add new features, or fix bugs.

### How to Contribute

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear, descriptive messages.
4. Submit a pull request with a detailed description of your changes.

### Reporting Issues

If you find a bug or have a feature request, please open an issue in the [RocketMQ GitHub repository](https://github.com/apache/rocketmq/issues).

> **Note**: All contributions are governed by the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

---

## License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

---

## Contact

- **Project Maintainers**: Apache RocketMQ Team
- **GitHub**: [https://github.com/apache/rocketmq-docker](https://github.com/apache/rocketmq-docker)
- **RocketMQ Documentation**: [https://rocketmq.apache.org](https://rocketmq.apache.org)
- **Community Forum**: [https://github.com/apache/rocketmq/discussions](https://github.com/apache/rocketmq/discussions)

For questions or feedback, please reach out to the RocketMQ community via the above links.