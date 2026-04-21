# Apache CouchDB Docker Images

## Description

This repository provides Docker images for Apache CouchDB. It includes multiple versions (2.3.1, 3.1.2, 3.2.3, 3.3.3, 3.4.1, 3.4.2, 3.4.3, 3.5.0, 3.5.1) and a Clouseau variant for enhanced performance and scalability. The images are built using Red Hat Universal Base Image (UBI) and leverage the Runit init system for process management.

## Features

*   Multiple CouchDB versions available.
*   Clouseau variant for improved performance and scalability.
*   Red Hat UBI base image for stability and security.
*   Runit init system for process management.
*   Configuration files for customization.
*   Support for multiple architectures (x86\_64, ARM64/v8, s390x).

## Prerequisites / Requirements

*   Docker installed and running.
*   Basic familiarity with Docker concepts.

## Installation

The installation process depends on the specific image you choose. Generally, you can pull the image from Docker Hub:

```bash
docker pull apache/couchdb:<version>
```

Replace `<version>` with the desired version (e.g., `apache/couchdb:2.3.1`, `apache/couchdb:3.5.1-nouveau`).

## Usage

To run a CouchDB instance using the Docker image:

```bash
docker run -d -p 5984:5984 -p 4369:4369 apache/couchdb:<version>
```

*   `-d`: Runs the container in detached mode (in the background).
*   `-p 5984:5984`: Maps port 5984 on the host to port 5984 in the container (CouchDB's default HTTP port).
*   `-p 4369:4369`: Maps port 4369 on the host to port 4369 in the container (Erlang portmap daemon).
*   `apache/couchdb:<version>`: Specifies the image to use.

To run the Clouseau variant:

```bash
docker run -d -p 5984:5984 -p 4369:4369 apache/couchdb:3.1.2-ubi-clouseau
```

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to contribute.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.