# Apache Flink Docker Packaging

This repository provides Docker images for Apache Flink.

## Description

This project packages Apache Flink in Docker containers, making it easier to deploy and run Flink applications.  It includes images for various Flink versions and Java runtimes.

## Features

*   Docker images for multiple Flink versions (1.20, 2.0, 2.1, 2.2).
*   Support for different Java runtimes (Scala 2.12, Java 11, Java 17, Java 21).
*   Pre-configured environment for running Flink.
*   Simplified deployment process.

## Prerequisites / Requirements

*   Docker installed and running.
*   Docker Hub account (required for publishing images).

## Installation

1.  Pull the desired Docker image from Docker Hub:

    ```bash
    docker pull apache/flink:<version>-scala_<scala_version>-java<java_version>
    ```

    Replace `<version>`, `<scala_version>`, and `<java_version>` with the appropriate values (e.g., `apache/flink:2.2-scala_2.12-java17`).

## Usage

1.  Run the Flink container:

    ```bash
    docker run -d -p 6123:6123 -p 8081:8081 apache/flink:<version>-scala_<scala_version>-java<java_version>
    ```

    *   `-d`: Runs the container in detached mode (background).
    *   `-p 6123:6123`: Maps port 6123 on the host to port 6123 in the container (Flink web UI).
    *   `-p 8081:8081`: Maps port 8081 on the host to port 8081 in the container (Flink REST API).
    *   `apache/flink:<version>-scala_<scala_version>-java<java_version>`: The name of the Docker image to run.

2.  Access the Flink web UI:

    Open a web browser and navigate to `http://localhost:6123`.

3.  Access the Flink REST API:

    Open a tool like `curl` or Postman to access the Flink REST API at `http://localhost:8081`.

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for details.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.

## Contact / Authors

Apache Software Foundation