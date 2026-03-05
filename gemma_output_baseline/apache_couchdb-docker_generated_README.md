# Apache CouchDB Docker Images

This repository provides official Docker images for Apache CouchDB. These images are designed to simplify the deployment and management of CouchDB in containerized environments.

## Description

Apache CouchDB is a powerful, open-source NoSQL database known for its document-oriented storage model, ease of use, and robust replication capabilities. These Docker images provide a pre-configured and easily deployable environment for running CouchDB.

## Features

* **Multiple Versions:** Images are provided for various CouchDB versions (e.g., 2.3.1, 3.1.2, 3.2.3, 3.3.3, 3.4.1, 3.4.2, 3.4.3, 3.5.0, 3.5.1).
* **Base Images:**  Based on Debian and RedHat UBI providing a consistent and secure base.
* **Pre-configured:** Images come with sensible defaults for ease of use.
* **User Management:** Dedicated `couchdb` user for security.
* **RunIt Integration:**  Images utilize `runit` for process management.
* **Nouveau Support:** Dedicated images with CouchDB Nouveau, the newer approach for full-text indexing and querying.
* **Clouseau Support:** Images that include Clouseau, a full-text search indexer.
* **Official Images:** Provided and maintained by the Apache CouchDB project.

## Installation

1. **Docker:**  Ensure Docker is installed on your system.  Refer to the official Docker documentation for installation instructions: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

2. **Pull the Image:**  Pull the desired CouchDB image from Docker Hub using the `docker pull` command. For example, to pull the 3.4.3 image:

   ```bash
   docker pull apache/couchdb:3.4.3
   ```

   To pull the 3.4.3 Nouveau image:

   ```bash
   docker pull apache/couchdb:3.4.3-nouveau
   ```

## Usage

1. **Run the Container:**

   Run the CouchDB container using the `docker run` command.  This example maps port 5984 (CouchDB's HTTP interface) to your host machine and sets environment variables for the admin user and password.

   ```bash
   docker run -d -p 5984:5984 \
       -e COUCHDB_USER=admin \
       -e COUCHDB_PASSWORD=password \
       apache/couchdb:3.4.3
   ```
   Replace `3.4.3` with the desired CouchDB version.

2. **Access CouchDB:**

   Open your web browser and navigate to `http://localhost:5984/`. You should see the CouchDB welcome page.  Login using the `admin` user and `password` you set in the `docker run` command.

3. **Environment Variables:**

   *   `COUCHDB_USER`:  Username for the CouchDB administrator.
   *   `COUCHDB_PASSWORD`: Password for the CouchDB administrator.
   *   `COUCHDB_ERLANG_COOKIE`: (Advanced) Specify a custom Erlang cookie for secure clustering.
   * `NODENAME`: Specify a node name.

## Available Tags

The following tags are available (not exhaustive, see Docker Hub for a complete list):

*   `2.3.1`
*   `3.1.2`
*   `3.2.3`
*   `3.3.3`
*   `3.4.1`
*   `3.4.2`
*   `3.4.3`
*   `3.5.0`
*   `3.5.1`
*   `-nouveau`:  Appended to the version number to indicate the Nouveau image.
*   `-ubi`: Appended to the version number to indicate a UBI based image.
*   `-ubi-clouseau`: Appended to the version number to indicate a UBI image with Clouseau included.

## Configuration

The Docker images provide a default configuration. You can customize the configuration by mounting a custom `local.ini` file into the `/opt/couchdb/etc/local.d/` directory within the container. Any settings in `local.ini` will override the default values. For advanced configuration, explore the official CouchDB documentation.

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file in the repository for information on how to contribute.

## License

This project is licensed under the [Apache License 2.0](LICENSE).

## Resources

*   **Apache CouchDB Website:** [http://couchdb.apache.org/](http://couchdb.apache.org/)
*   **Docker Hub:** [https://hub.docker.com/r/apache/couchdb](https://hub.docker.com/r/apache/couchdb)
*   **GitHub Repository:** [https://github.com/apache/couchdb-docker](https://github.com/apache/couchdb-docker)
```