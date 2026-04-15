# Apache Flink Docker Images

## Description

This repository provides pre-built Docker images for Apache Flink, enabling easy deployment and runtime execution of Flink applications in containerized environments. The images are designed to be lightweight, secure, and compatible with various Flink versions and Java runtime versions.

The project includes Dockerfiles for Flink versions 1.20, 2.0, and 2.1, each with support for multiple Java versions (Java 8, 11, 17, and 21). Each image is built on top of a secure, minimal base image (e.g., Eclipse Temurin) and includes essential dependencies, Flink binaries, and configuration adjustments to ensure proper network binding within containerized environments.

## Features

- **Multiple Flink Versions**: Support for Flink 1.20, 2.0, and 2.1.
- **Multiple Java Versions**: Available for Java 8, 11, 17, and 21.
- **Secure Container Setup**: Uses `gosu` for dropping privileges to a non-root `flink` user.
- **Network Configuration**: Automatically configures REST/RPC endpoints to bind to `0.0.0.0` instead of `localhost` for container network compatibility.
- **Flexible Configuration**: Supports custom configuration via environment variables such as `TASK_MANAGER_NUMBER_OF_TASK_SLOTS`, `FLINK_PROPERTIES`, and `DISABLE_JEMALLOC`.
- **Built-in Plugin Support**: Enables optional built-in plugins via the `ENABLE_BUILT_IN_PLUGINS` environment variable.
- **Standardized Entry Points**: Provides clear command-line interfaces for starting JobManager, TaskManager, HistoryServer, or standalone jobs.
- **Cross-Platform Support**: Builds for both `amd64` and `arm64v8` architectures.

## Installation

To use the Flink Docker images, ensure Docker is installed and running on your system. The images are available on Docker Hub at `apache/flink`.

### Prerequisites

- Docker installed and running
- `docker login` to Docker Hub (required for publishing)

### Build and Run

1. **Clone the Repository** (optional, for development):
   ```bash
   git clone https://github.com/apache/flink-docker.git
   cd flink-docker
   ```

2. **Build a Specific Image**:
   ```bash
   docker build -t flink:1.20.3-scala_2.12-java11 -f 1.20/scala_2.12-java11-ubuntu/Dockerfile .
   ```

3. **Run the Image**:
   ```bash
   docker run -d --name flink-jobmanager \
     -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
     -e TASK_MANAGER_NUMBER_OF_TASK_SLOTS=4 \
     flink:1.20.3-scala_2.12-java11
   ```

## Usage

The Flink Docker images provide a command-line interface for starting various Flink components. The available commands are:

- `jobmanager`: Starts the Flink JobManager
- `taskmanager`: Starts a Flink TaskManager
- `standalone-job`: Starts a standalone job (equivalent to JobManager)
- `historyserver`: Starts the Flink HistoryServer

### Example: Starting a Flink JobManager

```bash
docker run -d --name flink-jobmanager \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  -e TASK_MANAGER_NUMBER_OF_TASK_SLOTS=4 \
  apache/flink:1.20.3-scala_2.12-java11 \
  jobmanager
```

### Example: Starting a TaskManager

```bash
docker run -d --name flink-taskmanager \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  -e TASK_MANAGER_NUMBER_OF_TASK_SLOTS=4 \
  apache/flink:1.20.3-scala_2.12-java11 \
  taskmanager
```

### Example: Starting a Standalone Job

```bash
docker run -d --name flink-standalone \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  apache/flink:1.20.3-scala_2.12-java11 \
  standalone-job
```

### Environment Variables

| Variable | Description |
|---------|-------------|
| `JOB_MANAGER_RPC_ADDRESS` | Sets the RPC address for the JobManager (default: container hostname) |
| `TASK_MANAGER_NUMBER_OF_TASK_SLOTS` | Sets the number of task slots for TaskManagers |
| `FLINK_PROPERTIES` | Comma-separated key=value pairs for custom Flink configuration |
| `DISABLE_JEMALLOC` | Set to `true` to disable jemalloc memory allocator |
| `ENABLE_BUILT_IN_PLUGINS` | Comma-separated list of built-in plugins to enable (e.g., `statebackend-rocksdb`) |

### Accessing Flink Services

- **REST API**: Available on port `8081`
- **JobManager RPC**: Available on port `6123`
- **Blob Server**: Available on port `6124`
- **Query Server**: Available on port `6125`

> **Note**: The images are designed to run in non-root containers. Running as root is discouraged and will trigger a warning message.