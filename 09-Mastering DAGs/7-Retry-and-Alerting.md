# Retry and Alerting
- Refer - alert_dag.py
- Start Airflow
```
./start.sh
```
- Open Airflow UI
- Enable DAG - alert_dag
- Trigger dag by setting date in future
- Notice how much time it took to execute - 45 sec approx
- Refresh page
- Edit file
```
vi mnt/airflow/dags/alert_dag.py
```
- Change code - dagrun_timeout=timedelta(seconds=75) and save
```
with DAG(dag_id='alert_dag', schedule_interval="0 0 * * *", default_args=default_args, catchup=True, dagrun_timeout=timedelta(seconds=75)) as dag:
```
- Trigger dag again by setting date in future
- Notice how much time it took to execute - 45 sec approx
- Change code - dagrun_timeout=timedelta(seconds=45) and save
- Trigger dag again by setting date in future
- Notice how much time it took to execute - its failed as timeout happens
- In addition to timeout, we would like to do something if the DAGRun is failed or succeeded. We could add the callbacks on_failure_callback
- Refer to the functions - on_success_dag and on_failure_dag and also the callbacks in DAG object creation
- Now if DAG is success or failed, callback will be in effect accordingly
- We need to check scheduler logs
```
docker exec -it airflow bash
cd
cd logs/scheduler
ls
cd latest
cat alert_dag.py.log | grep failure
cat alert_dag.py.log
exit
```
- Open alert_dag.py and change dagrun_timeout from 25 to 75 seconds
- Now let's see how to handle if task fails. There are certain parameters to handle that
- Define the parameter in default_args
  - 'retries': 3
  - 'retry_delay': timedelta(seconds=60)
- Change bash command of t1 to make it fail - "exit 1"
- Trigger the DAG from Airflow UI
- In default_args, add parameters
  - on_failure_callback
  - on_success_callback
  - 'execution_timeout': timedelta(seconds=60)
    - Used for default timeout of every task in the DAG
- Trigger the dag and check the logs for the callback
