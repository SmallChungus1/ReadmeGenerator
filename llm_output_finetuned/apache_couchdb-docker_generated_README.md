# Apache CouchDB Docker Images

## Description

The Apache CouchDB Docker images provide a collection of pre-built, containerized environments for running Apache CouchDB, a NoSQL document database. This repository contains multiple versions of CouchDB (from 2.3.1 to 3.5.1) packaged as Docker images, supporting various architectures and deployment scenarios including standard, Red Hat UBI-based, and Clouseau (search) enabled configurations.

The images are designed for ease of use in development, testing, and production environments, offering built-in security features, proper ownership and permission management, and support for container orchestration platforms like Kubernetes and OpenShift.

## Features

- **Multiple CouchDB Versions**: Supports versions from 2.3.1 to 3.5.1, with regular updates and security patches.
- **Architecture Support**: Available for x86_64, ARM64, and other architectures via multi-arch builds.
- **Red Hat UBI Compatibility**: UBI-based images optimized for OpenShift and RHEL environments.
- **Security by Default**: Enforces secure configurations including admin authentication and restricted access.
- **Flexible Configuration**: Customizable via environment variables for admin credentials, node names, and authentication secrets.
- **Clouseau Search Support**: Specialized images with integrated full-text search capabilities.
- **Nouveau Mode**: Optimized configuration for high-performance, low-latency scenarios with alternative HTTP endpoints.
- **Automatic Ownership & Permissions**: Ensures proper file ownership and permissions for secure operation.
- **Graceful Shutdown**: Support for graceful process termination in cluster environments.
- **Multi-Platform Builds**: Automated builds for all supported architectures using Docker Buildx.

## Installation

To use the Apache CouchDB Docker images, you must first ensure Docker is installed on your system. The images are available on Docker Hub and can be pulled directly.

### Pulling the Image

```bash
docker pull apache/couchdb:<version>
```

Replace `<version>` with the desired CouchDB version (e.g., `3.5.1`, `3.4.3`, or `2.3.1`).

### Pulling UBI-Based Images

For OpenShift or RHEL-based environments:

```bash
docker pull apache/couchdb:<version>-ubi
```

### Pulling Clouseau-Enabled Images

For environments requiring full-text search capabilities:

```bash
docker pull apache/couchdb:<version>-ubi-clouseau
```

### Pulling Nouveau Mode Images

For high-performance, optimized deployments:

```bash
docker pull apache/couchdb:<version>-nouveau
```

### Build from Source (Optional)

To build images locally, use the provided `build.sh` script:

```bash
# Build all platforms for a specific version
./build.sh buildx 3.5.1

# Build and tag with a custom name
./build.sh buildx 3.5.1 as latest
```

## Usage

### Basic Usage

Start a CouchDB container with default settings:

```bash
docker run -d -p 5984:5984 apache/couchdb:3.5.1
```

This exposes the CouchDB HTTP API on port 5984.

### With Custom Admin Credentials

```bash
docker run -d -p 5984:5984 \
  -e COUCHDB_USER=admin \
  -e COUCHDB_PASSWORD=secret \
  apache/couchdb:3.5.1
```

### With Custom Node Name

```bash
docker run -d -p 5984:5984 \
  -e NODENAME=my-couch-node \
  apache/couchdb:3.5.1
```

### With Authentication Secret

```bash
docker run -d -p 5984:5984 \
  -e COUCHDB_SECRET=your-secret-key \
  apache/couchdb:3.5.1
```

### Using Clouseau Search

```bash
docker run -d -p 5984:5984 \
  -e NODENAME=my-search-node \
  apache/couchdb:3.5.1-ubi-clouseau
```

### Using Nouveau Mode

```bash
docker run -d -p 5987:5987 \
  -e COUCHDB_USER=admin \
  -e COUCHDB_PASSWORD=secret \
  apache/couchdb:3.5.1-nouveau
```

### Accessing the Database

Once running, access the CouchDB REST API at `http://localhost:5984`. Authentication is required for all operations unless admin credentials are provided.

### Environment Variables

| Variable | Description |
|---------|-------------|
| `COUCHDB_USER` | Admin username |
| `COUCHDB_PASSWORD` | Admin password |
| `COUCHDB_SECRET` | HTTP authentication secret |
| `NODENAME` | Node name for distributed clusters |
| `COUCHDB_ERLANG_COOKIE` | Erlang cookie for distributed nodes |

> **Note**: Starting with CouchDB 3.0+, "Admin Party" mode (no admin user) is disabled by default. You **must** provide an admin user and password via environment variables or configuration files.

### Volume Mounting

Mount a persistent data directory:

```bash
docker run -d -p 5984:5984 \
  -v /host/data:/opt/couchdb/data \
  apache/couchdb:3.5.1
```

This ensures data persists across container restarts.