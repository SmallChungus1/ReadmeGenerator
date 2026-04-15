# Apache CouchDB Docker Images

## Description

The Apache CouchDB Docker images provide a collection of pre-built, containerized environments for running Apache CouchDB, a NoSQL document database. This repository contains Dockerfile configurations for multiple CouchDB versions (2.3.1, 3.1.2, 3.2.3, 3.3.3, 3.4.1, 3.4.2, 3.4.3, 3.5.0, 3.5.1) across different base images, including standard Debian-based and Red Hat UBI (Universal Base Image) variants.

These images are designed for ease of deployment in Docker environments, offering built-in support for container orchestration platforms like Kubernetes and OpenShift. The repository includes specialized configurations for distributed search capabilities (Clouseau) and optimized performance settings for production workloads.

## Features

- **Multiple Version Support**: Pre-built images for CouchDB 2.3.1 through 3.5.1
- **Base Image Flexibility**: Available in both Debian-based and Red Hat UBI (Universal Base Image) variants
- **Distributed Search Support**: Specialized `3.1.2-ubi-clouseau` images with Clouseau search engine integration
- **Performance Optimization**: Configurations with enhanced IO scheduling, distribution buffer sizes, and CPU scheduling for containerized environments
- **Security Enhancements**: Default logging suppression, restricted file permissions, and mandatory admin authentication enforcement (3.0+)
- **Customizable Configuration**: Support for setting admin credentials, authentication secrets, and node names via environment variables
- **Automatic Permission Management**: Scripts automatically fix ownership and permissions for data and configuration directories
- **Graceful Shutdown**: Enhanced `pre_stop` scripts for proper process termination in distributed setups
- **Multi-Architecture Support**: Build scripts support building for multiple architectures (amd64, arm64, s390x)

## Installation

To install and use the Apache CouchDB Docker images, follow these steps:

```bash
# Pull a specific version of the CouchDB image
docker pull apache/couchdb:3.5.1

# Pull the UBI-based version
docker pull apache/couchdb:3.5.1-ubi

# Pull the Clouseau search-enabled version
docker pull apache/couchdb:3.1.2-ubi-clouseau
```

For building images from source, use the provided `build.sh` script:

```bash
# Build all platforms for a specific version
./build.sh buildx 3.5.1

# Build and tag with a custom name
./build.sh buildx 3.5.1 as latest
```

## Usage

### Basic Usage with Admin Credentials

```bash
# Start CouchDB with admin user and password
docker run -d \
  --name couchdb \
  -e COUCHDB_USER=admin \
  -e COUCHDB_PASSWORD=secret \
  -p 5984:5984 \
  apache/couchdb:3.5.1
```

### Using with Custom Configuration

```bash
# Mount a custom configuration file
docker run -d \
  --name couchdb \
  -v /host/config:/opt/couchdb/etc \
  -p 5984:5984 \
  apache/couchdb:3.5.1
```

### Starting Clouseau Search Service

```bash
# Start with Clouseau search enabled
docker run -d \
  --name couchdb \
  -e COUCHDB_USER=admin \
  -e COUCHDB_PASSWORD=secret \
  -p 5984:5984 \
  -p 5988:5988 \
  apache/couchdb:3.1.2-ubi-clouseau
```

### Using Environment Variables for Node Configuration

```bash
# Set a custom node name
docker run -d \
  --name couchdb \
  -e NODENAME=my-node \
  -e COUCHDB_USER=admin \
  -e COUCHDB_PASSWORD=secret \
  -p 5984:5984 \
  apache/couchdb:3.5.1
```

### Accessing the Admin Interface

After starting the container, access the CouchDB web interface at `http://localhost:5984` with the provided admin credentials.

> **Note**: Starting with CouchDB 3.0+, the "Admin Party" mode (where no admin credentials are required) has been deprecated. All versions require explicit admin credentials to be set via environment variables or configuration files.