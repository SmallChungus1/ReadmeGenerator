# Apache CouchDB Docker Images

## Description
This repository provides Docker images for Apache CouchDB, a NoSQL document database. The images are built for various versions of CouchDB and support different base operating systems, including Debian and Red Hat Universal Base Image (UBI). The images include pre-configured settings for running CouchDB in containerized environments with support for authentication, node naming, and secure configurations.

## Features
- Docker images for multiple CouchDB versions (2.3.1, 3.1.2, 3.2.3, 3.3.3, 3.4.1, 3.4.2, 3.4.3, 3.5.0, 3.5.1)
- Support for Red Hat UBI and Debian base images
- Built-in configuration for secure authentication and node naming
- Automatic handling of file permissions and ownership
- Support for distributed CouchDB clusters via Clouseau (search functionality)
- Customizable runtime configuration through environment variables
- Pre-configured logging and performance settings for production use

## Prerequisites / Requirements
- Docker or Docker Desktop installed
- Basic knowledge of Docker commands
- Access to a container runtime environment

## Installation
To build and use the images, follow these steps:

### Build a specific version
```bash
# Build the latest version of CouchDB 3.5.1
docker buildx build --platform linux/amd64,linux/arm64/v8 --tag apache/couchdb:3.5.1 .

# Build with a custom tag
docker buildx build --platform linux/amd64,linux/arm64/v8 --tag apache/couchdb:latest --tag apache/couchdb:3.5.1 .
```

### Build with UBI base image
```bash
# Build for Red Hat UBI
docker buildx build --platform linux/amd64,linux/arm64/v8 --tag apache/couchdb:2.3.1-ubi .
```

### Build with Clouseau support
```bash
# Build with Clouseau (search) support
docker buildx build --platform linux/amd64,linux/arm64/v8 --tag apache/couchdb:3.1.2-ubi-clouseau .
```

## Usage
### Run CouchDB container with basic configuration
```bash
# Run with default settings
docker run -d -p 5984:5984 apache/couchdb:3.5.1

# Run with admin credentials
docker run -d -p 5984:5984 \
  -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=password \
  apache/couchdb:3.5.1
```

### Run with custom node name
```bash
# Specify a custom node name
docker run -d -p 5984:5984 \
  -e NODENAME=my-node \
  apache/couchdb:3.5.1
```

### Run with Clouseau (search) support
```bash
# Run with search capabilities
docker run -d -p 5984:5984 -p 5988:5988 \
  -e NODENAME=my-node \
  apache/couchdb:3.1.2-ubi-clouseau
```

### Access the database
After starting the container, access the CouchDB web interface at `http://localhost:5984`.

## Contributing
Contributions are welcome. Please follow these guidelines:
1. Fork the repository
2. Create a feature branch
3. Commit your changes with descriptive messages
4. Push to the branch and open a pull request

For changes to the Dockerfiles or configuration, ensure they maintain backward compatibility and follow the existing code style.

## License
This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.

## Contact / Authors
Project maintained by the Apache CouchDB team. For questions or feedback, contact:
- dev@couchdb.apache.org
- See the [Apache CouchDB project page](https://couchdb.apache.org/) for more information.