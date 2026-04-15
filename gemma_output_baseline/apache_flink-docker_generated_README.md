```markdown
# Apache Flink Docker Images

This repository provides Docker images for Apache Flink, built and maintained by the Apache Flink project.

## Description

These Docker images offer a convenient and reproducible way to run Apache Flink. They are available for various Flink versions, Scala versions, and Java versions, simplifying deployment and ensuring consistency across different environments.  These images are intended for development, testing, and production use.

## Features

*   **Multiple Flink Versions:** Images are provided for Flink versions 1.20, 2.0, 2.1, and 2.2.
*   **Multiple Java Versions:** Support for Java 8, 11, 17, and 21.
*   **Scala 2.12 Support:** All images are built with Scala 2.12.
*   **Ubuntu Base Images:**  Images are based on Ubuntu, providing a familiar and well-supported environment.
*   **Pre-configured:** Images come with Flink pre-installed and configured, ready to run.
*   **Multi-Architecture Support:** Images are built for `amd64` and `arm64v8` architectures.

## Table of Contents

*   [Prerequisites / Requirements](#prerequisites--requirements)
*   [Installation](#installation)
*   [Usage](#usage)
*   [Contributing](#contributing)
*   [License](#license)
*   [Contact / Authors](#contact--authors)

## Prerequisites / Requirements

*   **Docker:** You need to have Docker installed and configured on your system.  See the official Docker documentation for installation instructions: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
*   **Docker Hub Account (for pushing images):** If you intend to build and push your own images based on these, you'll need a Docker Hub account.

## Installation

These images are readily available on Docker Hub. You don't need to build them unless you want to customize them.  To pull an image, use the following command:

```bash
docker pull apache/flink:<tag>
```

Replace `<tag>` with the desired tag.  For example:

```bash
docker pull apache/flink:2.2.0-scala_2.12-java11
```

## Usage

Once you've pulled an image, you can run it using `docker run`.  Here are some examples:

**Running in standalone mode:**

```bash
docker run -it --rm apache/flink:2.2.0-scala_2.12-java11 standalone-job
```

**Running a Job Manager:**

```bash
docker run -d --name flink-jobmanager -p 8081:8081 apache/flink:2.2.0-scala_2.12-java11 jobmanager
```

**Running a Task Manager (after starting a Job Manager):**

```bash
docker run --rm --link flink-jobmanager:flink apache/flink:2.2.0-scala_2.12-java11 taskmanager
```

**Note:** Replace `2.2.0-scala_2.12-java11` with the appropriate tag for your desired Flink version, Scala version, and Java version.  The `--link` option is deprecated, consider using Docker networks for better isolation and communication.

## Contributing

Contributions are welcome! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for more information.

## Contact / Authors

This project is maintained by the [Apache Flink community](https://flink.apache.org/). You can reach us through the following channels:

*   **Flink Mailing Lists:** [https://flink.apache.org/community/mailing-lists.html](https://flink.apache.org/community/mailing-lists.html)
*   **Flink Slack Channel:** [https://flink.apache.org/community/slack.html](https://flink.apache.org/community/slack.html)
*   **GitHub Issues:** [https://github.com/apache/flink-docker/issues](https://github.com/apache/flink-docker/issues)