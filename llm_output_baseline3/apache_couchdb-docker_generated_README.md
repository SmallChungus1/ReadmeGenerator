# Apache CouchDB Docker Images

![Build Status](https://github.com/apache/couchdb-docker/workflows/CI/badge.svg)
![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)

A collection of Docker images for Apache CouchDB, providing a reliable, consistent, and secure way to run CouchDB in containers across various environments including OpenShift, Kubernetes, and local development.

---

## Description

Apache CouchDB is a NoSQL document database that provides flexible, scalable, and highly available data storage. This repository offers pre-built Docker images for Apache CouchDB across multiple versions and architectures, enabling developers and operators to deploy CouchDB with minimal configuration.

The images are designed to be secure, production-ready, and compatible with container orchestration platforms. Each image includes:

- A dedicated CouchDB user with proper permissions
- Secure default configurations (no logging to files)
- Support for custom configuration via environment variables
- Automatic setup of data directories and configuration files
- Support for distributed clusters via `NODENAME` and Erlang cookie management

This project is maintained by the Apache CouchDB community and is intended for use in production environments where reliability, security, and ease of deployment are critical.

---

## Features

- ✅ **Multiple versions** available: 2.3.1, 3.1.2, 3.2.3, 3.3.3, 3.4.1, 3.4.2, 3.4.3, 3.5.0, 3.5.1
- ✅ **Multiple base images**:
  - Debian-based (default)
  - Red Hat UBI (for OpenShift compatibility)
- ✅ **Support for distributed clusters** via `NODENAME` and Erlang cookie
- ✅ **Secure by default**:
  - No logging to files
  - Admin access requires explicit configuration
- ✅ **Customizable via environment variables**:
  - `COUCHDB_USER`, `COUCHDB_PASSWORD`, `COUCHDB_SECRET`, `NODENAME`, `COUCHDB_ERLANG_COOKIE`
- ✅ **Support for "Clouseau" search engine** (in 3.1.2-ubi-clouseau images)
- ✅ **Multi-architecture support** (x86_64, ARM64, s390x) via `buildx`
- ✅ **Easy integration with Kubernetes and OpenShift** via standard Docker image tags
- ✅ **Automatic ownership and permission fixes** to ensure security and compatibility

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Prerequisites

Before using these images, ensure you have the following:

- **Docker** installed (version 19.03+ recommended)
- **Docker Compose** (optional, for multi-container setups)
- **Access to a container registry** (e.g., Docker Hub, private registry)
- **Basic knowledge of Docker commands** (`docker run`, `docker pull`, `docker build`)

> **Note**: The images are built and pushed to Docker Hub. You can pull them directly using the `apache/couchdb:<version>` tag.

---

## Installation

### 1. Pull a CouchDB Image

You can pull any version of the CouchDB image directly from Docker Hub:

```bash
# Pull the latest stable version
docker pull apache/couchdb:3.5.1

# Pull a specific version
docker pull apache/couchdb:3.4.3

# Pull a UBI-based version (OpenShift compatible)
docker pull apache/couchdb:3.5.1-ubi
```

### 2. Build a Custom Image (Optional)

To build a custom image from source, use the `build.sh` script:

```bash
# Build for a specific version
./build.sh buildx 3.5.1

# Build and tag with a custom name
./build.sh buildx 3.5.1 as latest
```

> The script supports building for multiple architectures (x86_64, ARM64, s390x) and will push the images to Docker Hub.

### 3. Use UBI Base (OpenShift Compatible)

For OpenShift environments, use the UBI-based images:

```bash
docker pull apache/couchdb:3.5.1-ubi
```

These images are optimized for Red Hat OpenShift and include OpenShift-specific labels and resource requirements.

---

## Usage

### Basic Container Run

Run a CouchDB container with a basic configuration:

```bash
docker run -d \
  --name couchdb \
  -p 5984:5984 \
  -e COUCHDB_USER=admin \
  -e COUCHDB_PASSWORD=password \
  apache/couchdb:3.5.1
```

> This starts a CouchDB instance with admin credentials. The database is accessible at `http://localhost:5984`.

### Secure Setup with Custom Configuration

To enable secure access, set the `COUCHDB_SECRET` environment variable:

```bash
docker run -d \
  --name couchdb \
  -p 5984:5984 \
  -e COUCHDB_USER=admin \
  -e COUCHDB_PASSWORD=password \
  -e COUCHDB_SECRET=your-secure-secret \
  apache/couchdb:3.5.1
```

### Cluster Mode

To run CouchDB in a distributed cluster, set the `NODENAME` and `COUCHDB_ERLANG_COOKIE`:

```bash
docker run -d \
  --name couchdb-node1 \
  -p 5984:5984 \
  -e NODENAME=couchdb-node1 \
  -e COUCHDB_ERLANG_COOKIE=your-secure-cookie \
  apache/couchdb:3.5.1
```

> The `NODENAME` ensures the node is uniquely identified in the cluster. The cookie is used for inter-node communication.

### Use with Clouseau (Search Engine)

The `3.1.2-ubi-clouseau` image includes Clouseau, a full-text search engine for CouchDB:

```bash
docker run -d \
  --name couchdb-search \
  -p 5988:5988 \
  -e NODENAME=couchdb-search \
  -e COUCHDB_ERLANG_COOKIE=your-secure-cookie \
  apache/couchdb:3.1.2-ubi-clouseau
```

> This image runs both CouchDB and Clouseau. The search service is accessible at `http://localhost:5988`.

### Use with Docker Compose

Create a `docker-compose.yml` file for a multi-container setup:

```yaml
version: '3.8'
services:
  couchdb:
    image: apache/couchdb:3.5.1
    ports:
      - "5984:5984"
    environment:
      - COUCHDB_USER=admin
      - COUCHDB_PASSWORD=password
    volumes:
      - ./data:/opt/couchdb/data

  search:
    image: apache/couchdb:3.1.2-ubi-clouseau
    ports:
      - "5988:5988"
    environment:
      - NODENAME=search-node
      - COUCHDB_ERLANG_COOKIE=secure-cookie
```

---

## Contributing

We welcome contributions to improve the stability, security, and usability of these images. Please follow these guidelines:

- Fork the repository on GitHub
- Create a new branch for your feature or bug fix
- Submit a pull request with a clear description of your changes
- Ensure all images are tested and compatible with the target versions

For reporting bugs or requesting new features, please open an issue on GitHub.

> **Note**: All contributions must comply with the Apache License 2.0 and follow the project's code of conduct.

---

## License

This project is licensed under the **Apache License, Version 2.0**.

See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions, feedback, or collaboration, please contact:

- **Project Maintainers**: `dev@couchdb.apache.org`
- **GitHub Repository**: [https://github.com/apache/couchdb-docker](https://github.com/apache/couchdb-docker)
- **Apache CouchDB Project**: [https://couchdb.apache.org](https://couchdb.apache.org)

We are actively working to improve the Docker experience for CouchDB users and welcome community input.