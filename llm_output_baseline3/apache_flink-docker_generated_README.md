# Apache Flink Docker Images

![Apache License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![GitHub Actions](https://img.shields.io/github/workflow/status/apache/flink-docker/build-and-push-docker-images)
![Docker](https://img.shields.io/badge/docker-yes-green.svg)

A collection of Docker images for Apache Flink, providing pre-built, ready-to-use containers for running Flink applications in production environments.

---

## Description

The Apache Flink Docker project provides a set of Docker images for Apache Flink, enabling developers and data engineers to run Flink applications in containers across various environments—on-premises, in the cloud, or in Kubernetes clusters.

This repository contains Dockerfiles and scripts to build and publish Flink images for different Flink versions (1.20, 2.0, 2.1, 2.2), with support for multiple Java versions (Java 8, 11, 17, 21) and Scala 2.12. Each image is built on top of a secure, minimal base image and includes essential dependencies, security hardening, and configuration adjustments to ensure optimal performance and compatibility.

The images are designed to be used with minimal configuration, allowing users to start Flink components (JobManager, TaskManager, HistoryServer, or standalone jobs) with just a few environment variables.

---

## Features

- ✅ **Multiple Flink Versions**: Supports Flink 1.20, 2.0, 2.1, and 2.2.
- ✅ **Multiple Java Versions**: Available for Java 8, 11, 17, and 21.
- ✅ **Secure by Default**: Uses non-root user (`flink`) and `gosu` for privilege reduction.
- ✅ **Network-Ready Configuration**: Automatically configures REST/RPC endpoints to bind to `0.0.0.0` for container networking.
- ✅ **Flexible Deployment**: Supports running JobManager, TaskManager, HistoryServer, or standalone jobs.
- ✅ **Customizable via Environment Variables**: Easily configure task slots, memory, and properties using environment variables.
- ✅ **Built-in Plugin Support**: Enables built-in plugins via `ENABLE_BUILT_IN_PLUGINS` environment variable.
- ✅ **JEMALLOC Memory Allocator**: Enabled by default to improve memory performance; can be disabled via `DISABLE_JEMALLOC`.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

---

## Prerequisites

To use these Docker images, you need:

- **Docker** or **Docker Desktop** (version 20.10 or later)
- **docker-compose** (optional, for local development)
- **Git** (to clone the repository, if needed)
- **Access to Docker Hub** (to pull images from `apache/flink`)

> ⚠️ Note: The images are built and published to Docker Hub. You do not need to build them locally unless you are contributing or customizing the images.

---

## Installation

The images are already available on Docker Hub. You can pull them directly using the following command:

```bash
docker pull apache/flink:2.2.0-scala_2.12-java17
```

To use a specific version or Java version, refer to the `release.metadata` files in each directory for available tags.

### Example: Pull a Flink 2.2 Image with Java 11

```bash
docker pull apache/flink:2.2.0-scala_2.12-java11
```

> 📝 The image tag format is: `version-scala_2.12-javaX`, where `X` is the Java version (e.g., 11, 17, 21).

---

## Usage

### Starting Flink Components

Once pulled, you can start Flink components using the container's entrypoint script.

#### 1. Start JobManager

```bash
docker run -d --name flink-jobmanager \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  -p 6123:6123 \
  -p 8081:8081 \
  apache/flink:2.2.0-scala_2.12-java17
```

> The JobManager exposes REST endpoints on port 6123 and the web UI on port 8081.

#### 2. Start TaskManager

```bash
docker run -d --name flink-taskmanager \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  -e TASK_MANAGER_NUMBER_OF_TASK_SLOTS=4 \
  -p 6124:6124 \
  apache/flink:2.2.0-scala_2.12-java17
```

> The TaskManager connects to the JobManager via the `JOB_MANAGER_RPC_ADDRESS` environment variable.

#### 3. Start HistoryServer

```bash
docker run -d --name flink-historyserver \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  -p 8088:8088 \
  apache/flink:2.2.0-scala_2.12-java17
```

> The HistoryServer provides access to job execution history via the web UI on port 8088.

#### 4. Run a Standalone Job

```bash
docker run -it --name flink-standalone \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  apache/flink:2.2.0-scala_2.12-java17 \
  standalone-job
```

> This starts a standalone Flink job with no JobManager or TaskManager required.

---

### Environment Variables

| Variable | Description |
|--------|-------------|
| `JOB_MANAGER_RPC_ADDRESS` | The address of the JobManager (default: container hostname) |
| `TASK_MANAGER_NUMBER_OF_TASK_SLOTS` | Number of task slots per TaskManager (default: 1) |
| `FLINK_PROPERTIES` | Comma-separated key=value pairs for Flink configuration |
| `ENABLE_BUILT_IN_PLUGINS` | Comma-separated list of plugin JARs to enable (e.g., `state-backup,checkpoint`) |
| `DISABLE_JEMALLOC` | Set to `true` to disable the JEMALLOC memory allocator |

> Example:
> ```bash
> docker run -e FLINK_PROPERTIES="taskmanager.memory.flink=1g" \
>   -e TASK_MANAGER_NUMBER_OF_TASK_SLOTS=8 \
>   apache/flink:2.2.0-scala_2.12-java17
> ```

---

## Contributing

Contributions to this project are welcome! Please follow these guidelines:

- Fork the repository on GitHub.
- Create a new branch for your feature or bug fix.
- Submit a pull request with clear descriptions and test cases (if applicable).
- Ensure all Dockerfiles and metadata are correctly formatted and consistent.

For reporting bugs or requesting features, please open an issue in the [Apache Flink GitHub Issues](https://github.com/apache/flink/issues).

> 📚 See the [CONTRIBUTING.md](https://github.com/apache/flink-docker/blob/master/CONTRIBUTING.md) file for detailed contribution guidelines.

---

## License

This project is licensed under the **Apache License, Version 2.0**. See the [LICENSE](https://github.com/apache/flink-docker/blob/master/LICENSE) file for details.

---

## Contact / Authors

This project is maintained by the **Apache Flink Community**.

- 📧 Email: `dev@flink.apache.org`
- 🌐 Website: [https://flink.apache.org](https://flink.apache.org)
- 💬 Community: [Apache Flink Slack](https://apache-flink.slack.com), [GitHub Discussions](https://github.com/apache/flink/discussions)

For questions or feedback, please reach out to the Flink community or open an issue on GitHub.

---

> This project is part of the [Apache Software Foundation](https://www.apache.org/) ecosystem.  
> All contributions are governed by the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).