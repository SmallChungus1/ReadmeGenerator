# Apache CouchDB Docker Images

![Build Status](https://github.com/apache/couchdb-docker/workflows/Build/badge.svg)
![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)

A collection of semi-official Docker images for Apache CouchDB, providing pre-built, production-ready containers for easy deployment across various environments including Docker, Kubernetes, and OpenShift.

---

## Description

Apache CouchDB is a document-oriented, distributed database that runs on top of the Erlang/OTP platform. This repository provides Docker images for Apache CouchDB across multiple versions, enabling developers and operations teams to deploy, manage, and scale CouchDB with minimal configuration.

The images are designed to be lightweight, secure, and compatible with container orchestration platforms. Each version includes pre-configured settings, proper user permissions, and support for common deployment patterns such as distributed clusters and search functionality via Clouseau.

This project is maintained by the Apache CouchDB community and is intended to serve as a reliable, standardized way to run CouchDB in containerized environments.

---

## Features

- ✅ **Multiple Versions**: Support for CouchDB 2.3.1, 3.1.2, 3.2.3, 3.3.3, 3.4.1, 3.4.2, 3.4.3, 3.5.0, and 3.5.1.
- 🚀 **Multi-Architecture Support**: Builds for `amd64`, `arm64`, and `s390x` platforms via Docker Buildx.
- 🔐 **Security by Default**: Runs as a non-root user (`couchdb`) with restricted permissions and secure default configurations.
- 🔍 **Admin Access Enforcement**: Starting from CouchDB 3.0+, admin access is required. Running in "Admin Party" mode is explicitly blocked with clear warnings.
- 📦 **Flexible Configuration**: Custom settings can be applied via environment variables or mounted configuration files.
- 🌐 **Distributed Support**: Includes support for clustering via `NODENAME` and `ERL_FLAGS` environment variables.
- 🔎 **Search Engine (Clouseau)**: Optional Clouseau search engine included in specific versions (e.g., `3.1.2-ubi-clouseau`).
- 📝 **Easy Setup**: Simple `docker run` commands with optional environment variables for authentication and node naming.
- 📦 **Open Source & Apache Licensed**: Fully open source under the Apache License 2.0.

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

To use these Docker images, you need:

- **Docker** (version 18.03 or later) or **Docker Desktop**
- **Docker Compose** (optional, for multi-container setups)
- A modern operating system (Linux, macOS, or Windows with Docker support)

No additional software or dependencies are required beyond Docker.

---

## Installation

The images are available on Docker Hub at `apache/couchdb`.

### 1. Pull a Version

```bash
docker pull apache/couchdb:3.5.1
```

> Replace `3.5.1` with any version listed in the repository (e.g., `2.3.1`, `3.4.2`, `3.5.0-nouveau`).

### 2. Run the Container

```bash
docker run -d \
  --name couchdb \
  -p 5984:5984 \
  -e COUCHDB_USER=admin \
  -e COUCHDB_PASSWORD=password \
  apache/couchdb:3.5.1
```

> This starts a CouchDB instance with an admin user and password.

### 3. Optional: Use with Docker Compose

Create a `docker-compose.yml` file:

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
```

Then start with:

```bash
docker-compose up -d
```

---

## Usage

### Basic Operations

Once running, you can interact with the CouchDB instance via HTTP:

- **Access the web interface**: `http://localhost:5984/_utils`
- **Query databases**: `GET /_all_dbs`
- **Create a database**: `POST /mydb`

### Environment Variables

| Variable | Purpose |
|--------|--------|
| `COUCHDB_USER` | Username for admin access |
| `COUCHDB_PASSWORD` | Password for admin access |
| `COUCHDB_SECRET` | Authentication secret for HTTP access |
| `NODENAME` | Node name for distributed clusters (e.g., `couchdb@mycluster`) |
| `ERL_FLAGS` | Additional Erlang VM flags (e.g., `-setcookie mycookie`) |
| `COUCHDB_ERLANG_COOKIE` | Sets the Erlang cookie for cluster communication |

> ⚠️ **Important**: Starting from CouchDB 3.0+, **admin access is mandatory**. Running without a user/password will result in an error and exit.

### Clouseau Search (Optional)

The `3.1.2-ubi-clouseau` image includes Clouseau, a full-text search engine for CouchDB. To use it:

```bash
docker run -d \
  --name couchdb-search \
  -p 5988:5988 \
  -e COUCHDB_USER=admin \
  -e COUCHDB_PASSWORD=password \
  apache/couchdb:3.1.2-ubi-clouseau
```

> Clouseau runs on port 5988 and can be accessed at `http://localhost:5988/_utils`.

---

## Contributing

We welcome contributions to improve the stability, security, and usability of these Docker images.

### How to Contribute

1. **Fork the repository** on GitHub.
2. **Create a new branch** for your feature or bug fix.
3. **Submit a pull request** with a clear description of your changes.

### Reporting Issues

If you encounter a bug or have a feature request, please open an issue in the [GitHub Issues](https://github.com/apache/couchdb-docker/issues) section.

### Code of Conduct

We follow the [Apache Code of Conduct](https://www.apache.org/foundation/policies/conduct) and encourage respectful, inclusive discussions.

---

## License

This project is licensed under the **Apache License, Version 2.0**.

See the [LICENSE](LICENSE) file for details.

---

## Contact / Authors

- **Project Maintainers**: Apache CouchDB Developers (`dev@couchdb.apache.org`)
- **GitHub Repository**: [https://github.com/apache/couchdb-docker](https://github.com/apache/couchdb-docker)
- **Documentation**: [https://docs.couchdb.org](https://docs.couchdb.org)
- **Community Forum**: [https://couchdb.apache.org/community](https://couchdb.apache.org/community)

For questions or feedback, please reach out to the project maintainers or join the community discussions.