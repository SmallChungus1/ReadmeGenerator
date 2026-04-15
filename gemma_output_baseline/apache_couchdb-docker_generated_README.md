# Apache CouchDB Docker Images

This repository provides Docker images for Apache CouchDB, a distributed, schemaless document database designed for scalability and usability. These images are maintained by the Apache CouchDB project and offer a convenient way to deploy and run CouchDB in containerized environments.

## Description

These Docker images provide pre-configured environments for running Apache CouchDB. They are designed to be easily integrated into various deployment workflows, including local development, testing, and production environments. The repository offers images based on different base images (Debian, UBI) and with/without Clouseau integration.

## Features

*   **Multiple Base Images:** Images are provided based on Debian and Red Hat Universal Base Image (UBI) for flexibility.
*   **Pre-configured:** Images come with CouchDB pre-installed and configured for basic usage.
*   **Clouseau Integration:**  Some images include Clouseau, a full-text search engine for CouchDB.
*   **Versioned Images:**  Images are tagged with CouchDB versions for easy selection and reproducibility.
*   **Docker Hub Availability:** Images are available on Docker Hub for easy pull and use.
*   **Automated Builds:** Images are automatically built and updated with new CouchDB releases.

## Table of Contents

*   [Prerequisites / Requirements](#prerequisites--requirements)
*   [Installation](#installation)
*   [Usage](#usage)
*   [Contributing](#contributing)
*   [License](#license)
*   [Contact / Authors](#contact--authors)

## Prerequisites / Requirements

*   Docker installed and configured on your system.
*   Docker Compose (optional, for more complex deployments).

## Installation

To pull a CouchDB Docker image, use the `docker pull` command. For example, to pull the latest 2.3.1 image:

```bash
docker pull apache/couchdb:2.3.1
```

To pull a specific version with UBI base image:

```bash
docker pull apache/couchdb:3.1.2-ubi
```

To pull a version with Clouseau integration:

```bash
docker pull apache/couchdb:3.1.2-ubi-clouseau
```

## Usage

To run a CouchDB instance, use the `docker run` command.  Here's a basic example:

```bash
docker run -d -p 5984:5984 apache/couchdb:2.3.1
```

This command will:

*   `-d`: Run the container in detached mode (background).
*   `-p 5984:5984`: Map port 5984 on the host machine to port 5984 inside the container (CouchDB's default HTTP port).
*   `apache/couchdb:2.3.1`:  Specify the image to use.

You can then access CouchDB in your browser at `http://localhost:5984`.

**Environment Variables:**

You can configure CouchDB using environment variables:

*   `COUCHDB_USER`: Sets the username for the admin user.
*   `COUCHDB_PASSWORD`: Sets the password for the admin user.
*   `COUCHDB_ERLANG_COOKIE`: Sets the Erlang cookie for clustering.

Example:

```bash
docker run -d -p 5984:5984 -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=password apache/couchdb:2.3.1
```

## Contributing

Contributions are welcome! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contact / Authors

This project is maintained by the Apache CouchDB community. You can find more information and get involved at:

*   [Apache CouchDB Website](https://couchdb.apache.org/)
*   [GitHub Repository](https://github.com/apache/couchdb-docker)