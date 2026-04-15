# Apache CouchDB Docker Images

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat)](https://github.com/apache/couchdb-docker)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=flat)](https://www.apache.org/licenses/LICENSE-2.0)
[![Apache Software Foundation](https://img.shields.io/badge/organization-Apache%20Software%20Foundation-000000.svg?style=flat)](https://apache.org)

> Official Docker images for **Apache CouchDB**, a flexible, document-oriented database with built-in replication, search, and real-time capabilities.

---

## Description

The `apache/couchdb-docker` repository provides **official, production-ready Docker images** for Apache CouchDB across multiple versions and configurations. These images are designed to simplify deployment, enable consistent environments across development, testing, and production, and support both standard CouchDB and enhanced features like **Clouseau** (search engine) and **Nouveau** (secure, lightweight HTTP server).

This project serves as a foundational tool for developers and DevOps engineers who want to run CouchDB in containers without managing complex system dependencies or configuration. It supports multiple architectures (x86_64, ARM64, S390x), integrates with OpenShift, and provides secure, configurable deployment options.

---

## Features

- ✅ **Multiple Version Support**: Available for CouchDB 2.3.1, 3.1.2, 3.2.3, 3.3.3, 3.4.1–3.5.1.
- ✅ **Multi-Architecture Builds**: Supports Linux x86_64, ARM64, and S390x via `docker buildx`.
- ✅ **OpenShift-Ready**: Includes OpenShift-specific labels and resource constraints (CPU, memory).
- ✅ **Secure by Default**: Enforces admin authentication in CouchDB 3.0+; disables default "Admin Party" mode.
- ✅ **Flexible Configuration**: Custom settings via environment variables (`COUCHDB_USER`, `COUCHDB_PASSWORD`, `COUCHDB_SECRET`, `NODENAME`, `COUCHDB_ERLANG_COOKIE`).
- ✅ **Clouseau Support**: Enhanced search capabilities with full-text indexing via `3.1.2-ubi-clouseau` image.
- ✅ **Nouveau Mode**: Lightweight, secure HTTP server with H2C support (3.5.1+).
- ✅ **Easy Setup**: Simple `docker run` commands with minimal configuration.
- ✅ **Volume Persistence**: Data directory is persisted via `VOLUME /opt/couchdb/data`.

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

- **Docker** (Docker Desktop, Docker Engine, or Docker Compose)
- **Docker Buildx** (for multi-architecture builds)
- **Linux** or **macOS** (with Docker support)
- **Basic knowledge of Docker commands** (`docker run`, `docker build`, `docker pull`)

> **Note**: No additional software or system-level dependencies are required beyond Docker.

---

## Installation

### 1. Pull a CouchDB Image

Pull the latest stable version from the official Apache registry:

```bash
docker pull apache/couchdb:3.5.1
```

Or pull a specific version:

```bash
docker pull apache/couchdb:3.4.3
```

For OpenShift compatibility:

```bash
docker pull apache/couchdb:3.1.2-ubi
```

For Clouseau (search) support:

```bash
docker pull apache/couchdb:3.1.2-ubi-clouseau
```

For Nouveau (secure HTTP) mode:

```bash
docker pull apache/couchdb:3.5.1-nouveau
```

> **Tip**: Use `docker images` to list available tags.

---

### 2. Build Images Locally (Optional)

To build images from source, use the `build.sh` script:

```bash
# Build all platforms for version 3.5.1
./build.sh buildx 3.5.1

# Build and tag as "latest"
./build.sh buildx 3.5.1 as latest

# Clean all local images
./build.sh clean *3.5.1*
```

> The script supports multi-platform builds (x86_64, ARM64, S390x) and can be used to build custom or experimental versions.

---

## Usage

### 1. Run CouchDB with Default Settings

```bash
docker run -d -p 5984:5984 apache/couchdb:3.5.1
```

This starts CouchDB on port `5984` and exposes the default HTTP interface.

---

### 2. Run with Admin Credentials

```bash
docker run -d -p 5984:5984 \
  --env COUCHDB_USER=admin \
  --env COUCHDB_PASSWORD=secret \
  apache/couchdb:3.5.1
```

> This creates an admin user with password `secret`. The database is now secured.

---

### 3. Run with Custom Node Name

```bash
docker run -d -p 5984:5984 \
  --env NODENAME=my-node \
  apache/couchdb:3.5.1
```

> This sets the node name to `my-node`, useful for distributed clusters.

---

### 4. Run Clouseau (Search) with CouchDB

```bash
docker run -d -p 5984:5984 -p 5988:5988 \
  --env NODENAME=my-node \
  apache/couchdb:3.1.2-ubi-clouseau
```

> Clouseau runs as a separate process and provides full-text search capabilities.

---

### 5. Run Nouveau Mode (Secure HTTP)

```bash
docker run -d -p 5987:5987 -p 5988:5988 \
  --env COUCHDB_USER=admin \
  --env COUCHDB_PASSWORD=secret \
  apache/couchdb:3.5.1-nouveau
```

> Uses a secure, H2C-based HTTP server (default port 5987) with admin authentication.

---

### 6. Mount Data Volume (Persistent Storage)

```bash
docker run -d -p 5984:5984 \
  -v /host/path/to/couchdb-data:/opt/couchdb/data \
  apache/couchdb:3.5.1
```

> Data persists across container restarts.

---

## Contributing

We welcome contributions from the community! Please follow these guidelines:

- Open issues or feature requests on [GitHub Issues](https://github.com/apache/couchdb-docker/issues).
- Submit pull requests for bug fixes, new features, or documentation improvements.
- Ensure all changes are tested and aligned with the Apache license.
- Follow the project's code style and documentation standards.

> **Note**: All contributions are subject to Apache License 2.0 and the Apache Software Foundation's review process.

For detailed contribution guidelines, refer to the [CONTRIBUTING.md](https://github.com/apache/couchdb-docker/blob/main/CONTRIBUTING.md) file (if available).

---

## License

This project is licensed under the **Apache License, Version 2.0**.

> See the [LICENSE](https://github.com/apache/couchdb-docker/blob/main/LICENSE) file for details.

---

## Contact / Authors

- **Project Maintainers**: Apache CouchDB Developers (`dev@couchdb.apache.org`)
- **Project Home**: [https://github.com/apache/couchdb-docker](https://github.com/apache/couchdb-docker)
- **Documentation**: [https://couchdb.apache.org](https://couchdb.apache.org)
- **Community**: Join the [Apache CouchDB mailing lists](https://lists.apache.org/list.html?cocb) or [Discord](https://discord.gg/your-link) for support.

> For questions, bug reports, or feature requests, please open an issue on GitHub.

---

> 📚 **Learn More**:  
> - [Apache CouchDB Documentation](https://couchdb.apache.org)  
> - [Docker Documentation](https://docs.docker.com)  
> - [OpenShift Documentation](https://docs.openshift.com)  
> - [Clouseau Project](https://github.com/cloudant/clouseau)  

> ⚠️ **Security Note**: Never expose CouchDB without authentication in production. Always use `COUCHDB_USER` and `COUCHDB_PASSWORD` in production environments.