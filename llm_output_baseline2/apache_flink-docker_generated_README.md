---
File: .asf.yaml
Size: 218 bytes
Lines: 10
---
github:
  description: "Docker packaging for Apache Flink"
  homepage: https://flink.apache.org/
  labels:
    - flink
    - docker
  enabled_merge_buttons:
    squash: true
    merge: false
    rebase: true


---
File: .gitignore
Size: 36 bytes
Lines: 5
---
.*.swp
.idea
dev
*.iml
.vscode


---
File: common.sh
Size: 2454 bytes
Lines: 71
---
#!/usr/bin/env bash


#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


# get the most recent commit which modified any of "$@"
fileCommit() {
    git log -1 --format='format:%H' HEAD -- "$@"
}

# get the most recent commit which modified "$1/Dockerfile" or any file COPY'd from "$1/Dockerfile"
dirCommit() {
    local dir="$1"; shift
    (
        cd "$dir"
        fileCommit \
            Dockerfile \
            $(git show HEAD:./Dockerfile | awk '
                toupper($1) == "COPY" {
                    for (i = 2; i < NF; i++) {
                        print $i
                    }
                }
            ')
    )
}

# Inputs:
#  - tags: comma-seprated list of image tags
#  - latestVersion: latest version
# Output: comma-separated list of tags with "latest" removed if not latest version
pruneTags() {
    local tags=$1
    local latestVersion=$2
    # Escape dots in version for proper regex matching
    local escapedVersion="${latestVersion//./\\.}"
    if [[ $tags =~ (^|[, ])$escapedVersion([, -]|$) ]]; then
        # tags contains latest version. keep "latest" tag
        echo $tags
    else
        # remove "latest", any "scala_" or "javaXX" tag, unless it is the latest version
        # the "scala" / "java" tags have a similar semantic as the "latest" tag in docker registries.
        echo $tags | sed -E 's#, (scala|latest|java[0-9]{1,2})[-_.[:alnum:]]*##g'
    fi
}

extractValue() {
    local key="$1"
    local file="$2"
    local line=$(cat $file | grep "$key:")
    echo $line | sed "s/${key}: //g"
}

# get latest flink version
latest_version=`ls -1a | grep -E "[0-9]+.[0-9]+" | sort -V -r | head -n 1`


---
File: generate-stackbrew-library-docker.sh
Size: 402 bytes
Lines: 16
---
#!/usr/bin/env bash

# How to recreate below docker image
# 
# $ cat Dockerfile
# FROM ubuntu:16.04
# RUN apt-get update ; apt-get install -y git bash
# 
# $ docker build -t rmetzger/git-and-bash:latest .
# $ docker push rmetzger/git-and-bash:latest
#

exec docker run --rm \
    --volume "${PWD}:/build:ro" \
    rmetzger/git-and-bash:latest \
    /build/generate-stackbrew-library.sh


---
File: generate-stackbrew-library.sh
Size: 1981 bytes
Lines: 61
---
#!/usr/bin/env bash

#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# This script generates a manifest compatibile with the expectations set forth
# by docker-library/official-images.
#
# It is not compatible with the version of Bash currently shipped with OS X due
# to the use of features introduced in Bash 4.

set -eu

self="$(basename "$BASH_SOURCE")"
cd "$(dirname "$(readlink -f "$BASH_SOURCE")")"

source common.sh

cat <<-EOH
# this file is generated via https://github.com/apache/flink-docker/blob/$(fileCommit "$self")/$self

Maintainers: The Apache Flink Project <dev@flink.apache.org> (@ApacheFlink)
GitRepo: https://github.com/apache/flink-docker.git
EOH


for dockerfile in $(find . -name "Dockerfile" | sort -r); do
    dir=$(dirname $dockerfile)

    commit="$(dirCommit "$dir")"
    metadata="$dir/release.metadata"
    architectures=$(extractValue "Architectures" $metadata)
    tags=$(extractValue "Tags" $metadata)
    tags=$(pruneTags "$tags" $latest_version)

    # newline
    echo

    # The tabs here are necessary for the heredoc to work right
    cat <<-EOE
		Tags: $tags
		Architectures: $architectures
		GitCommit: $commit
		Directory: $dir
	EOE

done


---
File: publish-to-dockerhub.sh
Size: 7010 bytes
Lines: 196
---
#!/usr/bin/env bash

#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# This script copies Flink docker images from GHCR to Docker Hub.
# It uses crane to efficiently copy images without pulling them locally.
#
# Prerequisites:
#   - crane installed (https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md)
#   - Authentication to Docker Hub (docker login)
#
# Usage:
#   ./publish-to-dockerhub.sh [--dry-run]
#   SOURCE_REGISTRY=ghcr.io/myorg/flink-docker TARGET_REGISTRY=myorg/flink ./publish-to-dockerhub.sh
#   ./publish-to-dockerhub.sh --dry-run  # Test without actually copying

set -euo pipefail

# Parse command line arguments
DRY_RUN=false
for arg in "$@"; do
    case $arg in
        --dry-run|-n)
            DRY_RUN=true
            shift
            ;;
        --help|-h)
            echo "Usage: $0 [--dry-run]"
            echo ""
            echo "Options:"
            echo "  --dry-run, -n    Show what would be copied without actually copying"
            echo "  --help, -h       Show this help message"
            echo ""
            echo "Environment variables:"
            echo "  SOURCE_REGISTRY  Source registry (default: ghcr.io/apache/flink-docker)"
            echo "  TARGET_REGISTRY  Target registry (default: apache/flink)"
            exit 0
            ;;
        *)
            echo "Unknown option: $arg"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

self="$(basename "$BASH_SOURCE")"
cd "$(dirname "$(readlink -f "$BASH_SOURCE")")"

source common.sh

# Configuration
SOURCE_REGISTRY=${SOURCE_REGISTRY:-"ghcr.io/apache/flink-docker"}
TARGET_REGISTRY=${TARGET_REGISTRY:-"apache/flink"}

echo "============================================"
echo "Publishing Flink Docker Images"
if [ "$DRY_RUN" = true ]; then
    echo "🔍 DRY RUN MODE - No images will be copied"
fi
echo "============================================"
echo "Source: $SOURCE_REGISTRY"
echo "Target: $TARGET_REGISTRY"
echo "============================================"
echo ""

# Confirmation check
if [ "$DRY_RUN" = false ]; then
    echo "⚠️  IMPORTANT: Before running this script, ensure that:"
    echo ""
    echo "1. The GitHub Actions workflow 'Build and Push Docker Images' has"
    echo "   completed successfully for the release you want to publish"
    echo ""
    echo "2. All Docker images are available in GHCR at:"
    echo "   https://github.com/orgs/apache/packages?repo_name=flink-docker"
    echo "   (or https://github.com/users/${USER}/packages if using a fork)"
    echo ""
    echo "3. The images were built from the correct branch/tag"
    echo "   - For releases: master branch"
    echo "   - For testing: dev-* branches"
    echo ""
    echo "4. You are authenticated to Docker Hub:"
    echo "   docker login"
    echo ""
    read -p "Have you verified the above? (yes/no): " -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy][Ee][Ss]$ ]]; then
        echo "❌ Aborted. Please verify the build workflow completed successfully first."
        exit 1
    fi

    echo "✅ Proceeding with image publication..."
    echo ""
else
    echo "🔍 Dry-run mode: Will verify images exist and show what would be copied"
    echo ""
fi

# Check if crane is installed
if ! command -v crane &> /dev/null; then
    echo "ERROR: crane is not installed"
    echo "Please install crane from: https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md"
    echo ""
    echo "Quick install:"
    echo "  macOS:   brew install crane"
    echo "  Linux:   go install github.com/google/go-containerregistry/cmd/crane@latest"
    exit 1
fi

# Process each Dockerfile
for dockerfile in $(find . -name "Dockerfile" | sort); do
    dir=$(dirname "$dockerfile")

    # Extract version and java version from Dockerfile
    FLINK_VERSION=$(grep "FLINK_TGZ_URL=" "$dockerfile" | head -1 | sed -E 's/.*flink-([0-9]+\.[0-9]+\.[0-9]+).*/\1/')

    # Extract java version from directory name (e.g., scala_2.12-java11-ubuntu -> java11)
    JAVA_VERSION=$(basename "$dir" | sed -E 's/.*-java([0-9]+)-.*/\1/')

    if [ -z "$FLINK_VERSION" ] || [ -z "$JAVA_VERSION" ]; then
        echo "⚠️  Skipping $dir - could not extract version info"
        continue
    fi

    # Construct source image tag
    SOURCE_TAG="${FLINK_VERSION}-scala_2.12-java${JAVA_VERSION}"
    SOURCE_IMAGE="${SOURCE_REGISTRY}:${SOURCE_TAG}"

    # Read target tags from metadata
    metadata="$dir/release.metadata"
    if [ ! -f "$metadata" ]; then
        echo "⚠️  Skipping $dir - no metadata file found"
        continue
    fi

    tags=$(extractValue "Tags" "$metadata")
    tags=$(pruneTags "$tags" "$latest_version")

    echo "📦 Processing Flink ${FLINK_VERSION} Java ${JAVA_VERSION}"
    echo "   Source: ${SOURCE_IMAGE}"

    # Check if source image exists
    if ! crane manifest "$SOURCE_IMAGE" &> /dev/null; then
        echo "   ❌ ERROR: Source image not found in GHCR"
        echo "   Please ensure the image was built and pushed by the CI workflow"
        echo ""
        echo "Aborting: Cannot proceed with missing images"
        exit 1
    fi

    # Copy to each target tag
    IFS=',' read -ra TAGS_ARRAY <<< "$tags"
    for raw_tag in "${TAGS_ARRAY[@]}"; do
        # Trim whitespace
        tag=$(echo "$raw_tag" | xargs)
        TARGET_IMAGE="${TARGET_REGISTRY}:${tag}"

        if [ "$DRY_RUN" = true ]; then
            echo "   🔍 Would copy to ${TARGET_IMAGE}"
        else
            echo "   📤 Copying to ${TARGET_IMAGE}"
            if crane copy "$SOURCE_IMAGE" "$TARGET_IMAGE"; then
                echo "      ✅ Success"
            else
                echo "      ❌ Failed"
                exit 1
            fi
        fi
    done

    echo ""
done

echo "============================================"
if [ "$DRY_RUN" = true ]; then
    echo "🔍 Dry-run completed successfully!"
    echo "Run without --dry-run to actually copy images."
else
    echo "✅ All images published successfully!"
fi
echo "============================================"


---
File: 1.20\scala_2.12-java11-ubuntu\Dockerfile
Size: 4638 bytes
Lines: 103
---
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
###

FROM eclipse-temurin:11-jre-jammy

# Install dependencies
RUN set -ex; \
  apt-get update; \
  apt-get -y install gpg libsnappy1v5 gettext-base libjemalloc-dev; \
  rm -rf /var/lib/apt/lists/*

# Grab gosu for easy step-down from root
ENV GOSU_VERSION 1.11
RUN set -ex; \
  wget -nv -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)"; \
  wget -nv -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc"; \
  export GNUPGHOME="$(mktemp -d)"; \
  for server in hkps://keys.openpgp.org $(shuf -e \
                          keyserver.ubuntu.com \
                          hkp://keyserver.ubuntu.com:80 \
                          pgp.mit.edu) ; do \
      gpg --batch --keyserver "$server" --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 && break || : ; \
  done && \
  gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \
  gpgconf --kill all; \
  rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc; \
  chmod +x /usr/local/bin/gosu; \
  gosu nobody true

# Configure Flink version
ENV FLINK_TGZ_URL=https://dlcdn.apache.org/flink/flink-1.20.3/flink-1.20.3-bin-scala_2.12.tgz \
    FLINK_ASC_URL=https://downloads.apache.org/flink/flink-1.20.3/flink-1.20.3-bin-scala_2.12.tgz.asc \
    GPG_KEY=5EE2CDBE52BDDB9CCB1C63B6E6BAF9CFABD4ED71 \
    CHECK_GPG=true

# Prepare environment
ENV FLINK_HOME=/opt/flink
ENV PATH=$FLINK_HOME/bin:$PATH
RUN groupadd --system --gid=9999 flink && \
    useradd --system --home-dir $FLINK_HOME --uid=9999 --gid=flink flink
WORKDIR $FLINK_HOME

# Install Flink
RUN set -ex; \
  wget -nv -O flink.tgz "$FLINK_TGZ_URL"; \
  \
  if [ "$CHECK_GPG" = "true" ]; then \
    wget -nv -O flink.tgz.asc "$FLINK_ASC_URL"; \
    export GNUPGHOME="$(mktemp -d)"; \
    for server in hkps://keys.openpgp.org $(shuf -e \
                            keyserver.ubuntu.com \
                            hkp://keyserver.ubuntu.com:80 \
                            pgp.mit.edu) ; do \
        gpg --batch --keyserver "$server" --recv-keys "$GPG_KEY" && break || : ; \
    done && \
    gpg --batch --verify flink.tgz.asc flink.tgz; \
    gpgconf --kill all; \
    rm -rf "$GNUPGHOME" flink.tgz.asc; \
  fi; \
  \
  tar -xf flink.tgz --strip-components=1; \
  rm flink.tgz; \
  \
  chown -R flink:flink .; \
  \
  # Replace default REST/RPC endpoint bind address to use the container's network interface \
  CONF_FILE="$FLINK_HOME/conf/flink-conf.yaml"; \
  if [ ! -e "$FLINK_HOME/conf/flink-conf.yaml" ]; then \
    CONF_FILE="${FLINK_HOME}/conf/config.yaml"; \
    /bin/bash "$FLINK_HOME/bin/config-parser-utils.sh" "${FLINK_HOME}/conf" "${FLINK_HOME}/bin" "${FLINK_HOME}/lib" \
        "-repKV" "rest.address,localhost,0.0.0.0" \
        "-repKV" "rest.bind-address,localhost,0.0.0.0" \
        "-repKV" "jobmanager.bind-host,localhost,0.0.0.0" \
        "-repKV" "taskmanager.bind-host,localhost,0.0.0.0" \
        "-rmKV" "taskmanager.host=localhost"; \
  else \
    sed -i 's/rest.address: localhost/rest.address: 0.0.0.0/g' "$CONF_FILE"; \
    sed -i 's/rest.bind-address: localhost/rest.bind-address: 0.0.0.0/g' "$CONF_FILE"; \
    sed -i 's/jobmanager.bind-host: localhost/jobmanager.bind-host: 0.0.0.0/g' "$CONF_FILE"; \
    sed -i 's/taskmanager.bind-host: localhost/taskmanager.bind-host: 0.0.0.0/g' "$CONF_FILE"; \
    sed -i '/taskmanager.host: localhost/d' "$CONF_FILE"; \
  fi;

# Configure container
COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 6123 8081
CMD ["help"]


---
File: 1.20\scala_2.12-java17-ubuntu\Dockerfile
Size: 4638 bytes
Lines: 103
---
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
# limitations under the License.
###

FROM eclipse-temurin:17-jre-jammy

# Install dependencies
RUN set -ex; \
  apt-get update; \
  apt-get -y install gpg libsnappy1v5 gettext-base libjemalloc-dev; \
  rm -rf /var/lib/apt/lists/*

# Grab gosu for easy step-down from root
ENV GOSU_VERSION 1.11
RUN set -ex; \
  wget -nv -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)"; \
  wget -nv -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc"; \
  export GNUPGHOME="$(mktemp -d)"; \
  for server in hkps://keys.openpgp.org $(shuf -e \
                          keyserver.ubuntu.com \
                          hkp://keyserver.ubuntu.com:80 \
                          pgp.mit.edu