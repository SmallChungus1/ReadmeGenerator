---
File: dev-cluster/Dockerfile
Size: 2875 bytes
Lines: 95
---
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

# Base layer containing dependencies needed at runtime. This layer will be
# cached after the initial build.
FROM debian:buster

MAINTAINER CouchDB Developers dev@couchdb.apache.org

# Add CouchDB user account
RUN groupadd -r couchdb && useradd -d /opt/couchdb -g couchdb couchdb

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    dirmngr \
    gnupg \
    haproxy \
    libicu63 \
    libmozjs-60-0 \
    openssl && \
  rm -rf /var/lib/apt/lists/*

# grab tini for signal handling
# see https://github.com/apache/couchdb-docker/pull/28#discussion_r141112407
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends tini; \
    rm -rf /var/lib/apt/lists/*; \
    tini --version

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    apt-transport-https \
    build-essential \
    erlang-nox \
    erlang-reltool \
    erlang-dev \
    git \
    libcurl4-openssl-dev \
    libicu-dev \
    libmozjs-60-dev \
    python3 \
    libpython3-dev \
    python3-pip \
    python3-sphinx \
    python3-setuptools

RUN pip3 install --upgrade \
    sphinx_rtd_theme \
    nose \
    requests \
    hypothesis

# Node is special
RUN set -ex; \
    curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -; \
    echo 'deb https://deb.nodesource.com/node_10.x buster main' > /etc/apt/sources.list.d/nodesource.list; \
    echo 'deb-src https://deb.nodesource.com/node_10.x buster main' >> /etc/apt/sources.list.d/nodesource.list; \
    apt-get update -y && apt-get install -y nodejs; \
    npm install -g grunt-cli


# Clone CouchDB source code including all dependencies
ARG clone_url=https://gitbox.apache.org/repos/asf/couchdb.git
RUN git clone $clone_url /usr/src/couchdb
WORKDIR /usr/src/couchdb
RUN ./configure -c --spidermonkey-version 60

ARG checkout_branch=main
ARG configure_options="-c --spidermonkey-version 60"

WORKDIR /usr/src/couchdb/
RUN git fetch origin \
    && git checkout $checkout_branch \
    && ./configure $configure_options \
    && make all

# Setup directories and permissions
RUN chown -R couchdb:couchdb /usr/src/couchdb

WORKDIR /opt/couchdb
EXPOSE 5984 15984 25984 35984
VOLUME ["/usr/src/couchdb/dev/lib"]

ENTRYPOINT ["tini", "--", "/usr/src/couchdb/dev/run"]
CMD ["--with-haproxy"]


---
File: 3.4.3-nouveau/nouveau.yaml
Size: 462 bytes
Lines: 27
---
maxIndexesOpen: 3000
commitIntervalSeconds: 30
idleSeconds: 60
rootDir: ./data/nouveau

logging:
  level: INFO

server:
  applicationConnectors:
    - type: http
      bindHost: 0.0.0.0
      port: 5987
      useDateHeader: false
  adminConnectors:
    - type: http
      bindHost: 0.0.0.0
      port: 5988
      useDateHeader: false
  gzip:
    includedMethods:
      - GET
      - POST
  requestLog:
    appenders:
      - type: console
        target: stderr


---
File: 3.4.3-nouveau/Dockerfile
Size: 3356 bytes
Lines: 88
---
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

FROM debian:bookworm-slim

LABEL maintainer="CouchDB Developers dev@couchdb.apache.org"

# Add CouchDB user account to make sure the IDs are assigned consistently
RUN groupadd -g 5984 -r nouveau && useradd -u 5984 -d /opt/nouveau -g nouveau nouveau

# be sure GPG and apt-transport-https are available and functional
RUN set -ex; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        apt-transport-https \
        ca-certificates \
        dirmngr \
        gnupg \
     ; \
    rm -rf /var/lib/apt/lists/*

# Nouveau wants a JRE/JDK
RUN set -ex; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        openjdk-17-jre-headless \
     ; \
    rm -rf /var/lib/apt/lists/*

# grab tini for signal handling and zombie reaping
# see https://github.com/apache/couchdb-docker/pull/28#discussion_r141112407
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends tini; \
    rm -rf /var/lib/apt/lists/*; \
    tini --version

# http://docs.couchdb.org/en/latest/install/unix.html#installing-the-apache-couchdb-packages
# gpg: rsa8192 205-01-19 The Apache Software Foundation (Package repository signing key) <root@apache.org>

ENV GPG_COUCH_KEY 390EF70BB1EA12B2773962950EE62FB37A00258D

RUN set -eux; \
   apt-get update; \
   apt-get install -y curl; \
   export GNUPGHOME="$(mktemp -d)"; \
   curl -fL -o keys.asc https://couchdb.apache.org/repo/keys.asc; \
   gpg --batch --import keys.asc; \
   gpg --batch --export "${GPG_COUCH_KEY}" > /usr/share/keyrings/couchdb-archive-keyring.gpg; \
   command -v gpgconf && gpgconf --kill all || :; \
   rm -rf "$GNUPGHOME"; \
   apt-key list; \
   apt purge -y --autoremove curl; \
   rm -rf /var/lib/apt/lists/*

RUN . /etc/os-release; \
   echo "deb [signed-by=/usr/share/keyrings/couchdb-archive-keyring.gpg] https://apache.jfrog.io/artifactory/couchdb-deb/ bookworm main" | \
       tee /etc/apt/sources.list.d/couchdb.list >/dev/null

# https://github.com/apache/couchdb-pkg/blob/master/debian/README.Debian
RUN set -eux; \
    apt-get update; \
    \
    echo "couchdb-nouveau couchdb-nouveau/enable select false" | debconf-set-selections; \
    DEBIAN_FRONTEND=noninteractive COUCHDB_NOUVEAU_ENABLE=1 apt-get install -y --allow-downgrades --allow-remove-essential --allow-change-held-packages --no-install-recommends \
            couchdb-nouveau=3.4.3~bookworm; \
    rm -rf /var/lib/apt/lists/*; \
    chown -R nouveau:nouveau /opt/nouveau

COPY --chown=nouveau:nouveau nouveau.yaml /opt/nouveau/etc/nouveau.yaml

VOLUME /opt/nouveau/data

# 5987: Nouveau App
# 5988: Nouveau Admin
EXPOSE 5987 5988

# TODO: re-add tini
CMD ["/usr/bin/java", "-server", "-Djava.awt.headless=true", "-Xmx2g", "-jar", "/opt/nouveau/lib/nouveau-1.0-SNAPSHOT.jar", "server", "/opt/nouveau/etc/nouveau.yaml"]


---
File: 3.2.3/10-docker-default.ini
Size: 248 bytes
Lines: 8
---
; CouchDB Configuration Settings

; Custom settings should be made in this file. They will override settings
; in default.ini, but unlike changes made to default.ini, this file won't be
; overwritten on server upgrade.

[chttpd]
bind_address = any


---
File: 3.2.3/docker-entrypoint.sh
Size: 5149 bytes
Lines: 122
---
#!/bin/bash
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

set -e

# first arg is `-something` or `+something`
if [ "${1#-}" != "$1" ] || [ "${1#+}" != "$1" ]; then
	set -- /opt/couchdb/bin/couchdb "$@"
fi

# first arg is the bare word `couchdb`
if [ "$1" = 'couchdb' ]; then
	shift
	set -- /opt/couchdb/bin/couchdb "$@"
fi

if [ "$1" = '/opt/couchdb/bin/couchdb' ]; then
	# this is where runtime configuration changes will be written.
	# we need to explicitly touch it here in case /opt/couchdb/etc has
	# been mounted as an external volume, in which case it won't exist.
	# If running as the couchdb user (i.e. container starts as root),
	# write permissions will be granted below.
	touch /opt/couchdb/etc/local.d/docker.ini

	# if user is root, assume running under the couchdb user (default)
	# and ensure it is able to access files and directories that may be mounted externally
	if [ "$(id -u)" = '0' ]; then
		# Check that we own everything in /opt/couchdb and fix if necessary. We also
		# add the `-f` flag in all the following invocations because there may be
		# cases where some of these ownership and permissions issues are non-fatal
		# (e.g. a config file owned by root with o+r is actually fine), and we don't
		# to be too aggressive about crashing here ...
		find /opt/couchdb \! \( -user couchdb -group couchdb \) -exec chown -f couchdb:couchdb '{}' +

		# Ensure that data files have the correct permissions. We were previously
		# preventing any access to these files outside of couchdb:couchdb, but it
		# turns out that CouchDB itself does not set such restrictive permissions
		# when it creates the files. The approach taken here ensures that the
		# contents of the datadir have the same permissions as they had when they
		# were initially created. This should minimize any startup delay.
		find /opt/couchdb/data -type d ! -perm 0755 -exec chmod -f 0755 '{}' +
		find /opt/couchdb/data -type f ! -perm 0644 -exec chmod -f 0644 '{}' +

		# Do the same thing for configuration files and directories. Technically
		# CouchDB only needs read access to the configuration files as all online
		# changes will be applied to the "docker.ini" file below, but we set 644
		# for the sake of consistency.
		find /opt/couchdb/etc -type d ! -perm 0755 -exec chmod -f 0755 '{}' +
		find /opt/couchdb/etc -type f ! -perm 0644 -exec chmod -f 0644 '{}' +
	fi

	if [ ! -z "$NODENAME" ] && ! grep "couchdb@" /opt/couchdb/etc/vm.args; then
		echo "-name couchdb@$NODENAME" >> /opt/couchdb/etc/vm.args
	fi

	if [ "$COUCHDB_USER" ] && [ "$COUCHDB_PASSWORD" ]; then
		# Create admin only if not already present
		if ! grep -Pzoqr "\[admins\]\n$COUCHDB_USER =" /opt/couchdb/etc/local.d/*.ini /opt/couchdb/etc/local.ini; then
			printf "\n[admins]\n%s = %s\n" "$COUCHDB_USER" "$COUCHDB_PASSWORD" >> /opt/couchdb/etc/local.d/docker.ini
		fi
	fi

	if [ "$COUCHDB_SECRET" ]; then
		# Set secret only if not already present
		if ! grep -Pzoqr "\[chttpd_auth\]\nsecret =" /opt/couchdb/etc/local.d/*.ini /opt/couchdb/etc/local.ini; then
			printf "\n[chttpd_auth]\nsecret = %s\n" "$COUCHDB_SECRET" >> /opt/couchdb/etc/local.d/docker.ini
		fi
	fi

	if [ "$COUCHDB_ERLANG_COOKIE" ]; then
		cookieFile='/opt/couchdb/.erlang.cookie'
		if [ -e "$cookieFile" ]; then
			if [ "$(cat "$cookieFile" 2>/dev/null)" != "$COUCHDB_ERLANG_COOKIE" ]; then
				echo >&2
				echo >&2 "warning: $cookieFile contents do not match COUCHDB_ERLANG_COOKIE"
				echo >&2
			fi
		else
			echo "$COUCHDB_ERLANG_COOKIE" > "$cookieFile"
		fi
		chown couchdb:couchdb "$cookieFile"
		chmod 600 "$cookieFile"
	fi

	if [ "$(id -u)" = '0' ]; then
		chown -f couchdb:couchdb /opt/couchdb/etc/local.d/docker.ini || true
	fi

	# if we don't find an [admins] section followed by a non-comment, display a warning
        if ! grep -Pzoqr '\[admins\]\n[^;]\w+' /opt/couchdb/etc/default.d/*.ini /opt/couchdb/etc/local.d/*.ini /opt/couchdb/etc/local.ini; then
		# The - option suppresses leading tabs but *not* spaces. :)
		cat >&2 <<-'EOWARN'
*************************************************************
ERROR: CouchDB 3.0+ will no longer run in "Admin Party"
       mode. You *MUST* specify an admin user and
       password, either via your own .ini file mapped
       into the container at /opt/couchdb/etc/local.ini
       or inside /opt/couchdb/etc/local.d, or with
       "-e COUCHDB_USER=admin -e COUCHDB_PASSWORD=password"
       to set it via "docker run".
*************************************************************
EOWARN
		exit 1
	fi

	if [ "$(id -u)" = '0' ]; then
		export HOME=$(echo ~couchdb)
		exec setpriv --reuid=couchdb --regid=couchdb --clear-groups "$@"
	fi
fi

exec "$@"


---
File: 3.5.0/10-docker-default.ini
Size: 248 bytes
Lines: 8
---
; CouchDB Configuration Settings

; Custom settings should be made in this file. They will override settings
; in default.ini, but unlike changes made to default.ini, this file won't be
; overwritten on server upgrade.

[chttpd]
bind_address = any


---
File: 3.5.0/docker-entrypoint.sh
Size: 5149 bytes
Lines: 122
---
#!/bin/bash
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

set -e

# first arg is `-something` or `+something`
if [ "${1#-}" != "$1" ] || [ "${1#+}" != "$1" ]; then
	set -- /opt/couchdb/bin/couchdb "$@"
fi

# first arg is the bare word `couchdb`
if [ "$1" = 'couchdb' ]; then
	shift
	set -- /opt/couchdb/bin/couchdb "$@"
fi

if [ "$1" = '/opt/couchdb/bin/couchdb' ]; then
	# this is where runtime configuration changes will be written.
	# we need to explicitly touch it here in case /opt/couchdb/etc has
	# been mounted as an external volume, in which case it won't exist.
	# If running as the couchdb user (i.e. container starts as root),
	# write permissions will be granted below.
	touch /opt/couchdb/etc/local.d/docker.ini

	# if user is root, assume running under the couchdb user (default)
	# and ensure it is able to access files and directories that may be mounted externally
	if [ "$(id -u)" = '0' ]; then
		# Check that we own everything in /opt/couchdb and fix if necessary. We also
		# add the `-f` flag in all the following invocations because there may be
		# cases where some of these ownership and permissions issues are non-fatal
		# (e.g. a config file owned by root with o+r is actually fine), and we don't
		# to be too aggressive about crashing here ...
		find /opt/couchdb \! \( -user couchdb -group couchdb \) -exec chown -f couchdb:couchdb '{}' +

		# Ensure that data files have the correct permissions. We were previously
		# preventing any access to these files outside of couchdb:couchdb, but it
		# turns out that CouchDB itself does not set such restrictive permissions
		# when it creates the files. The approach taken here ensures that the
		# contents of the datadir have the same permissions as they had when they
		# were initially created. This should minimize any startup delay.
		find /opt/couchdb/data -type d ! -perm 0755 -exec chmod -f 0755 '{}' +
		find /opt/couchdb/data -type f ! -perm 0644 -exec chmod -f 0644 '{}' +

		# Do the same thing for configuration files and directories. Technically
		# CouchDB only needs read access to the configuration files as all online
		# changes will be applied to the "docker.ini" file below, but we set 644
		# for the sake of consistency.
		find /opt/couchdb/etc -type d ! -perm 0755 -exec chmod -f 0755 '{}' +
		find /opt/couchdb/etc -type f ! -perm 0644 -exec chmod -f 0644 '{}' +
	fi

	if [ ! -z "$NODENAME" ] && ! grep "couchdb@" /opt/couchdb/etc/vm.args; then
		echo "-name couchdb@$NODENAME" >> /opt/couchdb/etc/vm.args
	fi

	if [ "$COUCHDB_USER" ] && [ "$COUCHDB_PASSWORD" ]; then
		# Create admin only if not already present
		if ! grep -Pzoqr "\[admins\]\n$COUCHDB_USER =" /opt/couchdb/etc/local.d/*.ini /opt/couchdb/etc/local.ini; then
			printf "\n[admins]\n%s = %s\n" "$COUCHDB_USER" "$COUCHDB_PASSWORD" >> /opt/couchdb/etc/local.d/docker.ini
		fi
	fi

	if [ "$COUCHDB_SECRET" ]; then
		# Set secret only if not already present
		if ! grep -Pzoqr "\[chttpd_auth\]\nsecret =" /opt/couchdb/etc/local.d/*.ini /opt/couchdb/etc/local.ini; then
			printf "\n[chttpd_auth]\nsecret = %s\n" "$COUCHDB_SECRET" >> /opt/couchdb/etc/local.d/docker.ini
		fi
	fi

	if [ "$COUCHDB_ERLANG_COOKIE" ]; then
		cookieFile='/opt/couchdb/.erlang.cookie'
		if [ -e "$cookieFile" ]; then
			if [ "$(cat "$cookieFile" 2>/dev/null)" != "$COUCHDB_ERLANG_COOKIE" ]; then
				echo