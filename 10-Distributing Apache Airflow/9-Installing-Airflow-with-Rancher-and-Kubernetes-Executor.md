# Installing Airflow on K8S directly

```
kubectl create namespace airflow
kubectl get namespaces
```

```
helm repo add apache-airflow https://airflow.apache.org
helm repo update
```

```
helm search repo airflow
helm uninstall airflow --namespace airflow
helm ls -n airflow
helm install airflow apache-airflow/airflow --namespace airflow --debug --timeout 20m0s
```

- You can see the number of the revision—currently it’s 1. In the future, if you make a mistake and want to go back to your previous version you can do that easily by using ```
helm ls -n airflow
kubectl get pods -n airflow
helm rollback airflow <Revision Number>.
```

## Configure Helm Chart
- Upgrade your Airflow instance to the latest version
```
helm show values apache-airflow/airflow > values.yaml
```

- Once it’s loaded, modify your Airflow instance. First, modify the Airflow version. Instead 2.0.0, change it to 2.1.0:
```
vi values.yaml
```

- Next, modify the executor to KubernetesExecutor

- To access the Airflow UI, change cluster ip to LoadBalancer in values.yaml
```
service:
    type: LoadBalancer
    ## service annotations
    annotations: {}
    ports:
      - name: airflow-ui
        port: "{{ .Values.ports.airflowUI }}"
```

## How to sync DAGs
- In the terminal you need to configure your chart with gitSync. Enable it by typing True
```
gitSync:
  enabled: true
  # git repo clone url
  # ssh examples ssh://git@github.com/apache/airflow.git
  # git@github.com:apache/airflow.git
  # https example: https://github.com/apache/airflow.git
  repo: https://github.com/atingupta2005/apache-airflow.git
  branch: main
  rev: HEAD
  depth: 1
  # the number of consecutive failures allowed before aborting
  maxFailures: 0
  # subpath within the repo where dags are located
  # should be "" if dags are at repo root
  subPath: "09-Mastering DAGs/mnt/airflow/dags"
```

- Upgrade Apache Airflow instance with
```
helm upgrade --install airflow apache-airflow/airflow -n airflow -f values.yaml --debug
```


- Get Public IP
```
kubectl get svc  -n airflow
```

- Open Airflow
  - URL: <Public-IP>:8080
  - Credentials: admin/admin

- Enable the DAGs and notice PODs are getting created for each task

- Logs with Airflow on Kubernetes
```
kubectl get pods  -n airflow
kubectl logs -f <pod-id> -n airflow
```

# Installing Airflow on K8S using Rancher
```
docker run  --name rancher  -d --restart=unless-stopped -p 80:80 -p 443:443 --privileged rancher/rancher:latest
```

- Reset rancher password:
```
docker exec -ti rancher  reset-password
#User Name: admin
```

- Create SSH Key
```
ssh-keygen -t rsa -b 4096 -C "your_email@domain.com"
cat /home/atingupta2005/.ssh/id_rsa.pub
```

- Create AKS using Rancher
  - North Europe
  - Standard D4s v3
  - 1.20.9
  - aks-dns-61282

- Create Namespace in AKS if needed
