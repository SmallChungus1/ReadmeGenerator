# Apache RocketMQ Docker

## Description
This repository provides Docker images and configuration templates for Apache RocketMQ, a distributed messaging system. It includes Dockerfiles for building RocketMQ images on various base images (Alpine, Ubuntu, CentOS), Kubernetes Helm charts for deploying RocketMQ in Kubernetes clusters, and scripts for running RocketMQ in Docker Compose or standalone mode.

## Features
- Docker images for RocketMQ broker, nameserver, and dashboard
- Support for multiple base images: Alpine, Ubuntu, CentOS
- Docker Compose templates for quick setup of RocketMQ clusters
- Kubernetes Helm charts for deploying RocketMQ in Kubernetes environments
- SSL/TLS support for secure communication
- Support for Dledger (Raft) mode for high availability
- Customizable configuration through environment variables and configuration files

## Prerequisites / Requirements
- Docker or Docker Desktop installed
- Docker Compose (version 2.0 or later) for Docker Compose templates
- Kubernetes cluster with Helm installed (for Kubernetes Helm charts)
- Java 8 or 11 (required by RocketMQ)
- A supported base image (Alpine, Ubuntu, or CentOS)

## Installation
### Build RocketMQ Docker Images
1. Clone the repository:
```bash
git clone https://github.com/apache/rocketmq-docker.git
cd rocketmq-docker
```

2. Build images for specific versions:
```bash
# Build for version 4.5.0 on Ubuntu
sh image-build/build-image.sh 4.5.0 ubuntu

# Build for version 5.0.0 on Alpine
sh image-build/build-image.sh 5.0.0 alpine
```

3. Build dashboard image:
```bash
sh image-build/build-image-dashboard.sh 5.0.0 centos
```

### Deploy with Docker Compose
1. Create a directory for your RocketMQ setup:
```bash
mkdir rocketmq-demo
cd rocketmq-demo
```

2. Copy the Docker Compose template:
```bash
cp ../templates/docker-compose/rmq4-docker-compose.yml .
```

3. Update the version in the template:
```bash
sed -i "s/ROCKETMQ_VERSION/4.5.0/g" rmq4-docker-compose.yml
```

4. Start the services:
```bash
docker compose up -d
```

### Deploy with Kubernetes Helm
1. Install Helm if not already available:
```bash
# On Ubuntu/Debian
sudo apt-get install helm

# On macOS with Homebrew
brew install helm
```

2. Deploy RocketMQ to Kubernetes:
```bash
# Set the version
export ROCKETMQ_VERSION=4.5.0

# Deploy with Helm
helm install rocketmq apache/rocketmq-k8s-helm --set image.tag=${ROCKETMQ_VERSION}
```

## Usage
### Running RocketMQ with Docker
Use the provided scripts to start RocketMQ services:

```bash
# Start a basic broker with nameserver
sh templates/play-docker.sh ubuntu

# Start with TLS support
sh templates/play-docker-tls.sh ubuntu

# Start with Dledger (Raft) mode
sh templates/play-docker-dledger.sh
```

### Using Configuration Files
Configuration files are provided in the `product/conf` directory with examples for:
- 2m-2s-async (async master/slave)
- 2m-2s-sync (sync master/slave)
- 2m-noslave (single master)

Replace `REPLACE_IT` values with actual IP addresses or hostnames.

### Accessing the Dashboard
After starting the broker and nameserver, access the RocketMQ dashboard:
```bash
sh product/start-dashboard.sh 5.0.0
```

The dashboard is accessible at `http://localhost:6765`.

## Contributing
Contributions are welcome. Please follow these guidelines:
1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Commit your changes with clear, descriptive messages
4. Submit a pull request with a detailed description of your changes

## License
Apache License 2.0

## Contact / Authors
This project is maintained by the Apache Software Foundation. For questions or feedback, please contact the RocketMQ community at https://rocketmq.apache.org.