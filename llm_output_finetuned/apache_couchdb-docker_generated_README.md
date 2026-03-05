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
File: 3.5.0-ubi/Dockerfile
Size: 3959 bytes
Lines: 97
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

FROM registry.access.redhat.com/ubi8/ubi-minimal

ARG RELEASE
ARG BUILD_DATE

LABEL maintainer="CouchDB Developers dev@couchdb.apache.org" \
      name="Apache CouchDB" \
      version="3.5.0" \
      summary="Apache CouchDB based on Red Hat UBI" \
      description="Red Hat OpenShift-compatible container that runs Apache CouchDB" \
      release=${RELEASE}  \
      usage="https://github.com/apache/couchdb-docker" \
      build-date=${BUILD_DATE} \
      io.k8s.display-name="Apache CouchDB" \
      io.k8s.description="Red Hat OpenShift-compatible container that runs Apache CouchDB" \
      io.openshift.tags="database couchdb apache rhel8" \
      io.openshift.expose-services="5984/http,4369/epmd,9100/erlang" \
      io.openshift.min-memory="1Gi" \
      io.openshift.min-cpu="1"

COPY imeyer_runit.repo /etc/yum.repos.d/imeyer_runit.repo
COPY couchdb.repo /etc/yum.repos.d/couchdb.repo

ENV COUCHDB_VERSION 3.5.0

# Add CouchDB user account to make sure the IDs are assigned consistently
# CouchDB user added to root group for OpenShift support
RUN set -ex; \
# be sure GPG and apt-transport-https are available and functional
    microdnf update --disableplugin=subscription-manager -y && rm -rf /var/cache/yum; \
    microdnf install -y \
            ca-certificates \
            gnupg \
            findutils \
            shadow-utils; \
# Add CouchDB User and Group (group required by rpm)
    useradd -u 5984 -d /opt/couchdb -g root couchdb; \
    groupadd -g 5984 couchdb; \
# Install runit
    microdnf update --disableplugin=subscription-manager -y && rm -rf /var/cache/yum; \
    microdnf install --enablerepo=imeyer_runit -y runit; \
# Clean up
    microdnf clean all; \
    rm -rf /var/cache/yum

# Install CouchDB
RUN set -xe; \
    microdnf update --disableplugin=subscription-manager -y && rm -rf /var/cache/yum; \
    microdnf install --enablerepo=couchdb -y couchdb-${COUCHDB_VERSION}; \
    microdnf clean all; \
    rm -rf /var/cache/yum; \
# remove defaults that force writing logs to file
    rm /opt/couchdb/etc/default.d/10-filelog.ini; \
# Check we own everything in /opt/couchdb. Matches the command in dockerfile_entrypoint.sh
    find /opt/couchdb \! \( -user couchdb -group 0 \) -exec chown -f couchdb:0 '{}' +; \
# Setup directories and permissions for config. Technically these could be 555 and 444 respectively
# but we keep them as 775 and 664 for consistency with the dockerfile_entrypoint.
    find /opt/couchdb/etc -type d ! -perm 0775 -exec chmod -f 0775 '{}' +; \
    find /opt/couchdb/etc -type f ! -perm 0664 -exec chmod -f 0664 '{}' +; \
# Setup directories and permissions for data.
    chmod 777 /opt/couchdb/data

# Add the License
COPY licenses /licenses

# Add configuration
COPY --chown=couchdb:0 resources/10-docker-default.ini /opt/couchdb/etc/default.d/
COPY --chown=couchdb:0 resources/vm.args /opt/couchdb/etc/
COPY resources/docker-entrypoint.sh /usr/local/bin
COPY resources/run /etc/service/couchdb/

# set permissions on runit scripts
RUN chmod -R 777 /etc/service/couchdb; \
    chmod 777 /usr/local/bin/docker-entrypoint.sh; \
# symlink to root folder
    ln -s usr/local/bin/docker-entrypoint.sh /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
VOLUME /opt/couchdb/data

# 5984: Main CouchDB endpoint
# 4369: Erlang portmap daemon (epmd)
# 9100: CouchDB cluster communication port
EXPOSE 5984 4369 9100
CMD ["/opt/couchdb/bin/couchdb"]


---
File: 3.5.0-ubi/couchdb.repo
Size: 241 bytes
Lines: 7
---
[couchdb]
name=couchdb
baseurl=https://apache.jfrog.io/artifactory/couchdb-rpm/el$releasever/$basearch/
gpgkey=https://couchdb.apache.org/repo/keys.asc https://couchdb.apache.org/repo/rpm-package-key.asc
gpgcheck=1
repo_gpgcheck=1
enabled=1


---
File: 3.5.0-ubi/imeyer_runit.repo
Size: 253 bytes
Lines: 10
---
[imeyer_runit]
name=imeyer_runit
baseurl=https://packagecloud.io/imeyer/runit/el/7/x86_64
repo_gpgcheck=1
gpgcheck=0
enabled=1
gpgkey=https://packagecloud.io/imeyer/runit/gpgkey
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300


---
File: 3.5.0-ubi/licenses/LICENSE
Size: 11189 bytes
Lines: 202
---

                                Apache License
                          Version 2.0, January 2004
                       http://www.apache.org/licenses/

  TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

  1. Definitions.

     "License" shall mean the terms and conditions for use, reproduction,
     and distribution as defined by Sections 1 through 9 of this document.

     "Licensor" shall mean the copyright owner or entity authorized by
     the copyright owner that is granting the License.

     "Legal Entity" shall mean the union of the acting entity and all
     other entities that control, are controlled by, or are under common
     control with that entity. For the purposes of this definition,
     "control" means (i) the power, direct or indirect, to cause the
     direction or management of such entity, whether by contract or
     otherwise, or (ii) ownership of fifty percent (50%) or more of the
     outstanding shares, or (iii) beneficial ownership of such entity.

     "You" (or "Your") shall mean an individual or Legal Entity
     exercising permissions granted by this License.

     "Source" form shall mean the preferred form for making modifications,
     including but not limited to software source code, documentation
     source, and configuration files.

     "Object" form shall mean any form resulting from mechanical
     transformation or translation of a Source form, including but
     not limited to compiled object code, generated documentation,
     and conversions to other media types.

     "Work" shall mean the work of authorship, whether in Source or
     Object form, made available under the License, as indicated by a
     copyright notice that is included in or attached to the work
     (an example is provided in the Appendix below).

     "Derivative Works" shall mean any work, whether in Source or Object
     form, that is based on (or derived from) the Work and for which the
     editorial revisions, annotations, elaborations, or other modifications
     represent, as a whole, an original work of authorship. For the purposes
     of this License, Derivative Works shall not include works that remain
     separable from, or merely link (or bind by name) to the interfaces of,
     the Work and Derivative Works thereof.

     "Contribution" shall mean any work of authorship, including
     the original version of the Work and any modifications or additions
     to that Work or Derivative Works thereof, that is intentionally
     submitted to Licensor for inclusion in the Work by the copyright owner
     or by an individual or Legal Entity authorized to submit on behalf of
     the copyright owner. For the purposes of this definition, "submitted"
     means any form of electronic, verbal, or written communication sent
     to the Licensor or its representatives, including but not limited to
     communication on electronic mailing lists, source code control systems,
     and issue tracking systems that are managed by, or on behalf of, the
     Licensor for the purpose of discussing and improving the Work, but
     excluding communication that is conspicuously marked or otherwise
     designated in writing by the copyright owner as "Not a Contribution."

     "Contributor" shall mean Licensor and any individual or Legal Entity
     on behalf of whom a Contribution has been received by Licensor and
     subsequently incorporated within the Work.

  2. Grant of Copyright License. Subject to the terms and conditions of
     this License, each Contributor hereby grants to You a perpetual,
     worldwide, non-exclusive, no-charge, royalty-free, irrevocable
     copyright license to reproduce, prepare Derivative Works of,
     publicly display, publicly perform, sublicense, and distribute the
     Work and such Derivative Works in Source or Object form.

  3. Grant of Patent License. Subject to the terms and conditions of
     this License, each Contributor hereby grants to You a perpetual,
     worldwide, non-exclusive, no-charge, royalty-free, irrevocable
     (except as stated in this section) patent license to make, have made,
     use, offer to sell, sell, import, and otherwise transfer the Work,
     where such license applies only to those patent claims licensable
     by such Contributor that are necessarily infringed by their
     Contribution(s) alone or by combination of their Contribution(s)
     with the Work to which such Contribution(s) was submitted. If You
     institute patent litigation against any entity (including a
     cross-claim or counterclaim in a lawsuit) alleging that the Work
     or a Contribution incorporated within the Work constitutes direct
     or contributory patent infringement, then any patent licenses
     granted to You under this License for that Work shall terminate
     as of the date such litigation is filed.

  4. Redistribution. You may reproduce and distribute copies of the
     Work or Derivative Works thereof in any medium, with or without
     modifications, and in Source or Object form, provided that You
     meet the following conditions:

     (a) You must give any other recipients of the Work or
         Derivative Works a copy of this License; and

     (b) You must cause any modified files to carry prominent notices
         stating that You changed the files; and

     (c) You must retain, in the Source form of any Derivative Works
         that You distribute, all copyright, patent, trademark, and
         attribution notices from the Source form of the Work,
         excluding those notices that do not pertain to any part of
         the Derivative Works; and

     (d) If the Work includes a "NOTICE" text file as part of its
         distribution, then any Derivative Works that You distribute must
         include a readable copy of the attribution notices contained
         within such NOTICE file, excluding those notices that do not
         pertain to any part of the Derivative Works, in at least one
         of the following places: within a NOTICE text file distributed
         as part of the Derivative Works; within the Source form or
         documentation, if provided along with the Derivative Works; or,
         within a display generated by the Derivative Works, if and
         wherever such third-party notices normally appear. The contents
         of the NOTICE file are for informational purposes only and
         do not modify the License. You may add Your own attribution
         notices within Derivative Works that You distribute, alongside
         or as an addendum to the NOTICE text from the Work, provided
         that such additional attribution notices cannot be construed
         as modifying the License.

     You may add Your own copyright statement to Your modifications and
     may provide additional or different license terms and conditions
     for use, reproduction, or distribution of Your modifications, or
     for any such Derivative Works as a whole, provided Your use,
     reproduction, and distribution of the Work otherwise complies with
     the conditions stated in this License.

  5. Submission of Contributions. Unless You explicitly state otherwise,
     any Contribution intentionally submitted for inclusion in the Work
     by You to the Licensor shall be under the terms and conditions of
     this License, without any additional terms or conditions.
     Notwithstanding the above, nothing herein shall supersede or modify
     the terms of any separate license agreement you may have executed
     with Licensor regarding such Contributions.

  6. Trademarks. This License does not grant permission to use the trade
     names, trademarks, service marks, or product names of the Licensor,
     except as required for reasonable and customary use in describing the
     origin of the Work and reproducing the content of the NOTICE file.

  7. Disclaimer of Warranty. Unless required by applicable law or
     agreed to in writing, Licensor provides the Work (and each
     Contributor provides its Contributions) on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
     implied, including, without limitation, any warranties or conditions
     of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
     PARTICULAR PURPOSE. You are solely responsible for determining the
     appropriateness of using or redistributing the Work and assume any
     risks associated with Your exercise of permissions under this License.

  8. Limitation of Liability. In no event and under no legal theory,
     whether in tort (including negligence), contract, or otherwise,
     unless required by applicable law (such as deliberate and grossly
     negligent acts) or agreed to in writing, shall any Contributor be
     liable to You for damages, including any direct, indirect, special,
     incidental, or consequential damages of any character arising as a
     result of this License or out of the use or inability to use the
     Work (including but not limited to damages for loss of goodwill,
     work stoppage, computer failure or malfunction, or any and all
     other commercial damages or losses), even if such Contributor
     has been advised of the possibility of such damages.

  9. Accepting Warranty or Additional Liability. While redistributing
     the Work or Derivative Works thereof, You may choose to offer,
     and charge a fee for, acceptance of support, warranty, indemnity,
     or other liability obligations and/or rights consistent with this
     License. However, in accepting such obligations, You may act only
     on Your own behalf and on Your sole responsibility, not on behalf
     of any other Contributor, and only if You agree to indemnify,
     defend, and hold each Contributor harmless for any liability
     incurred by, or claims asserted against, such Contributor by reason
     of your accepting any such warranty or additional liability.

  END OF TERMS AND CONDITIONS

  APPENDIX: How to apply the Apache License to your work.

     To apply the Apache License to your work, attach the following
     boilerplate notice, with the fields enclosed by brackets "[]"
     replaced with your own identifying information. (Don't include
     the brackets!)  The text should be enclosed in the appropriate
     comment syntax for the file format. We also recommend that a
     file or class name and description of purpose be included on the
     same "printed page" as the copyright notice for easier
     identification within third-party archives.

  Copyright [yyyy] [name of copyright owner]

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.


---
File: 3.5.0-ubi/resources/vm.args
Size: 968 bytes
Lines: