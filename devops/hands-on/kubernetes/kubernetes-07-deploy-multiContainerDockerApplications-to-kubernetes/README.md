# Hands-on Kubernetes-07 : Deploy multi-container Docker applications to kubernetes.

Purpose of the this hands-on training is to give students the knowledge of deploying `multi-container Docker applications` to kubernetes.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- Understand deployment and management of microservices.

## Outline

- Part 1 - Setting up the Kubernetes Cluster

- Part 2 - Outline of the multi-container docker applications

- Part 3 - Deployments and Services

- Part 4 - Secrets and ConfigMaps

- Part 5 - Volumes

## Part 1 - Setting up the Kubernetes Cluster

- Launch a Kubernetes Cluster of Ubuntu 20.04 with two nodes (one master, one worker) using the [Cloudformation Template to Create Kubernetes Cluster](./cfn-template-to-create-k8s-cluster.yml). *Note: Once the master node up and running, worker node automatically joins the cluster.*

>*Note: If you have problem with kubernetes cluster, you can use this link for lesson.*
>https://www.katacoda.com/courses/kubernetes/playground

- Check if Kubernetes is running and nodes are ready.

```bash
kubectl cluster-info
kubectl get no
```

## Part 2 - Outline of the multi-container docker applications

- Examine the `to-do-api.py`, `Dockerfile` and `docker-compose.yaml` files in `docker-compose` folder. Notice that there are two microservices: `database` is created from mysql:5.7 image and `myapp` is builded with `Dockerfile.` 

```yaml
version: "3.8"

services:
    database:
        image: mysql:5.7
        environment:
            MYSQL_ROOT_PASSWORD: R1234r
            MYSQL_DATABASE: todo_db
            MYSQL_USER: clarusway
            MYSQL_PASSWORD: Clarusway_1
        networks:
            - clarusnet
    myapp:
        build: .
        depends_on:
            - database
        restart: always
        ports:
            - "80:80"
        networks:
            - clarusnet

networks:
    clarusnet:
        driver: bridge
```

## Part 3 - Deployments and Services

- We need two images and we have just one that is mysql:5.7. So we build the other one. Firstly we change to-do-api.py file to get `MYSQL variables` from environment variables instead of py file.

- We just change the below statement ...

```py
# Import Flask modules
from flask import Flask, jsonify, abort, request, make_response
from flaskext.mysql import MySQL

# Create an object named app
app = Flask(__name__)

# Configure mysql database
app.config['MYSQL_DATABASE_HOST'] = 'database'
app.config['MYSQL_DATABASE_USER'] = 'clarusway'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Clarusway_1'
app.config['MYSQL_DATABASE_DB'] = 'todo_db'
```

- ... with this one below. Owing to `os` module we can get `MYSQL variables` from environment variable. Thanks to this, we do not need to change image even if `MYSQL variables` changes.

```py
# Import Flask modules
from flask import Flask, jsonify, abort, request, make_response
from flaskext.mysql import MySQL
import os

# Create an object named app
app = Flask(__name__)

# Configure mysql database
app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST')
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE')
```

- Build the image and push it to dockerhub.

```bash
docker build -t clarusways/todoapi-pod .
docker push clarusways/todoapi-pod
```


- Create a file and name it todoapi-kubernetes.

```bash
mkdir todoapi-kubernetes && cd todoapi-kubernetes
```

- Create a deployment for database microservice and name it `db-clarus-deploy.yaml` 

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: clarus-db-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: clarus-db
  template:
    metadata:
      labels:
        app: clarus-db
    spec:
      containers:
      - name: clarus-db
        image: mysql:5.7
        ports:
        - containerPort: 3306
        env:
          - name: MYSQL_ROOT_PASSWORD
            value: R1234r
          - name: MYSQL_DATABASE
            value: todo_db
          - name: MYSQL_USER
            value: clarusway
          - name: MYSQL_PASSWORD
            value: Clarusway_1
```

- Run the `clarus-db-deploy` and list it.

```bash
kubectl apply -f db-clarus-deploy.yaml
kubectl get po
```

- Create a service for database and name it `db-clarus-service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: clarus-db-service
  labels:
    name: clarus-db-service
spec:
  type: ClusterIP
  selector:
    app: clarus-db
  ports:
  - protocol: TCP
    port: 3306
    targetPort: 3306
```

- Run the `clarus-db-service` and list it.

```bash
kubectl apply -f db-clarus-service.yaml
kubectl get svc
```

- Create a deployment for todoapi-pod microservice and name it `todoapi-deploy.yaml`. Pay attention to environment variables. We pass this variables to our to-do-api.py.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: todo-api-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: todo-api
  template:
    metadata:
      labels:
        app: todo-api
    spec:
      containers:
      - name: todo-api
        image: clarusways/todoapi-pod
        ports:
        - containerPort: 80
        env:
          - name: MYSQL_DATABASE_HOST
            value: clarus-db-service
          - name: MYSQL_DATABASE
            value: todo_db
          - name: MYSQL_USER
            value: clarusway
          - name: MYSQL_PASSWORD
            value: Clarusway_1
```

- Run the `todo-api-deploy` and list it.

```bash
kubectl apply -f todoapi-deploy.yaml
kubectl get po
```

- Create a service for todoapi-pod microservice and name it `todoapi-service.yaml`.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: todoapi-service
  labels:
    name: todo-api
spec:
  type: NodePort
  selector:
    app: todo-api
  ports:
  - port: 8080
    targetPort: 80
    nodePort: 30001
```

- Run the `todoapi-service` and list it.

```bash
kubectl apply -f todoapi-service.yaml
kubectl get svc
```

- List the pods and services.

```bash
kubectl get po,svc
```

- Do not forget to open port 30001. Then in a browser check your work:
`http://<your ec2 instances public IP>30001`

- Delete all pods and services.

```bash
kubectl delete -f .
```

## Part 4 - Secrets and ConfigMaps

- We need to creata secrets for password. So we encode passwords with `base64`.

```bash
echo -n R1234r | base64
UjEyMzRy

echo -n Clarusway_1 | base64
Q2xhcnVzd2F5XzE=
```

- Create a secret for mysql variables with `todoapi-secret.yaml` and put these encoding variables.

```yaml
apiVersion: v1
kind: Secret
metadata: 
    name: todoapi-secret
type: Opaque
data: 
    mysql-root-password: UjEyMzRy
    mysql-admin-password: Q2xhcnVzd2F5XzE=
```

- Create todoapi-secret and list it.

```bash
kubectl apply -f todoapi-secret.yaml 
kubectl get secrets
```

- Change the environment variables related with passwords of `db-clarus-deploy.yaml` and` todoapi-deploy.yaml` to secrets. Firstly change `db-clarus-deploy.yaml`.

```yaml
        env:
          #- name: MYSQL_ROOT_PASSWORD
          #  value: R1234r
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: todoapi-secret
              key: mysql-root-password
        - name: MYSQL_DATABASE
          value: todo_db
        - name: MYSQL_USER
          value: clarusway
        #- name: MYSQL_PASSWORD
        #  value: Clarusway_1
        - name: MYSQL_PASSWORD
          valueFrom:
            secretKeyRef:
              name: todoapi-secret
              key: mysql-admin-password
```

- After that change the `todoapi-deploy.yaml`.

```yaml
        env:
        - name: MYSQL_DATABASE_HOST
          value: clarus-db-service
        - name: MYSQL_DATABASE
          value: todo_db
        - name: MYSQL_USER
          value: clarusway
        #- name: MYSQL_PASSWORD
        #  value: Clarusway_1
        - name: MYSQL_PASSWORD
          valueFrom:
            secretKeyRef:
              name: todoapi-secret
              key: mysql-admin-password
```

- Create a ConfigMap for environment variables with `todoapi-configmap.yaml` and put variables below.

```yaml
apiVersion: v1
kind: ConfigMap
metadata: 
    name: todoapi-configmap
data: 
    DATABASE_URL: clarus-db-service
    USER: clarusway
    DB: todo_db
```

- Create todoapi-configmap and list it.

```bash
kubectl apply -f todoapi-configmap.yaml 
kubectl get configmaps
```

- Change the environment variables of `db-clarus-deploy.yaml`.

```yaml
        env:
          #- name: MYSQL_ROOT_PASSWORD
          #  value: R1234r
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: todoapi-secret
              key: mysql-root-password
        #- name: MYSQL_DATABASE
        #  value: todo_db
        - name: MYSQL_DATABASE
          valueFrom:
            configMapKeyRef:
              name: todoapi-configmap
              key: DB
        #- name: MYSQL_USER
        #  value: clarusway
        - name: MYSQL_USER
          valueFrom:
            configMapKeyRef:
              name: todoapi-configmap
              key: USER
        #- name: MYSQL_PASSWORD
        #  value: Clarusway_1
        - name: MYSQL_PASSWORD
          valueFrom:
            secretKeyRef:
              name: todoapi-secret
              key: mysql-admin-password
```

- Then change the `todoapi-deploy.yaml`.

```yaml
        env:
        #- name: MYSQL_DATABASE_HOST
        #  value: clarus-db-service #.default.svc.cluster.local
        - name: MYSQL_DATABASE_HOST
          valueFrom:
            configMapKeyRef:
              name: todoapi-configmap
              key: DATABASE_URL         
        #- name: MYSQL_DATABASE
        #  value: todo_db
        - name: MYSQL_DATABASE
          valueFrom:
            configMapKeyRef:
              name: todoapi-configmap
              key: DB
        #- name: MYSQL_USER
        #  value: clarusway
        - name: MYSQL_USER
          valueFrom:
            configMapKeyRef:
              name: todoapi-configmap
              key: USER
        #- name: MYSQL_PASSWORD
        #  value: Clarusway_1
        - name: MYSQL_PASSWORD
          valueFrom:
            secretKeyRef:
              name: todoapi-secret
              key: mysql-admin-password
```

## Part 5 - Volumes

- Log into the `kube20-worker-1` node, create a `clarus-data` directory under home folder.

```bash
mkdir clarus-data
```

- Log into `kube20-master` node and create a `pv-clarus.yaml` file using the following content with the volume type of `hostPath` to build a `PersistentVolume`.

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: clarus-pv-volume
  labels:
    type: local
spec:
  storageClassName: manual
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/home/ubuntu/clarus-data"
```

- Create the PersistentVolume `clarus-pv-volume` and list it.

```bash
kubectl apply -f pv-clarus.yaml
kubectl get pv
```

- Create a `pv-claim-clarus.yaml` file using the following content to create a `PersistentVolumeClaim`.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: clarus-pv-claim
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
```

- Create the PersistentVolumeClaim `clarus-pv-claim` and list it.

```bash
kubectl apply -f pv-claim-clarus.yaml
kubectl get pvc
```

- Now we add the volume to `db-clarus-deploy.yaml` so we get below statement.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: clarus-db-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: clarus-db
  template:
    metadata:
      labels:
        app: clarus-db
    spec:
      containers:
      - name: clarus-db
        image: mysql:5.7
        ports:
        - containerPort: 3306
        env:
          #- name: MYSQL_ROOT_PASSWORD
          #  value: R1234r
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: todoapi-secret
              key: mysql-root-password
        #- name: MYSQL_DATABASE
        #  value: todo_db
        - name: MYSQL_DATABASE
          valueFrom:
            configMapKeyRef:
              name: todoapi-configmap
              key: DB
        #- name: MYSQL_USER
        #  value: clarusway
        - name: MYSQL_USER
          valueFrom:
            configMapKeyRef:
              name: todoapi-configmap
              key: USER
        #- name: MYSQL_PASSWORD
        #  value: Clarusway_1
        - name: MYSQL_PASSWORD
          valueFrom:
            secretKeyRef:
              name: todoapi-secret
              key: mysql-admin-password
        volumeMounts:
        - name: clarus-persistent-storage
          mountPath: /var/lib/mysql
      volumes:
      - name: clarus-persistent-storage
        persistentVolumeClaim:
          claimName: clarus-pv-claim
```

- Run all yaml files again and in a browser check your work:
`http://<your ec2 instances public IP>30001`.

```bash
kubectl apply -f .
```

- Delete all objects.

```bash
kubectl delete -f .
```