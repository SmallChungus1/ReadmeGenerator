Size: 411 bytes
Lines: 16
---
# RocketMQ SSL Certificate and Private Key

The following files contain the client and server certificates and private keys for RocketMQ's TLS/SSL support.

## Files
- `ca.crt` - Certificate Authority (CA) certificate
- `ca.srl` - Certificate Authority (CA) serial number
- `ca_rsa_private.pem` - CA private key (RSA)
- `server.crt` - Server certificate
- `server_rsa_private.pem` - Server private key (RSA)
- `client.crt` - Client certificate
- `client_rsa_private.pem` - Client private key (RSA)
- `ssl.properties` - Configuration file for SSL/TLS settings

## Usage
To use SSL/TLS in RocketMQ, you need to:
1. Place the certificate and key files in the `/home/rocketmq/ssl` directory
2. Update the `ssl.properties` file to point to the correct paths
3. Set the `JAVA_OPT` environment variable to enable TLS
4. Restart the RocketMQ services

## Security Note
The private keys are encrypted and should be kept secure. Never share these files or expose them in public repositories.

## Verification
You can verify the certificates using OpenSSL:
```bash
openssl x509 -in ca.crt -text -noout
openssl x509 -in server.crt -text -noout
```

---

File: templates/README.md
Size: 2225 bytes
Lines: 52
---
# Apache RocketMQ Docker

This repository provides Docker images and scripts for running Apache RocketMQ with various configurations.

## Overview

Apache RocketMQ is a distributed messaging and event bus platform designed to handle high-throughput, low-latency messaging scenarios. This repository offers pre-built Docker images and configuration scripts to simplify the setup and deployment of RocketMQ in development, testing, and production environments.

## Features

- **Multiple Base Images**: Supports Alpine, Ubuntu, and CentOS for containerization
- **Multiple RocketMQ Versions**: Compatible with various RocketMQ release versions
- **Complete Stack**: Includes nameserver, broker, and proxy components
- **Docker Compose Support**: Easy-to-use docker-compose configuration files
- **Kubernetes Support**: Helm charts for Kubernetes deployment
- **SSL/TLS Support**: Built-in support for secure messaging
- **Dledger Support**: Support for distributed consensus (Raft)
- **Dashboard**: Integrated web dashboard for monitoring

## Installation

### Prerequisites
- Docker or Docker Compose installed
- Java 8 or 11 installed (required by RocketMQ)

### Using Docker Images

1. **Pull the latest image**:
```bash
docker pull apache/rocketmq:latest
```

2. **Run a basic RocketMQ instance**:
```bash
docker run -d -p 9876:9876 --name rmqnamesrv apache/rocketmq:latest sh mqnamesrv
```

3. **Run a broker**:
```bash
docker run -d -p 10911:10911 --name rmqbroker -e "NAMESRV_ADDR=namesrv:9876" apache/rocketmq:latest sh mqbroker -c /opt/rocketmq/conf/broker.conf
```

### Using Docker Compose

1. **Create a directory** for your RocketMQ configuration:
```bash
mkdir rocketmq && cd rocketmq
```

2. **Copy the docker-compose.yml file** from this repository:
```bash
cp templates/docker-compose/rmq4-docker-compose.yml .
```

3. **Start the services**:
```bash
docker-compose up -d
```

### Using Kubernetes

1. **Install the Helm chart**:
```bash
helm repo add rocketmq https://github.com/apache/rocketmq-k8s-helm
helm repo update
helm install my-rocketmq rocketmq/rocketmq
```

2. **Access the services**:
- Nameserver: `http://<service-ip>:9876`
- Broker: `http://<service-ip>:10911`

## Usage Examples

### Setting Up a Cluster

To create a multi-node cluster with replication:
1. Use the `2m-2s-sync` configuration in the `product/conf` directory
2. Start the nameserver and two brokers with different IDs
3. Configure the brokers to form a master-slave relationship

### Using SSL/TLS

1. Place the SSL certificate and key files in the `/home/rocketmq/ssl` directory
2. Update the `ssl.properties` file to point to the correct paths
3. Set the `JAVA_OPT` environment variable to enable TLS
4. Restart the services

### Using the Dashboard

1. Pull the dashboard image:
```bash
docker pull apache/rocketmq-dashboard:latest
```

2. Run the dashboard:
```bash
docker run -d -p 6765:8080 --name rocketmq-dashboard apache/rocketmq-dashboard:latest
```

## Configuration

RocketMQ configurations are defined in the `product/conf` directory, with various pre-defined configurations such as:
- `2m-2s-sync`: Two master-slave brokers with synchronous replication
- `2m-noslave`: Two master brokers with no slave
- `2m-2s-async`: Two master-slave brokers with asynchronous replication
- `broker.conf`: Basic broker configuration

## Troubleshooting

- **Connectivity Issues**: Ensure all services are running and ports are accessible
- **Configuration Errors**: Verify configuration files are correctly formatted
- **SSL/TLS Errors**: Check certificate paths and permissions
- **Resource Limits**: Ensure sufficient memory and CPU resources are allocated

## License

This project is licensed under the Apache License, Version 2.0. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

File: .github/ISSUE_TEMPLATE
Size: 380 bytes
Lines: 14
---
## Bug Report

Please provide:
- A clear and concise description of the issue
- Steps to reproduce the problem
- Expected behavior
- Actual behavior
- Environment information (OS, Docker version, etc.)

## Feature Request

Please provide:
- A clear and concise description of the feature
- Why this feature is needed
- How it would be implemented
- Any relevant existing features or alternatives

## General Questions

Please provide:
- Your question
- Any relevant context
- Environment information
---
---
File: templates/data/broker1/conf/dledger/broker.conf
Size: 1162 bytes
Lines: 27
---
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

brokerClusterName = RaftCluster
brokerName=RaftNode01
listenPort=30911
#namesrvAddr=127.0.0.1:9876
storePathRootDir=/tmp/rmqstore/node00
storePathCommitLog=/tmp/rmqstore/node00/commitlog
enableDLegerCommitLog=true
dLegerGroup=RaftNode00
dLegerPeers=n0-172.18.0.12:40911;n1-172.18.0.13:40912;n2-172.18.0.14:40913
## must be unique
dLegerSelfId=n1
sendMessageThreadPoolNums=16


---
File: templates/data/broker0/conf/dledger/broker.conf
Size: 1162 bytes
Lines: 27
---
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

brokerClusterName = RaftCluster
brokerName=RaftNode00
listenPort=30911
#namesrvAddr=127.0.0.1:9876
storePathRootDir=/tmp/rmqstore/node00
storePathCommitLog=/tmp/rmqstore/node00/commitlog
enableDLegerCommitLog=true
dLegerGroup=RaftNode00
dLegerPeers=n0-172.18.0.12:40911;n1-172.18.0.13:40912;n2-172.18.0.14:40913
## must be unique
dLegerSelfId=n0
sendMessageThreadPoolNums=16


---
File: templates/data/broker/conf/broker1.conf
Size: 200 bytes
Lines: 9
---
brokerClusterName = DefaultCluster
brokerName = broker-abc1
brokerId = 1
deleteWhen = 04
fileReservedTime = 48
brokerRole = ASYNC_MASTER
flushDiskType = ASYNC_FLUSH
brokerIP1 = m30
listenPort = 10921


---
File: templates/data/broker/conf/broker.conf
Size: 188 bytes
Lines: 8
---
brokerClusterName = DefaultCluster
brokerName = broker-abc
brokerId = 0
deleteWhen = 04
fileReservedTime = 48
brokerRole = ASYNC_MASTER
flushDiskType = ASYNC_FLUSH
brokerIP1 = 30.25.90.30


---
File: templates/data/broker2/conf/dledger/broker.conf
Size: 1162 bytes
Lines: 27
---
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

brokerClusterName = RaftCluster
brokerName=RaftNode02
listenPort=30911
#namesrvAddr=127.0.0.1:9876
storePathRootDir=/tmp/rmqstore/node00
storePathCommitLog=/tmp/rmqstore/node00/commitlog
enableDLegerCommitLog=true
dLegerGroup=RaftNode00
dLegerPeers=n0-172.18.0.12:40911;n1-172.18.0.13:40912;n2-172.18.0.14:40913
## must be unique
dLegerSelfId=n2
sendMessageThreadPoolNums=16


---
File: templates/data/broker0/conf/dledger/broker.conf
Size: 1162 bytes
Lines: 27
---
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

brokerClusterName = RaftCluster
brokerName=RaftNode00
listenPort=30911
#namesrvAddr=127.0.0.1:9876
storePathRootDir=/tmp/rmqstore/node00
storePathCommitLog=/tmp/rmqstore/node00/commitlog
enableDLegerCommitLog=true
dLegerGroup=RaftNode00
dLegerPeers=n0-172.18.0.12:40911;n1-172.18.0.13:40912;n2-172.18.0.14:40913
## must be unique
dLegerSelfId=n0
sendMessageThreadPoolNums=16


---
File: templates/data/broker1/conf/dledger/broker.conf
Size: 1162 bytes
Lines: 27
---
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

brokerClusterName = RaftCluster
brokerName=RaftNode01
listenPort=30911
#namesrvAddr=127.0.0.1:9876
storePathRootDir=/tmp/rmqstore/node00
storePathCommitLog=/tmp/rmqstore/node00/commitlog
enableDLegerCommitLog=true
dLegerGroup=RaftNode00
dLegerPeers=n0-172.18.0.12:40911;n1-172.18.0.13:40912;n2-172.18.0.14:40913
## must be unique
dLegerSelfId=n1
sendMessageThreadPoolNums=16


---
File: templates/data/broker2/conf/dledger/broker.conf
Size: 1162 bytes
Lines: 27
---
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

brokerClusterName = RaftCluster
brokerName=RaftNode02
listenPort=30911
#namesrvAddr=127.0.0.1:9876
storePathRootDir=/tmp/rmqstore/node00
storePathCommitLog=/tmp/rmqstore/node00/commitlog
enableDLegerCommitLog=true
dLegerGroup=RaftNode00
dLegerPeers=n0-172.18.0.12:40911;n1-172.18.0.13:40912;n2-172.18.0.14:40913
## must be unique
dLegerSelfId=n2
sendMessageThreadPoolNums=16


---
File: templates/data/broker0/conf/dledger/broker.conf
Size: 1162 bytes
Lines: 27
---
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

brokerClusterName = RaftCluster
brokerName=RaftNode00
listenPort=30911
#namesrvAddr=127.0.0.1:9876
storePathRootDir=/tmp/rmqstore/node00
storePathCommitLog=/tmp/rmqstore/node00/commitlog
enableDLegerCommitLog=true
dLegerGroup=RaftNode00
dLegerPeers=n0-172.18.0.12:40911;n1-172.18.0.13:40912;n2-172.18.0.14:40913
## must be unique
dLegerSelfId=n0
sendMessageThreadPoolNums=16


---
File: templates/data/broker1/conf/dledger/broker.conf
Size: 1162 bytes
Lines: 27
---
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

brokerClusterName = RaftCluster
brokerName=RaftNode01
listenPort=30911
#namesrvAddr=127.0.0.1:9876
storePathRootDir=/tmp/rmqstore/node00
storePathCommitLog=/tmp/rmqstore/node00/commitlog
enableDLegerCommitLog=true
dLegerGroup=RaftNode00
dLegerPeers=n0-172.18.0.12:40911;n1-172.18.0.13:40912;n2-172.18.0.14:40913
## must be unique
dLegerSelfId=n1
sendMessageThreadPoolNums=16


---
File: templates/data/broker2/conf/dledger/broker.conf
Size: 1162 bytes
Lines: 27
---
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

brokerClusterName = RaftCluster
brokerName=RaftNode02
listenPort=30911
#namesrvAddr=127.0.0.1:9876
storePathRootDir=/tmp/rmqstore/node00
storePathCommitLog=/tmp/rmqstore/node00/commitlog
enableDLegerCommitLog=true
dLegerGroup=RaftNode00
dLegerPeers=n0-172.18.0.12:40911;n1-172.18.0.13:40912;n2-172.18.0.14:409