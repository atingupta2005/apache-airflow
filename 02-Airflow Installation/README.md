# Airflow Installation
- Using Production Docker Images
- Using Official Airflow Helm Chart
- Using Managed Airflow Services
- Using 3rd-party images, charts, deployments


## Using Production Docker Images
- Useful when you are familiar with Container/Docker stack
- The images are build by Apache Airflow release managers and they use officially released packages from PyPI

### Building the image
- Refer: https://airflow.apache.org/docs/apache-airflow/2.0.1/production-deployment.html
```
FROM apache/airflow
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow
```

```
docker build . --tag "my-stable-airflow:0.0.1"
```

```
docker run -itd -p 8089:8080 --env "_AIRFLOW_DB_UPGRADE=true" --env "_AIRFLOW_WWW_USER_CREATE=true" --env "_AIRFLOW_WWW_USER_PASSWORD=admin" --name airflow_prod_02 my-stable-airflow:0.0.1 webserver
docker logs -f airflow_prod_02
docker exec -itd airflow_prod_02 airflow scheduler
docker ps
```

```
curl localhost:8089
# Login using admin/admin
```


## Using Official Airflow Helm Chart
- Useful when you are not only familiar with Container/Docker stack but also when you use Kubernetes and want to install and maintain Airflow using the community-managed Kubernetes installation mechanism via Helm chart.
- Provides capabilities of easier maintaining, configuring and upgrading Airflow in the way that is standardized and will be maintained by the community.
- The Chart uses the Official Airflow Production Docker Images to run Airflow.

### Installing the Chart
```
kubectl create namespace airflow
helm repo add apache-airflow https://airflow.apache.org
helm install airflow apache-airflow/airflow --namespace airflow
```

### Upgrading the Chart
```
helm upgrade airflow apache-airflow/airflow --namespace airflow
```

### Uninstalling the Chart
```
helm delete airflow --namespace airflow
```

## Using Managed Airflow Services
- When you prefer to have someone else manage Airflow installation for you, there are Managed Airflow Services that you can use.
- Airflow Community does not provide any specific documentation for managed services. Please refer to the documentation of the Managed Services for details.

## Using 3rd-party images, charts, deployments
- Those installation methods are useful in case none of the official methods mentioned before work for you, or you have historically used those.
- It is recommended though that whenever you consider any change, you should consider switching to one of the methods that are officially supported by the Apache Airflow Community or Managed Services.
- Airflow Community does not provide any specific documentation for 3rd-party methods
