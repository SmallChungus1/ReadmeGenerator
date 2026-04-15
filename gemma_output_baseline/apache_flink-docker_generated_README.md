# Apache Flink Docker Images

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Description

This repository provides Docker images for Apache Flink, built and maintained by the Apache Flink community. It offers pre-built images for various Flink versions, Scala versions, and Java runtimes, making it easy to quickly get started with Flink without the need for manual installation and configuration.

## Features

*   **Multiple Flink Versions:** Supports Flink versions 1.20, 2.0, 2.1, and 2.2.
*   **Scala and Java Compatibility:** Provides images with Scala 2.12 and varying Java versions (8, 11, 17, and 21).
*   **Automated Builds:** Uses GitHub Actions for automated builds and pushes of images to Docker Hub.
*   **Multi-Architecture Support:**  Images are built for both `amd64` and `arm64/v8` architectures.
*   **Pre-configured Environment:**  Images come with Flink pre-installed and configured, minimizing setup effort.
*   **Snapshot Builds:** Includes nightly snapshot builds for testing and experimentation.

## Installation

To use these images, you simply need to have Docker installed on your system. You can then pull the images from Docker Hub using the following format:

```bash
docker pull apache/flink:<tag>
```

Replace `<tag>` with the desired tag, for example:

*   `apache/flink:2.2.0-scala_2.12-java11` (Flink 2.2.0 with Scala 2.12 and Java 11)
*   `apache/flink:latest` (Most recent stable release)

## Usage

Once you have pulled the image, you can use it to run Flink jobs.  Here are some common examples:

*   **Run JobManager in standalone mode:**

    ```bash
    docker run -d --name flink-jobmanager apache/flink:2.2.0-scala_2.12-java11 standalone-job
    ```

*   **Run TaskManager:**

    ```bash
    docker run -d --name flink-taskmanager --link flink-jobmanager apache/flink:2.2.0-scala_2.12-java11 taskmanager
    ```

*   **Access Flink Web UI:**

    Once the JobManager is running, you can access the Flink web UI at `http://localhost:8081`.

Refer to the official Flink documentation for more details on running Flink jobs: [https://flink.apache.org/docs/](https://flink.apache.org/docs/)

## Contributing

Contributions are welcome! If you find a bug or want to add support for a new Flink version or Java runtime, please submit a pull request.  See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Workflow

The following GitHub Actions workflows are used to maintain these images:

*   **docker-bake.hcl:** Defines the build targets using Docker Buildx.
*   **snapshot.yml:** Automatically builds and pushes nightly snapshot images.
*   **docker_push.yml:**  Builds and pushes official release images on tagging the repository.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more information.