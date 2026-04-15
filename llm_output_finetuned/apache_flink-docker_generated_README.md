# Apache Flink Docker Images

## Description

This repository provides pre-built Docker images for **Apache Flink**, enabling easy deployment and management of Flink clusters in containerized environments. The images are available for multiple Flink versions (1.20, 2.0, 2.1, 2.2) and support different Java versions (8, 11, 17, 21) with Scala 2.12.

Each image is built on top of a lightweight Ubuntu base with the appropriate Java runtime and includes Flink binaries, essential dependencies, and security best practices such as running Flink as a non-root user. The images are designed to be used with Docker, Kubernetes, or any container orchestration platform.

## Features

- ✅ **Multiple Flink Versions**: Supports Flink 1.20, 2.0, 2.1, and 2.2.
- ✅ **Multiple Java Versions**: Available for Java 8, 11, 17, and 21.
- ✅ **Scala 2.12 Compatibility**: All images are built with Scala 2.12.
- ✅ **Non-Root Execution**: Flink runs as a dedicated `flink` user to enhance security.
- ✅ **Network Accessibility**: Configured to bind REST and RPC endpoints to `0.0.0.0` for container network access.
- ✅ **GPG Verification**: All Flink binaries are verified using GPG signatures to ensure integrity.
- ✅ **JEMALLOC Support**: Memory allocator (jemalloc) is enabled by default for better memory management.
- ✅ **Plugin Support**: Built-in plugins can be enabled via environment variables.
- ✅ **Flexible Configuration**: Supports custom configuration via environment variables and Flink properties files.

## Installation

To use these Docker images, ensure Docker is installed and running on your system. The images are available on **Docker Hub** (`apache/flink`) and **GitHub Container Registry (GHCR)** (`ghcr.io/apache/flink-docker`).

### Pull Images from Docker Hub

```bash
# Pull a specific version and Java version
docker pull apache/flink:1.20.3-scala_2.12-java11

# Pull the latest version (automatically resolves to the latest stable)
docker pull apache/flink:latest
```

### Pull Images from GitHub Container Registry (GHCR)

```bash
# Pull from GHCR (for development or testing)
docker pull ghcr.io/apache/flink-docker:1.20.3-scala_2.12-java11
```

> 🔍 **Note**: The `latest` tag is managed automatically and points to the most recent stable release. For production, it's recommended to use specific version tags.

## Usage

The images provide a command-line interface to start Flink components. You can run the following commands to start Flink services:

### 1. Start Job Manager

```bash
docker run -d \
  --name flink-jobmanager \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  apache/flink:1.20.3-scala_2.12-java11 \
  jobmanager
```

### 2. Start Task Manager

```bash
docker run -d \
  --name flink-taskmanager \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  -e TASK_MANAGER_NUMBER_OF_TASK_SLOTS=4 \
  apache/flink:1.20.3-scala_2.12-java11 \
  taskmanager
```

### 3. Start Standalone Job (Alternative to Job Manager)

```bash
docker run -d \
  --name flink-standalone \
  apache/flink:1.20.3-scala_2.12-java11 \
  standalone-job
```

### 4. Start History Server

```bash
docker run -d \
  --name flink-historyserver \
  apache/flink:1.20.3-scala_2.12-java11 \
  history-server
```

### 5. View Help and Available Commands

```bash
docker run --rm apache/flink:1.20.3-scala_2.12-java11 help
```

> 📝 **Environment Variables**:
> - `JOB_MANAGER_RPC_ADDRESS`: Sets the JobManager RPC address (default: container hostname).
> - `TASK_MANAGER_NUMBER_OF_TASK_SLOTS`: Sets the number of task slots per task manager.
> - `FLINK_PROPERTIES`: A semicolon-separated list of key=value properties to override Flink configuration.
> - `ENABLE_BUILT_IN_PLUGINS`: Enables built-in plugins (e.g., `state-backup`, `checkpointing`).
> - `DISABLE_JEMALLOC`: Set to `true` to disable jemalloc memory allocator.

### 6. Example: Run a Flink Job with Custom Configuration

```bash
# Start a task manager with 8 slots and custom properties
docker run -d \
  --name flink-taskmanager \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  -e TASK_MANAGER_NUMBER_OF_TASK_SLOTS=8 \
  -e FLINK_PROPERTIES="jobmanager.rpc.address=192.168.1.100;taskmanager.memory.process.size=4g" \
  apache/flink:2.2.0-scala_2.12-java17 \
  taskmanager
```

> 💡 **Tip**: For production deployments, use a container orchestration platform like Kubernetes or Docker Swarm to manage multiple Flink services.

---

**License**: Apache License 2.0  
**Maintainers**: The Apache Flink Project <dev@flink.apache.org>  
**Homepage**: https://flink.apache.org/  
**Repository**: https://github.com/apache/flink-docker