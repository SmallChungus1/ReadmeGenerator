# Apache Flink Docker Images

## Description

This repository provides Docker images for Apache Flink, including various versions and Java runtime configurations. The images are built from source and packaged with a minimal base image to include Flink binaries, configuration utilities, and necessary dependencies.

## Features

- Docker images for Apache Flink 1.20, 2.0, 2.1, and 2.2
- Multiple Java versions: 8, 11, 17, and 21
- Scala 2.12 support
- Pre-configured Flink settings with network interface binding
- Built-in support for jemalloc memory allocator
- Container entrypoint scripts for starting Flink components
- Support for running Flink in standalone mode, jobmanager, taskmanager, or history server modes

## Prerequisites / Requirements

- Docker or container runtime
- Access to the internet for downloading Flink binaries
- A Linux-based environment (Ubuntu 20.04 or later)

## Installation

The images are available on Docker Hub as `apache/flink` and are built from the `apache/flink-docker` repository on GitHub.

To pull a specific image:

```bash
docker pull apache/flink:1.20.3-scala_2.12-java11
```

Available tags include:
- `1.20.3-scala_2.12-java11`, `1.20-scala_2.12-java11`, `scala_2.12-java11`, `1.20.3-scala_2.12`, `1.20-scala_2.12`, `scala_2.12`, `1.20.3-java11`, `1.20-java11`, `java11`, `1.20.3`, `1.20`, `latest`
- `2.0.1-scala_2.12-java17`, `2.0-scala_2.12-java17`, `scala_2.12-java17`, `2.0.1-java17`, `2.0-java17`, `java17`, `2.0.1`, `2.0`, `latest`
- `2.1.1-scala_2.12-java17`, `2.1-scala_2.12-java17`, `scala_2.12-java17`, `2.1.1-java17`, `2.1-java17`, `java17`, `2.1.1`, `2.1`, `latest`
- `2.2.0-scala_2.12-java17`, `2.2-scala_2.12-java17`, `scala_2.12-java17`, `2.2.0-java17`, `2.2-java17`, `java17`, `2.2.0`, `2.2`, `latest`

## Usage

Run Flink components using the appropriate image and command:

```bash
# Start Flink JobManager
docker run -d --name flink-jobmanager \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  apache/flink:1.20.3-scala_2.12-java11 jobmanager

# Start Flink TaskManager
docker run -d --name flink-taskmanager \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  -e TASK_MANAGER_NUMBER_OF_TASK_SLOTS=4 \
  apache/flink:1.20.3-scala_2.12-java11 taskmanager

# Start Flink standalone job
docker run -d --name flink-standalone \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  apache/flink:1.20.3-scala_2.12-java11 standalone-job

# Start Flink History Server
docker run -d --name flink-historyserver \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  apache/flink:1.20.3-scala_2.12-java11 history-server
```

### Environment Variables

- `JOB_MANAGER_RPC_ADDRESS`: The address to bind the JobManager RPC endpoint (default: container hostname)
- `TASK_MANAGER_NUMBER_OF_TASK_SLOTS`: Number of task slots per task manager (default: not set)
- `FLINK_PROPERTIES`: Comma-separated key=value pairs to override Flink configuration
- `ENABLE_BUILT_IN_PLUGINS`: Comma-separated list of built-in plugins to enable (e.g., `state-backup`, `checkpointing`)

### Configuration

The entrypoint script automatically configures Flink to bind to the container's network interface by default. Configuration files are located in `/opt/flink/conf`.

## Contributing

Contributions are welcome. Please open an issue or pull request for any improvements or bug fixes.

- Fork the repository
- Create a feature branch
- Commit your changes
- Push to the branch
- Open a pull request

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.

## Contact / Authors

The Apache Flink Project  
dev@flink.apache.org  
https://flink.apache.org/