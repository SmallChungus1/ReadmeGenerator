# Apache Flink Docker Images

![Apache License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![GitHub](https://img.shields.io/badge/github-https%3A%2F%2Fgithub.com%2Fapache%2Fflink--docker-green.svg)
![Docker](https://img.shields.io/badge/docker-https%3A%2F%2Fhub.docker.com%2Fr%2Fapache%2Fflink-blue.svg)

A collection of Docker images for **Apache Flink**, providing pre-built, production-ready containers for various Flink versions and Java runtime environments.

---

## Description

Apache Flink is a powerful, distributed stream and batch processing framework. This repository provides official Docker images for Flink, enabling developers and data engineers to run Flink applications in containers with minimal configuration.

The images are built for multiple Flink versions (1.20, 2.0, 2.1, 2.2) and Java versions (8, 11, 17, 21), ensuring compatibility with a wide range of use cases. Each image includes:

- Flink binaries compiled for the specified version and Scala/Java combination
- A secure, non-root user (`flink`) with minimal privileges
- Automatic configuration to bind Flink services to the container's network interface
- Support for running JobManager, TaskManager, standalone jobs, or HistoryServer
- Optional built-in plugins and memory allocator (jemalloc) configuration

This project is maintained by the Apache Flink community and is designed to simplify Flink deployment in cloud, Kubernetes, or local development environments.

---

## Features

- ✅ **Multiple Flink versions**: 1.20, 2.0, 2.1, and 2.2
- ✅ **Multiple Java versions**: 8, 11, 17, and 21
- ✅ **Non-root user execution**: All services run as the `flink` user for security
- ✅ **Network binding**: REST/RPC endpoints bind to `0.0.0.0` by default
- ✅ **Flexible configuration**: Customizable via environment variables
- ✅ **Built-in plugins support**: Enable required plugins via `ENABLE_BUILT_IN_PLUGINS`
- ✅ **Memory allocator control**: Disable jemalloc with `DISABLE_JEMALLOC=true`
- ✅ **Easy deployment**: Run with `docker run` or integrate with Kubernetes, ECS, etc.

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

- **Docker** (version 18.03 or later) installed on your system
- A working internet connection to download Flink binaries
- Access to Docker Hub or GitHub Container Registry (GHCR) for image pulls (if needed)

> ⚠️ **Note**: The images are built and published to Docker Hub (`apache/flink`) and GitHub Container Registry (`ghcr.io/apache/flink-docker`). The `publish-to-dockerhub.sh` script automates the transfer from GHCR to Docker Hub.

---

## Installation

The images are available via Docker Hub and GitHub Container Registry. You can pull them directly using the `docker pull` command.

### Pull Flink Images

```bash
# Pull a specific version and Java combination
docker pull apache/flink:1.20.3-scala_2.12-java11

# Pull the latest version (automatically resolves to the latest stable tag)
docker pull apache/flink:latest
```

> ✅ The `latest` tag is automatically resolved to the most recent stable version.  
> ✅ All tags include the Flink version, Scala version, and Java version (e.g., `2.2.0-scala_2.12-java17`).

### Available Tags

| Version | Java Version | Tags |
|--------|--------------|------|
| 1.20   | 8, 11, 17    | `1.20.3-scala_2.12-java8`, `1.20.3-scala_2.12-java11`, `1.20.3-scala_2.12-java17` |
| 2.0    | 11, 17, 21   | `2.0.1-scala_2.12-java11`, `2.0.1-scala_2.12-java17`, `2.0.1-scala_2.12-java21` |
| 2.1    | 11, 17, 21   | `2.1.1-scala_2.12-java11`, `2.1.1-scala_2.12-java17`, `2.1.1-scala_2.12-java21` |
| 2.2    | 11, 17, 21   | `2.2.0-scala_2.12-java11`, `2.2.0-scala_2.12-java17`, `2.2.0-scala_2.12-java21` |

> 🔍 For a complete list of tags, refer to the `release.metadata` files in each version directory.

---

## Usage

Run Flink components using the provided Docker image with the appropriate command.

### Start JobManager

```bash
docker run -d --name flink-jobmanager \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  -p 6123:6123 \
  -p 8081:8081 \
  apache/flink:2.2.0-scala_2.12-java17 \
  jobmanager
```

### Start TaskManager

```bash
docker run -d --name flink-taskmanager \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  -p 6123:6123 \
  -p 8081:8081 \
  apache/flink:2.2.0-scala_2.12-java17 \
  taskmanager
```

### Run a Standalone Job

```bash
docker run -d --name flink-standalone \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  apache/flink:2.2.0-scala_2.12-java17 \
  standalone-job
```

### Start History Server

```bash
docker run -d --name flink-historyserver \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  -p 8088:8088 \
  apache/flink:2.2.0-scala_2.12-java17 \
  historyserver
```

> 📝 **Note**: The `JOB_MANAGER_RPC_ADDRESS` environment variable is optional. If not set, the container's hostname is used.

---

### Environment Variables

| Variable | Description |
|--------|-------------|
| `JOB_MANAGER_RPC_ADDRESS` | Sets the address for JobManager RPC (default: container hostname) |
| `TASK_MANAGER_NUMBER_OF_TASK_SLOTS` | Sets the number of task slots per TaskManager (e.g., `4`) |
| `FLINK_PROPERTIES` | Comma-separated key=value pairs (e.g., `jobmanager.rpc.address=0.0.0.0`) |
| `ENABLE_BUILT_IN_PLUGINS` | Comma-separated list of plugin JARs to enable (e.g., `state-backup,checkpoint`) |
| `DISABLE_JEMALLOC` | Set to `true` to disable jemalloc memory allocator |

---

## Contributing

We welcome contributions to improve, maintain, and extend this project. Please follow these guidelines:

- Fork the repository on GitHub
- Create a new feature branch (`feature/your-feature`)
- Submit a pull request with a clear description of your changes
- Ensure all Dockerfiles and metadata are correctly formatted
- Run the CI workflow to validate your changes

For bug reports or feature requests, please open an issue in the [Apache Flink GitHub repository](https://github.com/apache/flink/issues).

> 🔗 See the [CONTRIBUTING.md](https://github.com/apache/flink-docker/blob/master/CONTRIBUTING.md) for detailed contribution guidelines.

---

## License

This project is licensed under the **Apache License, Version 2.0**.

See the [LICENSE](https://github.com/apache/flink-docker/blob/master/LICENSE) file for details.

---

## Contact / Authors

This project is maintained by the **Apache Flink Community**.

- 📧 **Development Team**: `dev@flink.apache.org`
- 🌐 **Project Homepage**: [https://flink.apache.org](https://flink.apache.org)
- 📚 **GitHub Repository**: [https://github.com/apache/flink-docker](https://github.com/apache/flink-docker)
- 📞 **Community Forum**: [https://community.apache.org](https://community.apache.org)

For questions or feedback, please reach out to the Flink community via the official channels.