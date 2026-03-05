```markdown
# Apache Flink Docker Images

This repository provides Docker images for Apache Flink. These images are built from official Flink distributions and are designed to simplify the deployment and execution of Flink jobs.

## Description

This project builds and maintains Docker images for various versions and configurations of Apache Flink.  Images are provided for different Scala versions (currently 2.12), Java versions (8, 11, 17, and 21) and Ubuntu as the base operating system.  The repository leverages GitHub Actions to automatically build and push images to [GitHub Container Registry (GHCR)](https://ghcr.io).

## Features

*   **Multiple Flink Versions:** Supports various Flink versions including 1.20, 2.0, 2.1, and 2.2.
*   **Multiple Java Versions:** Provides images built with Java 8, 11, 17, and 21.
*   **Ubuntu-based:** Uses Ubuntu as the base operating system for container images.
*   **Automated Builds:** Leverages GitHub Actions for continuous integration and automated image building and publishing.
*   **GHCR Integration:** Images are published to GitHub Container Registry for easy access and distribution.
*   **Reproducible Builds:** Dockerfiles and build scripts are version controlled.
*   **Configuration Options:** Images are pre-configured for optimized performance and ease of use.

## Installation

You do *not* directly install from this repository. Instead, you pull the pre-built Docker images from the GitHub Container Registry (GHCR).

**Example (Pulling a Flink 2.2 image with Java 11):**

```bash
docker pull apache/flink:2.2.0-scala_2.12-java11
```

Replace `2.2.0-scala_2.12-java11` with the desired tag based on the version and configuration you require.

## Usage

Once you've pulled the Docker image, you can run a Flink job using the `docker run` command.

**Example (Running a Flink JobManager):**

```bash
docker run -d --name flink-jobmanager -p 8081:8081 apache/flink:2.2.0-scala_2.12-java11 jobmanager
```

**Example (Running a Flink TaskManager):**

```bash
docker run -d --name flink-taskmanager --link flink-jobmanager apache/flink:2.2.0-scala_2.12-java11 taskmanager
```

**Running in Standalone Mode:**

```bash
docker run -d --name flink-standalone apache/flink:2.2.0-scala_2.12-java11 standalone-job
```

**Other commands and configurations:**

Refer to the official Apache Flink documentation for detailed information on running Flink jobs in Docker: [https://flink.apache.org/docs/](https://flink.apache.org/docs/)

## Available Tags

The following tags are generally available.  Note that the versions and availability may change. You can find the most up-to-date list by browsing the GHCR repository: [https://ghcr.io/apache/flink](https://ghcr.io/apache/flink)

*   **`<flink_version>-scala_2.12-java8`**: Flink version with Scala 2.12 and Java 8.
*   **`<flink_version>-scala_2.12-java11`**: Flink version with Scala 2.12 and Java 11.
*   **`<flink_version>-scala_2.12-java17`**: Flink version with Scala 2.12 and Java 17.
*   **`<flink_version>-scala_2.12-java21`**: Flink version with Scala 2.12 and Java 21.
*   **`latest`**:  Generally points to the latest stable Flink release with Java 11 and Scala 2.12. *Use with caution as this can change unexpectedly.*

Where `<flink_version>` is something like `1.20.3`, `2.0.1`, `2.1.1`, or `2.2.0`.

## Contributing

Contributions are welcome! Please review the [CONTRIBUTING guide](CONTRIBUTING.md) to learn how to contribute to this project.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE file](LICENSE) for more information.

## GitHub Actions

This repository utilizes GitHub Actions for automated builds and publishing. The following workflows are defined:

*   **`docker-bake.hcl`**: This file defines the build process using Docker Buildx, allowing for multi-platform builds.
*   **`docker_push.yml`**: This workflow is triggered on pushes to the main branch and tags, and automatically builds and pushes the Docker images to GHCR.
*   **`snapshot.yml`**: This workflow builds and publishes snapshot releases on a daily schedule.

## Known Issues and Limitations

*   The images are relatively large due to including the entire Flink distribution.
*   The configuration options within the images are limited to those set during the build process.  Custom configurations should be applied via external configuration files or environment variables.
*   The images are built for Linux/amd64 and Linux/arm64 architectures.

## Support

For questions or support, please reach out to the Apache Flink community through the official channels:

*   **Mailing Lists:** [https://flink.apache.org/community/mailing-lists.html](https://flink.apache.org/community/mailing-lists.html)
*   **Slack:** [https://flink.apache.org/community/slack.html](https://flink.apache.org/community/slack.html)
*   **GitHub Issues:** [https://github.com/apache/flink/issues](https://github.com/apache/flink/issues)