# Sharing data with XCOMs
- We need to understand how xcoms work
- Open xcom_dag.py
- Review the code of tasks
- Start Airflow
```
docker-compose -f docker-compose-CeleryExecutor.yml up -d
docker ps
```
- Open Airflow UI
- Enable DAG xcom_dag
- Trigger DAG
- Refresh Page
- Open Admin -> XCOMS
- Notice the key/values
- What xcom is pushed by task t0, task t1 tries to pull it
- Notice the function get_pushed_xcom_with_return
- Open Airflow UI
- Open xcom_dag ->Tree View and open the logs of task t1
- In the logs, notice that the value my_returned_xcom from the xcom has been well pulled as shown
  - Note: When we don't specify the key in the command xcomm_pull then the default value to that key is return_value. So specifying the key - return_value is not necessary
- So we are noe able to push and pull xcom
- There are 2 other ways to push and pull xcoms

## Other ways to push and pull xcoms
- In code of xcom_dag, the task t2 pushed the xcom
- Notice the function push_next_task
- Here instead of returning the value, we are using xcom_push and specifying the key and values both
- Then notice the task - branching and the function get_next_task
- In get_next_task, the value is being pulled by specifying the key and that value is being return
- Open Airflow UI
- Open variables from Admin
- Notice that there is a key - next_task which is created by the task t3
- Open Tree View
- Click task - branching and click Log
- Inspect logs

## Pull multiple values from xcoms
- We can pull multiple xcoms at once by specifying different task ids in the xcom_pull method
- Open code of DAG and notice the task t5
- Notice function - get_multiple_xcoms
- Open Airflow UI -> Tree View and click task t5 then "View Log"
- From the logs, notice that there is a tuple with 2 values
- Stop Airflow
```
docker-compose -f docker-compose-CeleryExecutor.yml down
```
