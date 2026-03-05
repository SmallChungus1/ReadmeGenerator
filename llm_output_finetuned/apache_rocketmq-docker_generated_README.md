---
File: image-build/scripts/runserver-customize.sh
Size: 2737 bytes
Lines: 67
---
#!/bin/bash

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#===========
# Java Environment Setting
#===========
error_exit ()
{
    echo "ERROR: $1 !!"
    exit 1
}

find_java_home()
{
    case "`uname`" in
        Darwin)
            JAVA_HOME=$(/usr/libexec/java_home)
        ;;
        *)
            JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))
        ;;
    esac
}

find_java_home

[ ! -e "$JAVA_HOME/bin/java" ] && JAVA_HOME=$HOME/jdk/java
[ ! -e "$JAVA_HOME/bin/java" ] && JAVA_HOME=/usr/java
[ ! -e "$JAVA_HOME/bin/java" ] && error_exit "Please set the JAVA_HOME variable in your environment, We need java(x64)!"

export JAVA_HOME
export JAVA="$JAVA_HOME/bin/java"
export BASE_DIR=$(dirname $0)/..
export CLASSPATH=.:${BASE_DIR}/conf:${CLASSPATH}

#===========
# JVM Configuration
#===========
DEFAULT_HEAP_OPTS="-Xms1g -Xmx1g -Xmn512M"
HEAP_OPTS=${HEAP_OPTS:-$DEFAULT_HEAP_OPTS}

# Set for `JAVA_OPT`.
JAVA_OPT="${JAVA_OPT} -server ${HEAP_OPTS}"
JAVA_OPT="${JAVA_OPT} -XX:+UseConcMarkSweepGC -XX:+UseCMSCompactAtFullCollection -XX:CMSInitiatingOccupancyFraction=70 -XX:+CMSParallelRemarkEnabled -XX:SoftRefLRUPolicyMSPerMB=0 -XX:+CMSClassUnloadingEnabled -XX:SurvivorRatio=8  -XX:-UseParNewGC"
JAVA_OPT="${JAVA_OPT} -verbose:gc -Xloggc:/dev/shm/rmq_srv_gc.log -XX:+PrintGCDetails"
JAVA_OPT="${JAVA_OPT} -XX:-OmitStackTraceInFastThrow"
JAVA_OPT="${JAVA_OPT}  -XX:-UseLargePages"
JAVA_OPT="${JAVA_OPT} -Djava.ext.dirs=${JAVA_HOME}/jre/lib/ext:${BASE_DIR}/lib"
#JAVA_OPT="${JAVA_OPT} -Xdebug -Xrunjdwp:transport=dt_socket,address=9555,server=y,suspend=n"
JAVA_OPT="${JAVA_OPT} ${JAVA_OPT_EXT}"
JAVA_OPT="${JAVA_OPT} -cp ${CLASSPATH}"

$JAVA ${JAVA_OPT} $@


---
File: templates/play-docker-tls.sh
Size: 2277 bytes
Lines: 53
---
#!/bin/bash

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

RMQ_CONTAINER=$(docker ps -a|awk '/rmq/ {print $1}')
if [[ -n "$RMQ_CONTAINER" ]]; then
   echo "Removing RocketMQ Container..."
   docker rm -fv $RMQ_CONTAINER
   # Wait till the existing containers are removed
   sleep 5
fi

prepare_dir()
{
    dirs=("data/namesrv/logs" "data/broker/logs" "data/broker/store")

    for dir in ${dirs[@]}
    do
        if [ ! -d "`pwd`/${dir}" ]; then
            mkdir -p "`pwd`/${dir}"
            chmod a+rw "`pwd`/${dir}"
        fi
    done
}

prepare_dir

echo "Starting RocketMQ nodes..."

# Start nameserver
docker run -d -v `pwd`/ssl:/home/rocketmq/ssl  -v `pwd`/data/namesrv/logs:/home/rocketmq/logs --name rmqnamesrv -e "JAVA_OPT=-Dtls.test.mode.enable=false -Dtls.config.file=/home/rocketmq/ssl/ssl.properties -Dtls.test.mode.enable=false -Dtls.server.need.client.auth=required"  apache/rocketmq:ROCKETMQ_VERSION sh mqnamesrv

# Start Broker
docker run -d -v `pwd`/ssl:/home/rocketmq/ssl  -v `pwd`/data/broker/logs:/home/rocketmq/logs -v `pwd`/data/broker/store:/home/rocketmq/store --name rmqbroker --link rmqnamesrv:namesrv -e "NAMESRV_ADDR=namesrv:9876" -e "JAVA_OPT=-Dtls.enable=true -Dtls.client.authServer=true -Dtls.test.mode.enable=false -Dtls.config.file=/home/rocketmq/ssl/ssl.properties -Dtls.test.mode.enable=false -Dtls.server.mode=enforcing  -Dtls.server.need.client.auth=required" apache/rocketmq:ROCKETMQ_VERSION sh mqbroker

# Service unavailable when not ready
# sleep 20

# Produce messages
# sh ./play-producer.sh


---
File: templates/ssl/ssl.properties
Size: 489 bytes
Lines: 13
---
## client setting
tls.client.certPath=/home/rocketmq/ssl/client.crt
tls.client.keyPath=/home/rocketmq/ssl/client_rsa_private_pkcs8.pem
tls.client.keyPassword=client
tls.client.trustCertPath=/home/rocketmq/ssl/ca.crt

## server setting
tls.server.certPath=/home/rocketmq/ssl/server.crt
tls.server.keyPath=/home/rocketmq/ssl/server_rsa_private_pkcs8.pem
tls.server.keyPassword=server
tls.server.trustCertPath=/home/rocketmq/ssl/ca.crt
#server.auth.client
tls.server.need.client.auth=required

---
File: templates/ssl/ca.crt
Size: 1241 bytes
Lines: 21
---
-----BEGIN CERTIFICATE-----
MIIDZjCCAk4CCQCtAwqWe7vLNzANBgkqhkiG9w0BAQsFADB1MQswCQYDVQQGEwJD
TjELMAkGA1UECAwCQkoxCzAJBgNVBAcMAkJKMQwwCgYDVQQKDANDT00xDDAKBgNV
BAsMA05TUDELMAkGA1UEAwwCQ0ExIzAhBgkqhkiG9w0BCQEWFHlvdXJlbWFpbEBh
cGFjaGUuY29tMB4XDTE5MDYxMzA3MDk1M1oXDTIwMDYxMjA3MDk1M1owdTELMAkG
A1UEBhMCQ04xCzAJBgNVBAgMAkJKMQswCQYDVQQHDAJCSjEMMAoGA1UECgwDQ09N
MQwwCgYDVQQLDANOU1AxCzAJBgNVBAMMAkNBMSMwIQYJKoZIhvcNAQkBFhR5b3Vy
ZW1haWxAYXBhY2hlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
ANdzKEOXr/NRkJir0+vHGYkbAYhRZaFvAJTnjymAOtipAEWENgUTcNSOfdJu+0EZ
Xiw8sItYgj/WOBMdsHLDFDv2Z/tKZodPFOH2UkgmqrHEQLVSXoRcEaOMs9OXrVBy
0tzv2VQdGyihIM0hWHGXEcf7jbh7mhho0fVI0Kc7YfWrx1Q57ad4WzM9zAvsU5J4
tyBGfgZQcScwVbyqc01N5Q0pUKRbVNgIYbr806a6lOHc0NfHrZFyyo0TGCF/U3o5
Wkyb2Nm67IGJXwbFICi3u8IEVcqy/8JLHja8IXW89oksqY6lSkergsHpUESW1y7q
tREeeLbZqJVUUA/T8yLAr7UCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAResTmwE0
JW9mvWfZX9jI5/ERUOklYkiTRNfbVtXMJv2dnqpI6ZqUoAt7Yq+W1jYHqqf+sSYP
jbaxO2aC5nTQIigdbrtNazpUScSiFCydu9wThlY4sGWu39Yy5YJ55MsE/Ra7J8lj
v7EjWe+eG54f9kOfjwAsH2oKIntxSvHvGoNZ7/46JwU3volL+EAVA+Yvs5mwR4F2
NB9FItBK2TCRErmf6JrP/2TZ399kabVRk1ZSjGNoe3UQc5ZxlvtW3shGR0d98ysf
/AkVb6P77tAc4VX9ccoznc1xR/kzZMCu/AWc8TNV5lzVL4EfmKrtrzWAHkkeTLjY
lSck/qDdF0uKNg==
-----END CERTIFICATE-----

---
File: templates/ssl/server.csr
Size: 1029 bytes
Lines: 17
---
-----BEGIN CERTIFICATE REQUEST-----
MIICvjCCAaYCAQAweTELMAkGA1UEBhMCQ04xCzAJBgNVBAgMAkJKMQswCQYDVQQH
DAJCSjEMMAoGA1UECgwDQ09NMQwwCgYDVQQLDANOU1AxDzANBgNVBAMMBlNFUlZF
UjEjMCEGCSqGSIb3DQEJARYUeW91cmVtYWlsQGFwYWNoZS5jb20wggEiMA0GCSqG
SIb3DQEBAQUAA4IBDwAwggEKAoIBAQC9DgTX7RfPfdu7kI0LTDJZsEZjcO7v6jju
I5AsGie9V8jCYusJGI7VbHEFDlAd8Bj+Di+VDSKyVhBwVvE9vCFtccXpnnbq1BuLT
iJuMJ8JoAF6BZnnS7heGeXE073nco8m90kt2GvDJ+GGtM29tDzAGRZiEXlGABQO
vRblqUNK4ZyIOcS+nhPMxu5vJF1kA2xS03ow+Sas0CtJ90yPCNJEczuyeXuyeJTl
MKUsPyjzwQsKQRScipi7X6MOh+4dDm3FRt0N4+H29yGHSjxgmlzR5H4/je7INW6Y
XCPoK5YrcsPfbgl2FvqHMMC2wH7+Yjlf1GCFWWAC84p6x+2DtbgdAgMBAAEwDQYJK
oZIhvcNAQEFBQADggEPADCCAQoCggEBANdzKEOXr/NRkJir0+vHGYkbAYhRZaFv
AJTnjymAOtipAEWENgUTcNSOfdJu+0EZXiw8sItYgj/WOBMdsHLDFDv2Z/tKZod
PFOH2UkgmqrHEQLVSXoRcEaOMs9OXrVBy0tzv2VQdGyihIM0hWHGXEcf7jbh7mh
ho0fVI0Kc7YfWrx1Q57ad4WzM9zAvsU5J4tyBGfgZQcScwVbyqc01N5Q0pUKRbVN
gIYbr806a6lOHc0NfHrZFyyo0TGCF/U3o5Wkyb2Nm67IGJXwbFICi3u8IEVcqy/
8JLHja8IXW89oksqY6lSkergsHpUESW1y7qtREeeLbZqJVUUA/T8yLAr7UCAwEA
ATANBgkqhkiG9w0BAQsFAAOCAQEAResTmwE0JW9mvWfZX9jI5/ERUOklYkiTRNfb
VtXMJv2dnqpI6ZqUoAt7Yq+W1jYHqqf+sSYPjbaxO2aC5nTQIigdbrtNazpUScSi
FCydu9wThlY4sGWu39Yy5YJ55MsE/Ra7J8ljv7EjWe+eG54f9kOfjwAsH2oKIntx
SvHvGoNZ7/46JwU3volL+EAVA+Yvs5mwR4F2NB9FItBK2TCRErmf6JrP/2TZ399k
abVRk1ZSjGNoe3UQc5ZxlvtW3shGR0d98ysf/AkVb6P77tAc4VX9ccoznc1xR/kz
ZMCu/AWc8TNV5lzVL4EfmKrtrzWAHkkeTLjYlSck/qDdF0uKNg==
-----END CERTIFICATE REQUEST-----

---
File: templates/ssl/ca.srl
Size: 17 bytes
Lines: 1
---
E58D4036D019CAA5
---
File: templates/ssl/server_rsa_private_pkcs8.pem
Size: 1773 bytes
Lines: 29
---
-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIE4jAcBgoqhkiG9w0BDAEBMA4ECJOZ3PKU8BRPAgIIAASCBMAocpv2E45lph1C
G5zcJbwMJw08ER7ouxnhcGyKt+CXIbMESikTUUJDudCWgTiTIt/A0baNPW4m6Zv+
oJhvMBFl7KfUyCkVRpSw53ygHM6TeeIS0UP6x7eB9++yNCJ3ZVF7OzVvmDwx9FnV
XOfgQjZIIvcyXgn5jwj82PB7YG3fwQye4AUgmr6ngbMk/GZ35XIZSfPptHHdvkxG
DifswZynDX8FeH4NAKZJilC0m/gO2OayVRHl19LVTu9V/1SKya0uLJvP9Lezqwl9
n1cSexe8rbpho3HX5nRbWk3T2/sM1F/fD/ylDdzgrvLe7xmlbExhBMZfIaFnTJu3
4+dJBYlS7cBBeF2B+9/4r6TXVtZMsjNVmWLEye3ExXCOY41fKvTv5qH4TyXXrsrc
1G4Bv4+oNXa/WnfF8qDlvtsSouOPWHtQEQMVMKyaLL70Z1wyKFVtFT8EbkGmT878
lJX/XsgXgfq61+OZUpriQb1+0nzlPStnRRUL07D+ryllvFRoIBh1q9OwIvdVHDsI
zh+KCVsPEuq7VdIW+wNRiomIGu4SLjquPYxyOnqV3YVmcSUfzbo+li1QcplC6WVS
LICZsvIuCUtEAOTXzJdcUMKSNgYX+sCLZBrG+EYZhTBFwTELSTGESC3gGGdua1nq
Bm86S1wBgY6i9jIDxvuLXOVcphVUB6/9PQrxbVAtrpeDXGAyMj72h1GSGehr/VuS
jlSNz/LLXoSCZKs6faPo3B0PM0VMN87dVNVpOw+3eTkdy2x/0H2oAoGVIbtSTvbh
bmTbCcMiXlwCBgfUZUu+6YuwRZzxXxS8gNpXW/RT8KNnmCLGNtjJhQN4hHfrKsAI
+M1qAVbkSixHRGWQygbFSUUQ8h7OYFMft5YpnKLgl/BaMjzAsFZOFbcOAerQHcL7
FatCQpBCmQ8MleiEzK7rN7IGYe7yx0HW1NzX6ym2uhCUtwipH6sspT7hDJvMrGFW
vAQwBBdw6ewmjq+XCliSDNFTp1TRkiN0ilgeLS+EIBPKh0SFooXe5oXJhbTNVQem
is958jgJLeDGVDZrjyZq2ptPYb0kXmGQKvhnqZkO8hqI1xGbGZm7tERivolclMN2
e4Yh1D68fcyOzpmfPiVN6T22I0GMAtq8exO+F2LTdarGWnBRr6aOp6QSPz7iMQhf
OHXUj4smLGkZT5XIlinoVK5YlKIq5aUusKrS9hxqNfyMTz9iETiNNg9hCTolXKvN
tuYygAMR44DqhLTsQLr/8++DxdLZ4v3Rd16q/YX1GNAUMvNEMzokDbp50+ET36Mg
VZu3SeRmjnh5SvohDRbM4uool+0KFkGjsB3UpyeF1QgfNcUuc608VnFFF3XIErw9
TaARow1v8LJ9+C2p8ZweSr5npatP4uMcDZ3DalRx7Dhef5PpOmt0BTuV9AJpBLDe
l3qpQo/z5a25wJa1fe7xk2nbVGjI7goxJSJu4BovE9pBw0GkQz44xNiKn+S4Bunp
lIJ9CpB1i9+EN7xxcG2vPkcsajgCmoXqlMfxvuvegZPISAwsxjd9WPO8BuC1a6dA
EmVffgNsK43YGSnBJZEmmOb+1uGvbZJHLiMcpTF2xiaCr9qxDurn1euOFJ4nIF1f
ONZTTyJQ
-----END ENCRYPTED PRIVATE KEY-----
---
File: templates/ssl/client_rsa_private_pkcs8.pem
Size: 1777 bytes
Lines: 29
---
-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIE4zAcBgoqhkiG9w0BDAEBMA4ECLmmzAmLIjO3AgIIAASCBMETwEYAUaz988mU
3NyUox7+owFLpeIkqHptQ+KP/iMmP+cXJe+hLMjyvG7HGSauQ5ruNSUqg2OfaHrx
RqzBjESlkqOmJ7u7IGNRGFlds+SHikbgHoJb+sYP1K7qPeHpCMgq+JD3cV0F7UQF
cUZNv/4PLSsw/lo70N8+FaGeGRto0TO8Djhlvs4sPM4rlTazV5h3LpOZCYkO56Gd
DpwYo+bcr1S0GxZMgyRbggAvcL02GTTvSoH5KdzX10UbH/pJh6Q28