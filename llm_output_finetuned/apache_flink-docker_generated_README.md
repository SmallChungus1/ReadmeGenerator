# Apache Flink Docker Images

![Apache License](https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=for-the-badge)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

A collection of Docker images for **Apache Flink**, providing pre-built, production-ready containers for various Flink versions and Java runtime environments.

---

## Description

This repository contains Docker images for Apache Flink, designed to simplify deployment and operation in containerized environments. Each image is built from a specific Flink version (1.20, 2.0, 2.1, 2.2) and supports different Java versions (8, 11, 17, 21) to meet diverse application requirements.

The images are optimized for use in Kubernetes, Docker Swarm, and other container orchestration platforms. They include:
- Flink binaries with proper security and memory management
- Configurations to bind Flink services to the container's network interface
- Support for running Job Managers, Task Managers, History Servers, and standalone jobs
- Built-in support for jemalloc memory allocator (configurable)

All images are published to **Docker Hub** and **GitHub Container Registry (GHCR)**, with automated CI/CD workflows ensuring consistency and reliability.

---

## Features

- ✅ **Multiple Flink Versions**: Supports Flink 1.20, 2.0, 2.1, and 2.2
- ✅ **Multiple Java Versions**: Java 8, 11, 17, and 21 (via `scala_2.12-javaX`)
- ✅ **Secure by Default**: Runs as non-root user (`flink`) with minimal privileges
- ✅ **Network-Ready**: REST and RPC endpoints bind to `0.0.0.0` instead of `localhost`
- ✅ **Flexible Configuration**: Supports environment variables for customizing behavior
- ✅ **Built-in Plugins**: Enables optional built-in plugins via `ENABLE_BUILT_IN_PLUGINS`
- ✅ **Memory Optimization**: Default jemalloc memory allocator (can be disabled)
- ✅ **Cross-Platform**: Available for both `amd64` and `arm64v8` architectures

---

## Table of Contents

- [Prerequisites / Requirements](#prerequisites--requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Authors](#contact--authors)

---

## Prerequisites / Requirements

To use these Docker images, you need:

- **Docker** or **Docker Desktop** (version 20.10 or later)
- **Docker Hub** account (for pulling images)
- **Basic knowledge of Docker commands** (e.g., `docker run`, `docker logs`)

> ⚠️ **Note**: These images are built for Ubuntu-based systems using `eclipse-temurin` as the base JRE. They are not compatible with Windows or macOS without a Docker-in-Docker setup.

---

## Installation

The images are pre-built and available via Docker Hub. You can pull them directly using the `docker pull` command.

### Pull a Specific Image

```bash
# Example: Pull Flink 2.2 with Java 17
docker pull apache/flink:2.2.0-scala_2.12-java17

# Pull Flink 1.20 with Java 8 (latest)
docker pull apache/flink:1.20-java8
```

> 📝 **Tip**: The image tags follow a pattern like `version-javaX` or `version-scala_2.12-javaX`. See the [release.metadata](./release.metadata) files for complete tag lists.

---

## Usage

The images provide a command-line interface to start Flink components. You can run them with the following commands.

### Start a Job Manager

```bash
docker run -d --name flink-jobmanager \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  -p 6123:6123 \
  -p 8081:8081 \
  apache/flink:2.2.0-scala_2.12-java17 \
  jobmanager
```

> 🔍 The `JOB_MANAGER_RPC_ADDRESS` environment variable sets the address for the JobManager. If not specified, it defaults to the container's hostname.

### Start a Task Manager

```bash
docker run -d --name flink-taskmanager \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  -p 6123:6123 \
  -p 8081:8081 \
  apache/flink:2.2.0-scala_2.12-java17 \
  taskmanager
```

> 📌 The Task Manager connects to the Job Manager via the specified RPC address.

### Start a Standalone Job

```bash
docker run -d --name flink-standalone \
  apache/flink:2.2.0-scala_2.12-java17 \
  standalone-job
```

> 💡 This starts a standalone job manager, useful for testing or small-scale workloads.

### Start the History Server

```bash
docker run -d --name flink-historyserver \
  apache/flink:2.2.0-scala_2.12-java17 \
  historyserver
```

> 📊 The History Server provides access to job execution logs and metrics.

### Configure Environment Variables

You can customize behavior using environment variables:

| Variable | Purpose |
|--------|--------|
| `TASK_MANAGER_NUMBER_OF_TASK_SLOTS` | Sets the number of slots per task manager |
| `FLINK_PROPERTIES` | Comma-separated key=value pairs to override configuration |
| `ENABLE_BUILT_IN_PLUGINS` | Enables built-in plugins (e.g., `state-backup`, `kafka`) |
| `DISABLE_JEMALLOC` | Disables jemalloc memory allocator (set to `true`) |

Example:
```bash
docker run -e TASK_MANAGER_NUMBER_OF_TASK_SLOTS=4 \
  -e FLINK_PROPERTIES="execution.checkpointing.interval=30000" \
  apache/flink:2.2.0-scala_2.12-java17 \
  jobmanager
```

---

## Contributing

We welcome contributions to improve the Docker images, fix bugs, or add new features.

### How to Contribute

1. **Report Issues**: Open an issue on GitHub with a clear description.
2. **Submit Pull Requests**: For new features or bug fixes, create a PR with tests and documentation.
3. **Improve Documentation**: Help clarify usage or add examples.
4. **Suggest New Versions**: Propose support for new Flink or Java versions.

> 📚 For detailed contribution guidelines, see the [CONTRIBUTING.md](CONTRIBUTING.md) file (not included in this repository).

---

## License

This project is licensed under the **Apache License, Version 2.0**.

> See the [LICENSE](LICENSE) file for details.

---

## Contact / Authors

This project is maintained by the **Apache Flink Project**.

- 📧 Email: `dev@flink.apache.org`
- 🌐 Website: [https://flink.apache.org](https://flink.apache.org)
- 💬 Community: [Apache Flink Slack](https://flink.apache.org/community/)
- 🐞 Issues & Feature Requests: [GitHub Issues](https://github.com/apache/flink-docker/issues)

For questions or feedback, please reach out to the Flink community.

---

> ✅ **Note**: This repository is part of the official Apache Flink infrastructure. All images are built and tested by the Apache Flink team. For the latest updates, refer to the [Apache Flink GitHub](https://github.com/apache/flink) and [Apache Flink Documentation](https://nightlies.apache.org/flink/).