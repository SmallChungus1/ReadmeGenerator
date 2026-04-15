---
File: templates\docker-compose\data\broker\conf\broker1.conf
Size: 169 bytes
Lines: 7
---
brokerClusterName = DefaultCluster
brokerName = broker-b
brokerId = 1
deleteWhen = 04
fileReservedTime = 48
brokerRole = SLAVE
flushDiskType = ASYNC_FLUSH


---
File: templates\docker-compose\docker-compose.yml
Size: 1379 bytes
Lines: 47
---
version: '2'
services:
  #Service for nameserver
  namesrv:
    image: apache/rocketmq:ROCKETMQ_VERSION
    container_name: rmqnamesrv
    ports:
      - 9876:9876
    volumes:
      - ./data/namesrv/logs:/home/rocketmq/logs
    command: sh mqnamesrv

  #Service for broker
  broker:
    image: apache/rocketmq:ROCKETMQ_VERSION
    container_name: rmqbroker
    links:
      - namesrv
    ports:
      - 10909:10909
      - 10911:10911
      - 10912:10912
    environment:
      - NAMESRV_ADDR=namesrv:9876
    volumes:
      - ./data/broker/logs:/home/rocketmq/logs
      - ./data/broker/store:/home/rocketmq/store
      - ./data/broker/conf/broker.conf:/opt/rocketmq-ROCKETMQ_VERSION/conf/broker.conf
    command: sh mqbroker -c /opt/rocketmq-ROCKETMQ_VERSION/conf/broker.conf

  #Service for another broker -- broker1
  broker1:
    image: apache/rocketmq:ROCKETMQ_VERSION
    container_name: rmqbroker-b
    links:
      - namesrv
    ports:
      - 10929:10909
      - 10931:10911
      - 10932:10912
    environment:
      - NAMESRV_ADDR=namesrv:9876
    volumes:
      - ./data1/broker/logs:/home/rocketmq/logs
      - ./data1/broker/store:/home/rocketmq/store
      - ./data1/broker/conf/broker.conf:/opt/rocketmq-ROCKETMQ_VERSION/conf/broker.conf
    command: sh mqbroker -c /opt/rocketmq-ROCKETMQ_VERSION/conf/broker.conf


---
File: templates\docker-compose\rmq5-docker-compose.yml
Size: 1950 bytes
Lines: 69
---
version: '2'
services:
  #Service for nameserver
  namesrv:
    image: apache/rocketmq:ROCKETMQ_VERSION
    container_name: rmqnamesrv
    ports:
      - 9876:9876
    volumes:
      - ./data/namesrv/logs:/home/rocketmq/logs
    command: sh mqnamesrv

  #Service for broker
  broker:
    image: apache/rocketmq:ROCKETMQ_VERSION
    container_name: rmqbroker
    links:
      - namesrv
    ports:
      - 10909:10909
      - 10911:10911
      - 10912:10912
    environment:
      - NAMESRV_ADDR=namesrv:9876
    volumes:
      - ./data/broker/logs:/home/rocketmq/logs
      - ./data/broker/store:/home/rocketmq/store
      - ./data/broker/conf/broker.conf:/opt/rocketmq-ROCKETMQ_VERSION/conf/broker.conf
    command: sh mqbroker -c /opt/rocketmq-ROCKETMQ_VERSION/conf/broker.conf

  #Service for another broker -- broker1
  broker1:
    image: apache/rocketmq:ROCKETMQ_VERSION
    container_name: rmqbroker-b
    links:
      - namesrv
    ports:
      - 10929:10909
      - 10931:10911
      - 10932:10912
    environment:
      - NAMESRV_ADDR=namesrv:9876
    volumes:
      - ./data1/broker/logs:/home/rocketmq/logs
      - ./data1/broker/store:/home/rocketmq/store
      - ./data1/broker/conf/broker.conf:/opt/rocketmq-ROCKETMQ_VERSION/conf/broker.conf
    command: sh mqbroker -c /opt/rocketmq-ROCKETMQ_VERSION/conf/broker.conf

  #Service for proxy
  proxy:
    image: apache/rocketmq:ROCKETMQ_VERSION
    container_name: rmqproxy
    links:
      - namesrv
      - broker
      - broker1
    depends_on:
      - broker
      - broker1
    ports:
      - 8080:8080
      - 8081:8081
    restart: on-failure
    environment:
      - NAMESRV_ADDR=namesrv:9876
    volumes:
      - ./proxy/logs:/home/rocketmq/logs
      - ./proxy/conf/rmq-proxy.json:/opt/rocketmq-ROCKETMQ_VERSION/conf/rmq-proxy.json
    command: sh mqproxy -pc /opt/rocketmq-ROCKETMQ_VERSION/conf/rmq-proxy.json


---
File: templates\kubernetes\deployment.yaml
Size: 1281 bytes
Lines: 46
---
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: rocketmq
spec:
  replicas: 1
  template:
    metadata:
     labels:
       app: rocketmq
    spec:
      containers:
      - name: broker
        image: apache/rocketmq:ROCKETMQ_VERSION
        command: ["sh","mqbroker", "-n","localhost:9876"]
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 10909
          - containerPort: 10911
        volumeMounts:
          - mountPath: /home/rocketmq/logs
            name: brokeroptlogs
          - mountPath: /home/rocketmq/store
            name: brokeroptstore
      - name: namesrv
        image: apache/rocketmq:ROCKETMQ_VERSION
        command: ["sh","mqnamesrv"]
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 9876
        volumeMounts:
          - mountPath: /home/rocketmq/logs
            name: namesrvoptlogs
      volumes:
      - name: brokeroptlogs
        hostPath:
          path: /data/broker/logs
      - name: brokeroptstore
        hostPath:
          path: /data/broker/store
      - name: namesrvoptlogs
        hostPath:
          path: /data/namesrv/logs
      - name: namesrvoptstore
        hostPath:
          path: /data/namesrv/store


---
File: templates\kubernetes\deployment2.yaml
Size: 1687 bytes
Lines: 68
---
kind: Deployment
apiVersion: extensions/v1beta1
metadata:
  name: rocketmq-ns-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: rocketmq-nameserver
      name: rocketmq-nameserver
  template:
    metadata:
     labels:
      app: rocketmq-nameserver
      name: rocketmq-nameserver
    spec:
      containers:
      - name: rocketmq-nameserver
        image: apache/rocketmq:ROCKETMQ_VERSION
        command: ["sh","mqnamesrv"]
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 9876
        volumeMounts:
          - mountPath: /home/rocketmq/logs
            name: namesrvlogs
      volumes:
      - name: namesrvlogs
        emptyDir: {}
      - name: namesrvstore 
        emptyDir: {}
---          
kind: Deployment
apiVersion: extensions/v1beta1
metadata:
  name: rocketmq-broker-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: rocketmq-broker
      name: rocketmq-broker
  template:
    metadata:
     labels:
      app: rocketmq-broker
      name: rocketmq-broker
    spec:
      containers:
      - name: rocketmq-broker
        image: apache/rocketmq:ROCKETMQ_VERSION
        command: ["sh","mqbroker", "-n","rocketmq-ns-deployment:9876"]
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 10909
          - containerPort: 10911
        volumeMounts:
          - mountPath: /home/rocketmq/logs
            name: brokerlogs
          - mountPath: /home/rocketmq/store
            name: brokerstore
      volumes:
      - name: brokerlogs
        emptyDir: {}
      - name: brokerstore
        emptyDir: {}




---
File: templates\docker-compose\docker-compose.yml
Size: 1379 bytes
Lines: 47
---
version: '2'
services:
  #Service for nameserver
  namesrv:
    image: apache/rocketmq:ROCKETMQ_VERSION
    container_name: rmqnamesrv
    ports:
      - 9876:9876
    volumes:
      - ./data/namesrv/logs:/home/rocketmq/logs
    command: sh mqnamesrv

  #Service for broker
  broker:
    image: apache/rocketmq:ROCKETMQ_VERSION
    container_name: rmqbroker
    links:
      - namesrv
    ports:
      - 10909:10909
      - 10911:10911
      - 10912:10912
    environment:
      - NAMESRV_ADDR=namesrv:9876
    volumes:
      - ./data/broker/logs:/home/rocketmq/logs
      - ./data/broker/store:/home/rocketmq/store
      - ./data/broker/conf/broker.conf:/opt/rocketmq-ROCKETMQ_VERSION/conf/broker.conf
    command: sh mqbroker -c /opt/rocketmq-ROCKETMQ_VERSION/conf/broker.conf

  #Service for another broker -- broker1
  broker1:
    image: apache/rocketmq:ROCKETMQ_VERSION
    container_name: rmqbroker-b
    links:
      - namesrv
    ports:
      - 10929:10909
      - 10931:10911
      - 10932:10912
    environment:
      - NAMESRV_ADDR=namesrv:9876
    volumes:
      - ./data1/broker/logs:/home/rocketmq/logs
      - ./data1/broker/store:/home/rocketmq/store
      - ./data1/broker/conf/broker.conf:/opt/rocketmq-ROCKETMQ_VERSION/conf/broker.conf
    command: sh mqbroker -c /opt/rocketmq-ROCKETMQ_VERSION/conf/broker.conf


---
File: templates\docker-compose\rmq5-docker-compose.yml
Size: 1950 bytes
Lines: 69
---
version: '2'
services:
  #Service for nameserver
  namesrv:
    image: apache/rocketmq:ROCKETMQ_VERSION
    container_name: rmqnamesrv
    ports:
      - 9876:9876
    volumes:
      - ./data/namesrv/logs:/home/rocketmq/logs
    command: sh mqnamesrv

  #Service for broker
  broker:
    image: apache/rocketmq:ROCKETMQ_VERSION
    container_name: rmqbroker
    links:
      - namesrv
    ports:
      - 10909:10909
      - 10911:10911
      - 10912:10912
    environment:
      - NAMESRV_ADDR=namesrv:9876
    volumes:
      - ./data/broker/logs:/home/rocketmq/logs
      - ./data/broker/store:/home/rocketmq/store
      - ./data/broker/conf/broker.conf:/opt/rocketmq-ROCKETMQ_VERSION/conf/broker.conf
    command: sh mqbroker -c /opt/rocketmq-ROCKETMQ_VERSION/conf/broker.conf

  #Service for another broker -- broker1
  broker1:
    image: apache/rocketmq:ROCKETMQ_VERSION
    container_name: rmqbroker-b
    links:
      - namesrv
    ports:
      - 10929:10909
      - 10931:10911
      - 10932:10912
    environment:
      - NAMESRV_ADDR=namesrv:9876
    volumes:
      - ./data1/broker/logs:/home/rocketmq/logs
      - ./data1/broker/store:/home/rocketmq/store
      - ./data1/broker/conf/broker.conf:/opt/rocketmq-ROCKETMQ_VERSION/conf/broker.conf
    command: sh mqbroker -c /opt/rocketmq-ROCKETMQ_VERSION/conf/broker.conf

  #Service for proxy
  proxy:
    image: apache/rocketmq:ROCKETMQ_VERSION
    container_name: rmqproxy
    links:
      - namesrv
      - broker
      - broker1
    depends_on:
      - broker
      - broker1
    ports:
      - 8080:8080
      - 8081:8081
    restart: on-failure
    environment:
      - NAMESRV_ADDR=namesrv:9876
    volumes:
      - ./proxy/logs:/home/rocketmq/logs
      - ./proxy/conf/rmq-proxy.json:/opt/rocketmq-ROCKETMQ_VERSION/conf/rmq-proxy.json
    command: sh mqproxy -pc /opt/rocketmq-ROCKETMQ_VERSION/conf/rmq-proxy.json


---
File: templates\kubernetes\deployment.yaml
Size: 1281 bytes
Lines: 46
---
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: rocketmq
spec:
  replicas: 1
  template:
    metadata:
     labels:
       app: rocketmq
    spec:
      containers:
      - name: broker
        image: apache/rocketmq:ROCKETMQ_VERSION
        command: ["sh","mqbroker", "-n","localhost:9876"]
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 10909
          - containerPort: 10911
        volumeMounts:
          - mountPath: /home/rocketmq/logs
            name: brokeroptlogs
          - mountPath: /home/rocketmq/store
            name: brokeroptstore
      - name: namesrv
        image: apache/rocketmq:ROCKETMQ_VERSION
        command: ["sh","mqnamesrv"]
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 9876
        volumeMounts:
          - mountPath: /home/rocketmq/logs
            name: namesrvoptlogs
      volumes:
      - name: brokeroptlogs
        hostPath:
          path: /data/broker/logs
      - name: brokeroptstore
        hostPath:
          path: /data/broker/store
      - name: namesrvoptlogs
        hostPath:
          path: /data/namesrv/logs
      - name: namesrvoptstore
        hostPath:
          path: /data/namesrv/store


---
File: templates\kubernetes\deployment2.yaml
Size: 1687 bytes
Lines: 68
---
kind: Deployment
apiVersion: extensions/v1beta1
metadata:
  name: rocketmq-ns-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: rocketmq-nameserver
      name: rocketmq-nameserver
  template:
    metadata:
     labels:
      app: rocketmq-nameserver
      name: rocketmq-nameserver
    spec:
      containers:
      - name: rocketmq-nameserver
        image: apache/rocketmq:ROCKETMQ_VERSION
        command: ["sh","mqnamesrv"]
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 9876
        volumeMounts:
          - mountPath: /home/rocketmq/logs
            name: namesrvlogs
      volumes:
      - name: namesrvlogs
        emptyDir: {}
      - name: namesrvstore 
        emptyDir: {}
---          
kind: Deployment
apiVersion: extensions/v1beta1
metadata:
  name: rocketmq-broker-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: rocketmq-broker
      name: rocketmq-broker
  template:
    metadata:
     labels:
      app: rocketmq-broker
      name: rocketmq-broker
    spec:
      containers:
      - name: rocketmq-broker
        image: apache/rocketmq:ROCKETMQ_VERSION
        command: ["sh","mqbroker", "-n","rocketmq-ns-deployment:9876"]
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 10909
          - containerPort: 10911
        volumeMounts:
          - mountPath: /home/rocketmq/logs
            name: brokerlogs
          - mountPath: /home/rocketmq/store
            name: brokerstore
      volumes:
      - name: brokerlogs
        emptyDir: {}
      - name: brokerstore
        emptyDir: {}



---
File: templates\kubernetes\deployment.yaml
Size: 1281 bytes
Lines: 46
---
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: rocketmq
spec:
  replicas: 1
  template:
    metadata:
     labels:
       app: rocketmq
    spec:
      containers:
      - name: broker
        image: apache/rocketmq:ROCKETMQ_VERSION
        command: ["sh","mqbroker", "-n","localhost:9876"]
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 10909
          - containerPort: 10911
        volumeMounts:
          - mountPath: /home/rocketmq/logs
            name: brokeroptlogs
          - mountPath: /home/rocketmq/store
            name: brokeroptstore
      - name: namesrv
        image: apache/rocketmq:ROCKETMQ_VERSION
        command: ["sh","mqnamesrv"]
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 9876
        volumeMounts:
          - mountPath: /home/rocketmq/logs
            name: namesrvoptlogs
      volumes:
      - name: brokeroptlogs
        hostPath:
          path: /data/broker/logs
      - name: brokeroptstore
        hostPath:
          path: /data/broker/store
      - name: namesrvoptlogs
        hostPath:
          path: /data/namesrv/logs
      - name: namesrvoptstore
        hostPath:
          path: /data/namesrv/store


---
File: templates\kubernetes\deployment2.yaml
Size: 1687 bytes
Lines: 68
---
kind: Deployment
apiVersion: extensions/v1beta1
metadata:
  name: rocketmq-ns-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: rocketmq-nameserver
      name: rocketmq-nameserver
  template:
    metadata:
     labels:
      app: rocketmq-nameserver
      name: rocketmq-nameserver
    spec:
      containers:
      - name: rocketmq-nameserver
        image: apache/rocketmq:ROCKETMQ_VERSION
        command: ["sh","mqnamesrv"]
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 9876
        volumeMounts:
          - mountPath: /home/rocketmq/logs
            name: namesrvlogs
      volumes:
      - name: namesrvlogs
        emptyDir: {}
      - name: namesrvstore 
        emptyDir: {}
---          
kind: Deployment
apiVersion: extensions/v1beta1
metadata:
  name: rocketmq-broker-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: rocketmq-broker
      name: rocketmq-broker
  template:
    metadata:
     labels:
      app: rocketmq-broker
      name: rocketmq-broker
    spec:
      containers:
      - name: rocketmq-broker
        image: apache/rocketmq:ROCKETMQ_VERSION
        command: ["sh","mqbroker", "-n","rocketmq-ns-deployment:9876"]
        imagePullPolicy: IfNotPresent
        ports:
          - containerPort: 10909
          - containerPort: 10911
        volumeMounts:
          - mountPath: /home/rocketmq/logs
            name: brokerlogs
          - mountPath: /home/rocketmq/store
            name: brokerstore
      volumes:
      - name: brokerlogs
        emptyDir: {}
      - name: brokerstore
        emptyDir: {}



---
File: templates\kubernetes\deployment.yaml
Size: 1281 bytes
Lines: 46
---
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: rocketmq
spec:
  replicas: 1
  template:
    metadata:
     labels:
       app: rocketmq
    spec:
      containers:
      - name: broker
        image: apache/rocketmq:ROCKETMQ_VERSION
        command: ["sh","mqbroker", "-n","localhost:9876"]
        imagePullPolicy: IfNotPresent