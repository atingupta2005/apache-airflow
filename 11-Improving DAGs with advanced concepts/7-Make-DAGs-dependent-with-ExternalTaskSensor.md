# Make DAGs dependent with ExternalTaskSensor
- Refer - externaltasksensor_dag.py
- This DAG has 2 tasks - sensor and last_task
- Task - sensor is using external_dag_id and external_task_id
  - We are actually waiting for the task t2 in sleep_dag to finish before the next task in this DAG can start
- Open sleep_dag.py
- Review its code
- Notice that the start_date and schedule interval of both the DAGs are same
- Start Airflow UI
```
docker-compose -f docker-compose-CeleryExecutor.yml up -d
docker ps
```
- Open Airflow UI in 2 separete browsers
- Open DAG - externaltasksensor_dag in one browser and sleep_dag in another
- Execution of the DAG externaltasksensor_dag depends on the execution of the task t2 from the DAG sleep_dag
- Open Graph view on both the browsers
- Refresh the pages and observe the behaviour
- Stop Airflow
```
docker-compose -f docker-compose-CeleryExecutor.yml down
docker ps
```
