# Deploy and run Airflow with Kubernetes Executor on EKS
- We will install and execute our first DAG using Airflow through the Kubernetes Executor inside our EKS cluster
- We will first install Airflow inside EKS
- We have already made a chart for running Airflow with the KubernetesExecutor
- The first step is to add the catalogue where the template is
- Click on Global -> Apps -> Manage Catalogue
- Click Add Catalogue
  - Name: airflow-eks
  - Catalog URL: https://github.com/atingupta2005/airflow-helm-chart.git
  - Branch: master
  - Scope: global
- Click Create
- We have added our catalog, we will now install Airflow using that catalog
- Click Apps -> Launch
- Select Airflow-k8s-eks
  - Name: airflow-eks
  - Target Project: Default
  - Available Roles: Cluster
- Click - Launch
- Open it
- It will take 10 min to setup Airflow
- Open Apps -> nginx-ingress
- Click on the endpoint just below the nginx controller service. It will open Airflow interface
- Enable parallel_dag
- Connect to shell
- Run command
```
kubectl get nodes
kubectl get pods
```
