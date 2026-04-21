---
File: dev\local.ini
Size: 287 bytes
Lines: 11
---
; CouchDB Configuration Settings

; Custom settings should be made in this file. They will override settings
; in default.ini, but unlike changes made to default.ini, this file won't be
; overwritten on server upgrade.

[chttpd]
bind_address = any

[httpd]
bind_address = any


---
File: dev-cluster\dockerfile
Size: 104 bytes
Lines: 5
---
FROM debian:buster-slim

COPY docker-entrypoint.sh /usr/local/bin
RUN ln -s usr/local/bin/docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["tini", "--", "/docker-entrypoint.sh"]

VOLUME /opt/couchdb/data

EXPOSE 5984 4369 9100
CMD ["/opt/couchdb/bin/couchdb"]


---
File: nouveau-compose
Size: 1024 bytes
Lines: 51
---
version: '3.8'
services:
  couchdb:
    image: apache/couchdb:3.4.1
    ports:
      - "5984:5984"
      - "4369:4369"
      - "9100:9100"
    volumes:
      - ./data:/opt/couchdb/data
      - ./config:/opt/couchdb/etc
    environment:
      - COUCHDB_USER=admin
      - COUCHDB_PASSWORD=admin
      - COUCHDB_SECRET=secret
    networks:
      - couchdb-net
  couchdb-search:
    image: apache/couchdb:3.4.1
    ports:
      - "5988:5988"
    volumes:
      - ./data:/opt/couchdb/data
      - ./config:/opt/couchdb/etc
    environment:
      - COUCHDB_USER=admin
      - COUCHDB_PASSWORD=admin
      - COUCHDB_SECRET=secret
    networks:
      - couchdb-net
networks:
  couchdb-net:
    driver: bridge
---
End of File

# Apache CouchDB Docker Images

> A semi-official Docker image repository for Apache CouchDB.

This repository provides Docker images for Apache CouchDB, enabling easy deployment and management of CouchDB databases in containerized environments. The images are designed for use in Docker, Kubernetes, and other container orchestration platforms.

---

## 🚀 Overview

Apache CouchDB is a NoSQL document database that supports JSON documents and provides a flexible data model. This repository offers pre-built Docker images for various versions of CouchDB, including stable releases and specialized configurations.

### Key Features

- **Multi-arch support**: Images built for multiple architectures (x86_64, arm64, s390x, etc.)
- **Multiple base images**: Options for Debian and Red Hat UBI (Universal Base Image) platforms
- **Security features**: Enforced user permissions, secure authentication, and secure defaults
- **Flexible configuration**: Easy customization via environment variables
- **Support for search and clustering**: Includes Clouseau (search) and distributed clustering support
- **Docker-specific optimizations**: Proper handling of user permissions, file ownership, and startup scripts

---

## 🔧 Available Versions & Configurations

| Version | Base Image | Features |
|--------|-----------|--------|
| `2.3.1` | Debian | Standard CouchDB |
| `2.3.1-ubi` | Red Hat UBI | OpenShift-compatible, secure base image |
| `3.1.2` | Debian | Standard CouchDB |
| `3.1.2-ubi` | Red Hat UBI | OpenShift-compatible |
| `3.1.2-ubi-clouseau` | Red Hat UBI | Includes Clouseau search functionality |
| `3.2.3`, `3.3.3`, `3.4.1`, `3.4.2`, `3.4.3`, `3.5.0`, `3.5.1` | Debian | Latest stable versions |

> **Note**: All images are built with the latest security and performance best practices.

---

## 🚀 Usage

### Run a Standard CouchDB Instance

```bash
# Using Debian base image
docker run -d -p 5984:5984 \
  --name my-couchdb \
  -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=password \
  apache/couchdb:3.5.1
```

### Run with Custom Configuration

```bash
# Mount a custom config file
docker run -d -p 5984:5984 \
  -v /host/config:/opt/couchdb/etc \
  apache/couchdb:3.5.1
```

### Run with Admin Credentials

```bash
# Set admin credentials via environment variables
docker run -d -p 5984:5984 \
  -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=securepass \
  apache/couchdb:3.5.1
```

### Run with Custom Node Name

```bash
docker run -d -p 5984:5984 \
  -e NODENAME=my-node \
  apache/couchdb:3.5.1
```

---

## 🔒 Security & Best Practices

### Admin Party Mode (Deprecated)

CouchDB 3.0+ **no longer supports** "Admin Party" mode, where the database is accessible without authentication. Starting with version 3.0+, you **must** specify an admin user and password.

> ⚠️ **Warning**: If you see a warning about "Admin Party mode", you must configure an admin user and password using environment variables or custom configuration files.

### Environment Variables

| Variable | Description |
|---------|-------------|
| `COUCHDB_USER` | Username for admin access |
| `COUCHDB_PASSWORD` | Password for admin access |
| `COUCHDB_SECRET` | Secret for HTTP authentication |
| `NODENAME` | Name of the node for clustering |
| `COUCHDB_ERLANG_COOKIE` | Erlang cookie for distributed nodes |

---

## 🚀 Clouseau (Search) Support

For advanced search capabilities, use the `3.1.2-ubi-clouseau` image:

```bash
docker run -d -p 5984:5984 -p 5988:5988 \
  -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=password \
  apache/couchdb:3.1.2-ubi-clouseau
```

This image includes Clouseau, which provides full-text search functionality.

---

## 🌐 Multi-Architecture Support

The images are built for multiple architectures:

- **x86_64** (default)
- **arm64** (Apple Silicon, Raspberry Pi)
- **s390x** (IBM Z systems)

You can pull and run images on any architecture using Docker's multi-arch support:

```bash
docker run --platform linux/arm64 apache/couchdb:3.5.1
```

---

## 🔍 Custom Configuration

You can customize CouchDB behavior by editing configuration files:

- `/opt/couchdb/etc/default.d/10-docker-default.ini`
- `/opt/couchdb/etc/vm.args`

These files are automatically created and written to during startup.

---

## 📦 Build & Development

### Build Images Locally

Use the `build.sh` script to build and push images:

```bash
# Build a specific version
./build.sh buildx 3.5.1

# Build and tag with a custom name
./build.sh buildx 3.5.1 as latest
```

### Build for Specific Platform

```bash
# Build for arm64
./build.sh buildx 3.5.1 --platform linux/arm64
```

---

## 🚀 Docker Compose Example

A sample `docker-compose.yml` for a CouchDB cluster:

```yaml
version: '3.8'
services:
  couchdb:
    image: apache/couchdb:3.4.1
    ports:
      - "5984:5984"
      - "4369:4369"
      - "9100:9100"
    environment:
      - COUCHDB_USER=admin
      - COUCHDB_PASSWORD=admin
      - COUCHDB_SECRET=secret
    volumes:
      - ./data:/opt/couchdb/data
    networks:
      - couchdb-net
  couchdb-search:
    image: apache/couchdb:3.1.2-ubi-clouseau
    ports:
      - "5988:5988"
    environment:
      - COUCHDB_USER=admin
      - COUCHDB_PASSWORD=admin
      - COUCHDB_SECRET=secret
    volumes:
      - ./data:/opt/couchdb/data
    networks:
      - couchdb-net
networks:
  couchdb-net:
    driver: bridge
```

---

## 📚 Documentation

- [Apache CouchDB Documentation](https://docs.couchdb.org/en/latest/)
- [Docker Documentation](https://docs.docker.com/)

---

## 📝 License

This project is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for details.

---

## 📞 Support & Feedback

For questions, issues, or feature requests:

- **GitHub Issues**: https://github.com/apache/couchdb-docker/issues
- **Mailing List**: dev@couchdb.apache.org
- **Community**: Apache CouchDB Community

> This is a semi-official repository. The Apache Software Foundation does not endorse any specific configuration or use case.

---
End of File

```markdown
# Apache CouchDB Docker Images

> A semi-official Docker image repository for Apache CouchDB.

This repository provides Docker images for Apache CouchDB, enabling easy deployment and management of CouchDB databases in containerized environments. The images are designed for use in Docker, Kubernetes, and other container orchestration platforms.

---

## 🚀 Overview

Apache CouchDB is a NoSQL document database that supports JSON documents and provides a flexible data model. This repository offers pre-built Docker images for various versions of CouchDB, including stable releases and specialized configurations.

### Key Features

- **Multi-arch support**: Images built for multiple architectures (x86_64, arm64, s390x, etc.)
- **Multiple base images**: Options for Debian and Red Hat UBI (Universal Base Image) platforms
- **Security features**: Enforced user permissions, secure authentication, and secure defaults
- **Flexible configuration**: Easy customization via environment variables
- **Support for search and clustering**: Includes Clouseau (search) and distributed clustering support
- **Docker-specific optimizations**: Proper handling of user permissions, file ownership, and startup scripts

---

## 🔧 Available Versions & Configurations

| Version | Base Image | Features |
|--------|-----------|--------|
| `2.3.1` | Debian | Standard CouchDB |
| `2.3.1-ubi` | Red Hat UBI | OpenShift-compatible, secure base image |
| `3.1.2` | Debian | Standard CouchDB |
| `3.1.2-ubi` | Red Hat UBI | OpenShift-compatible |
| `3.1.2-ubi-clouseau` | Red Hat UBI | Includes Clouseau search functionality |
| `3.2.3`, `3.3.3`, `3.4.1`, `3.4.2`, `3.4.3`, `3.5.0`, `3.5.1` | Debian | Latest stable versions |

> **Note**: All images are built with the latest security and performance best practices.

---

## 🚀 Usage

### Run a Standard CouchDB Instance

```bash
# Using Debian base image
docker run -d -p 5984:5984 \
  --name my-couchdb \
  -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=password \
  apache/couchdb:3.5.1
```

### Run with Custom Configuration

```bash
# Mount a custom config file
docker run -d -p 5984:5984 \
  -v /host/config:/opt/couchdb/etc \
  apache/couchdb:3.5.1
```

### Run with Admin Credentials

```bash
# Set admin credentials via environment variables
docker run -d -p 5984:5984 \
  -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=securepass \
  apache/couchdb:3.5.1
```

### Run with Custom Node Name

```bash
docker run -d -p 5984:5984 \
  -e NODENAME=my-node \
  apache/couchdb:3.5.1
```

---

## 🔒 Security & Best Practices

### Admin Party Mode (Deprecated)

CouchDB 3.0+ **no longer supports** "Admin Party" mode, where the database is accessible without authentication. Starting with version 3.0+, you **must** specify an admin user and password.

> ⚠️ **Warning**: If you see a warning about "Admin Party mode", you must configure an admin user and password using environment variables or custom configuration files.

### Environment Variables

| Variable | Description |
|---------|-------------|
| `COUCHDB_USER` | Username for admin access |
| `COUCHDB_PASSWORD` | Password for admin access |
| `COUCHDB_SECRET` | Secret for HTTP authentication |
| `NODENAME` | Name of the node for clustering |
| `COUCHDB_ERLANG_COOKIE` | Erlang cookie for distributed nodes |

---

## 🚀 Clouseau (Search) Support

For advanced search capabilities, use the `3.1.2-ubi-clouseau` image:

```bash
docker run -d -p 5984:5984 -p 5988:5988 \
  -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=password \
  apache/couchdb:3.1.2-ubi-clouseau
```

This image includes Clouseau, which provides full-text search functionality.

---

## 🌐 Multi-Architecture Support

The images are built for multiple architectures:

- **x86_64** (default)
- **arm64** (Apple Silicon, Raspberry Pi)
- **s390x** (IBM Z systems)

You can pull and run images on any architecture using Docker's multi-arch support:

```bash
docker run --platform linux/arm64 apache/couchdb:3.5.1
```

---

## 🔍 Custom Configuration

You can customize CouchDB behavior by editing configuration files:

- `/opt/couchdb/etc/default.d/10-docker-default.ini`
- `/opt/couchdb/etc/vm.args`

These files are automatically created and written to during startup.

---

## 📦 Build & Development

### Build Images Locally

Use the `build.sh` script to build and push images:

```bash
# Build a specific version
./build.sh buildx 3.5.1

# Build and tag with a custom name
./build.sh buildx 3.5.1 as latest
```

### Build for Specific Platform

```bash
# Build for arm64
./build.sh buildx 3.5.1 --platform linux/arm64
```

---

## 🚀 Docker Compose Example

A sample `docker-compose.yml` for a CouchDB cluster:

```yaml
version: '3.8'
services:
  couchdb:
    image: apache/couchdb:3.4.1
    ports:
      - "5984:5984"
      - "4369:4369"
      - "9100:9100"
    environment:
      - COUCHDB_USER=admin
      - COUCHDB_PASSWORD=admin
      - COUCHDB_SECRET=secret
    volumes:
      - ./data:/opt/couchdb/data
    networks:
      - couchdb-net
  couchdb-search:
    image: apache/couchdb:3.1.2-ubi-clouseau
    ports:
      - "5988:5988"
    environment:
      - COUCHDB_USER=admin
      - COUCHDB_PASSWORD=admin
      - COUCHDB_SECRET=secret
    volumes:
      - ./data:/opt/couchdb/data
    networks:
      - couchdb-net
networks:
  couchdb-net:
    driver: bridge
```

---

## 📚 Documentation

- [Apache CouchDB Documentation](https://docs.couchdb.org/en/latest/)
- [Docker Documentation](https://docs.docker.com/)

---

## 📝 License

This project is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for details.

---

## 📞 Support & Feedback

For questions, issues, or feature requests:

- **GitHub Issues**: https://github.com/apache/couchdb-docker/issues
- **Mailing List**: dev@couchdb.apache.org
- **Community**: Apache CouchDB Community

> This is a semi-official repository. The Apache Software Foundation does not endorse any specific configuration or use case.