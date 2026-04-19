# Apache Flink Docker Images

## Description

This repository provides Docker images for Apache Flink, including various versions and Java runtime configurations. The images are built from source distributions and include configuration modifications to allow Flink to bind to the container's network interface by default.

## Features

- Docker images for Flink versions 1.20, 2.0, and 2.1
- Support for multiple Java versions (8, 11, 17, 21)
- Scala 2.12 compatibility
- Configuration to bind REST/RPC endpoints to the container's network interface
- Built-in support for plugins via symbolic links
- Memory allocator (jemalloc) support with optional disabling
- Non-root user execution with privilege checks

## Prerequisites / Requirements

- Docker or Docker Desktop
- Access to the Docker Hub registry (for publishing)
- `crane` command-line tool (for image copying, optional)
- Internet access for downloading Flink binaries and dependencies

## Installation

The images are available in the Docker Hub registry under the `apache/flink` namespace.

To pull an image:

```bash
docker pull apache/flink:2.2.0-scala_2.12-java17
```

Available tags include:
- Version-specific tags (e.g., `2.2.0-scala_2.12-java17`)
- Version tags (e.g., `2.2-scala_2.12-java17`)
- Java version tags (e.g., `java17`)
- Latest tag (for the most recent version)

## Usage

After pulling an image, start Flink components using the appropriate command:

```bash
# Start Job Manager
docker run -d --name jobmanager \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  apache/flink:2.2.0-scala_2.12-java17 jobmanager

# Start Task Manager
docker run -d --name taskmanager \
  -e JOB_MANAGER_RPC_ADDRESS=0.0.0.0 \
  apache/flink:2.2.0-scala_2.12-java17 taskmanager

# Start standalone job
docker run -d --name standalone-job \
  apache/flink:2.2.0-scala_2.12-java17 standalone-job

# Start History Server
docker run -d --name historyserver \
  apache/flink:2.2.0-scala_2.12-java17 historyserver
```

### Environment Variables

- `JOB_MANAGER_RPC_ADDRESS`: Sets the RPC address for the JobManager (default: container hostname)
- `TASK_MANAGER_NUMBER_OF_TASK_SLOTS`: Sets the number of task slots for TaskManagers
- `FLINK_PROPERTIES`: Comma-separated key=value pairs for Flink configuration
- `ENABLE_BUILT_IN_PLUGINS`: Comma-separated list of plugin JARs to enable (e.g., `state-backup,checkpoint`)
- `DISABLE_JEMALLOC`: Set to `true` to disable jemalloc memory allocator

## Contributing

Contributions are welcome. Please follow the Apache Flink contribution guidelines.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.

## Contact / Authors

The Apache Flink Project  
Contact: dev@flink.apache.org  
Repository: https://github.com/apache/flink-docker

For issues or feature requests, please open an issue on GitHub.