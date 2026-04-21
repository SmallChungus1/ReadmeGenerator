# Apache CouchDB Docker Images

## Description

This repository provides Docker images for Apache CouchDB, including various versions and configurations. The images are designed to run CouchDB in containerized environments and support multiple deployment scenarios including standard CouchDB, with Clouseau search functionality, and optimized builds for specific platforms.

The repository contains Dockerfiles for different CouchDB versions (2.3.1, 3.1.2, 3.2.3, 3.3.3, 3.4.1, 3.4.2, 3.4.3, 3.5.0, 3.5.1) and includes both standard and UBI (Universal Base Image) variants. It also provides a "nouveau" configuration for optimized performance and a development environment.

## Features

- Docker images for Apache CouchDB versions 2.3.1 through 3.5.1
- UBI-based images for Red Hat OpenShift compatibility
- Support for Clouseau search functionality (3.1.2-ubi-clouseau variant)
- Optimized "nouveau" configuration with improved performance settings
- Development environment for local testing
- Multi-architecture builds via `build.sh`
- Configuration files for custom settings including bind addresses and authentication
- Environment variable support for setting admin credentials, secrets, and node names
- Proper ownership and permission management for data and configuration directories

## Prerequisites / Requirements

- Docker or Docker Desktop
- A container runtime environment (Docker Engine, Podman, or similar)
- Access to the internet for image downloads (required for package repositories)

## Installation

### Build and Run a Standard CouchDB Image

1. Clone the repository:
   ```bash
   git clone https://github.com/apache/couchdb-docker.git
   cd couchdb-docker
   ```

2. Build a specific version (e.g., 3.5.1):
   ```bash
   ./build.sh buildx 3.5.1
   ```

3. Run the container:
   ```bash
   docker run -d -p 5984:5984 --name couchdb apache/couchdb:3.5.1
   ```

### Build and Run with Custom Configuration

To set up an admin user and password:
```bash
docker run -d -p 5984:5984 --name couchdb \
  -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=secret \
  apache/couchdb:3.5.1
```

### Run with Clouseau Search

For the Clouseau search variant:
```bash
docker run -d -p 5984:5984 --name couchdb \
  apache/couchdb:3.1.2-ubi-clouseau
```

### Run with Nouveau Configuration

For optimized performance:
```bash
docker run -d -p 5987:5987 --name couchdb-nouveau \
  apache/couchdb:3.4.1-nouveau
```

## Usage

### Accessing the CouchDB Interface

After starting the container, access the CouchDB web interface at `http://localhost:5984`.

### Environment Variables

- `COUCHDB_USER`: Admin username (required for versions 3.0+)
- `COUCHDB_PASSWORD`: Admin password (required for versions 3.0+)
- `COUCHDB_SECRET`: HTTP authentication secret (optional)
- `NODENAME`: Node name for distributed clusters (optional)
- `COUCHDB_ERLANG_COOKIE`: Erlang cookie for distributed nodes (optional)

### Configuration Files

Custom settings can be added to the `10-docker-default.ini` file in the container's configuration directory. This file will override default settings and is not overwritten during upgrades.

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository on GitHub
2. Create a new branch for your feature or bug fix
3. Commit your changes with clear, descriptive messages
4. Push to your fork and open a pull request

The repository uses a pull request workflow with a single required reviewer. All changes must be reviewed and approved before merging.

## License

This project is licensed under the Apache License, Version 2.0. See the LICENSE file for details.

## Contact / Authors

For questions or issues, contact the CouchDB developers at `dev@couchdb.apache.org`.

The repository is maintained by the Apache CouchDB community.