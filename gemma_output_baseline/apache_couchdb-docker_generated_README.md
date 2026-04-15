# Apache CouchDB Docker Images

[![Build Status](https://ci-builds.apache.org/job/CouchDB-Docker/job/main/badge/)]()

This repository provides Docker images for Apache CouchDB. It supports a variety of versions and base images to suit different needs.

## Description

These images are designed to provide a convenient and reproducible way to run Apache CouchDB in a containerized environment.  They are based on Debian and UBI base images for compatibility and ease of use.  The images are built and maintained by the Apache CouchDB community.

## Features

*   **Multiple Versions:** Contains images for various CouchDB versions (2.3.1, 3.1.2, 3.2.3, 3.3.3, 3.4.1, 3.4.2, 3.4.3, 3.5.0, 3.5.1), providing flexibility for different application requirements.
*   **Base Image Options:** Offers images based on Debian and Red Hat's Universal Base Image (UBI).
*   **Optimized for Docker:** Images are configured specifically for running CouchDB within a Docker container.
*   **Automated Builds:**  Automated CI builds are provided for continuous integration and testing.
*   **Clouseau Integration:** Includes images with pre-integrated Clouseau support (e.g., 3.1.2-ubi-clouseau, 3.4.1-nouveau, 3.4.2-nouveau, 3.4.3-nouveau, 3.5.0-nouveau, 3.5.1-nouveau).
*   **Nouveau Support:** Includes specific images containing Nouveau integration.

## Installation

To use these images, you need to have Docker installed on your system.  Instructions for installing Docker can be found on the official Docker website: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

After installing Docker, you can pull an image using the `docker pull` command. For example:

```bash
docker pull apache/couchdb:3.4.3
```

## Usage

Once you have pulled an image, you can run it using the `docker run` command. Here's an example:

```bash
docker run -d -p 5984:5984 --name my-couchdb apache/couchdb:3.4.3
```

This command will:

*   `-d`: Run the container in detached mode (in the background).
*   `-p 5984:5984`: Map port 5984 on the host machine to port 5984 in the container (CouchDB's default port).
*   `--name my-couchdb`:  Assign a name to the container.
*  `apache/couchdb:3.4.3`: Specifies the image to use.

To access the CouchDB web interface, open your web browser and navigate to `http://localhost:5984`.

### Environment Variables

The following environment variables can be used to configure the CouchDB container:

*   `COUCHDB_USER`:  The admin username.
*   `COUCHDB_PASSWORD`: The admin password.
*   `COUCHDB_SECRET`:  The secret for HTTP authentication.
*   `COUCHDB_ERLANG_COOKIE`: Set the Erlang cookie.
*   `NODENAME`: Set name for CouchDB instance.

### Example with Environment Variables:

```bash
docker run -d -p 5984:5984 --name my-couchdb \
    -e COUCHDB_USER=admin \
    -e COUCHDB_PASSWORD=password \
    apache/couchdb:3.4.3
```

## Contributing

Contributions to this project are welcome!  Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information.

## License

This project is licensed under the [Apache License 2.0](LICENSE).

## Repository Structure

The repository is organized as follows:

*   `.asf.yaml`: Apache Software Foundation metadata.
*   `.github/`: GitHub configuration files.
*   `.gitignore`: Specifies intentionally untracked files that Docker ignores.
*   `<version>/`:  Directories for each CouchDB version (e.g., `2.3.1`, `3.1.2`).  Each version directory contains the Dockerfile, configuration files, and entrypoint script for that version.
*   `LICENSE`: The Apache License 2.0 file.
*   `build.sh`:  A script for building and publishing the Docker images.
*   `dev/`: Development related files (Dockerfile, entrypoint, configs).
*   `dev-cluster/`: Contains files starting a couchDB cluster.
*   `nouveau-compose`: Contains files for starting a nouveau couchDB cluster.

## Support

For questions, support, or to report issues, please visit the [Apache CouchDB website](https://couchdb.apache.org/) or the [CouchDB mailing lists](https://couchdb.apache.org/community.html).