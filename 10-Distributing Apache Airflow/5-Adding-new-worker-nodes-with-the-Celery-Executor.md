# Adding new worker nodes with the Celery Executor
- Open airflow.cfg and change the value of sql_alchemy_conn to specify connection string of postgrss database
```
vim mnt/airflow/airflow.cfg
```

```
postgresql+psycopg2://airflow:airflow@postgres:5432/airflow
```
- Set executor = CeleryExecutor
- Set result_backend = db+postgresql://airflow:airflow@postgres:5432/airflow
  - When a job finishes, the Executor needs to update the metadata of the job. Therefore it will insert a message into a database that will be used by the scheduler to update the state of the task
- We had used the same value in environment variable when we defined docker-compose-CeleryExecutor.yml
- If we want to use mysql instead of postgres, we would just need to change all the references of postgres to mysql
- Set broker_url = redis://:redispass@redis:6379/1
- Open terminal add this node to cluster

- Stop existing
```
docker-compose -f docker-compose-CeleryExecutor.yml down
```

- Start existing Airflow cluster
```
docker-compose -f docker-compose-CeleryExecutor.yml up -d
```
## Create new worker node
```
docker-compose -f docker-compose-CeleryExecutor.yml scale worker=2
```
- Open flower dashboard and notice that now there are 2 worker nodes
- Open Airflow UI and enable parallel_dag
- Refresh Page
- Open Flower dashboard and notice that both workers are executing tasks

- Stop Airflow
```
docker-compose -f docker-compose-CeleryExecutor.yml down
```
