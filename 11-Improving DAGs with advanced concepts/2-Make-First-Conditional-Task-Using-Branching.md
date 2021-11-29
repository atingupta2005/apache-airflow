# Make First Conditional Task Using Branching
- How to conditionaly execute tasks
- Refer branch_dag.py
- This DAG is for requesting different APIs in order to geolocate IP addresses
- There is a function - check_api(). It checks the API if that is working. If API return data having the field country, this function returns that
- The returned value is then processed by the BranchPythonOperator in order to execute the corresponding task
  - If the value returned is "ipstack", then the task "ipstack" will be executed and the other tasks will be skipped
- If no API is available, the check_api function returns "none" and so only the task "none" will be executed
- If the tasks corresponding to the APIs are created from the "for loop" as well as the dependencies with the branch task and the store task
- Start Airflow
```
docker-compose -f docker-compose-CeleryExecutor.yml up -d
docker ps
```
- Open Airflow UI
- Open branch_dag and open tab - Graph View
- There are several tasks in it
- Enable the DAG
- Trigger the TAG
- Refresh Page
- Notice that DAG is failed and only 2 tasks are executed
- The task - save is skipped. We need this task to get executed. It's skipped as the trigger rule is that all the previous tasks should be executed successfully
- We need to change trigger rule
- Open branch_dag.py and specify trigger rule for the task Save
  - trigger_rule='one_success'
- Now trigger DAG again
- Notice that Save task is now executed

## Return multiple task ID to chose multiple branches at once
- Modify branch_dag.py and update check_api()
```
apis = []
apis.append(api)
return apis if len(apis) > 0 else 'none'
```
- Open Airflow UI and refresh page
- Trigger DAG
- Refresh Page
- Open Graph View
- Notice 2 tasks are now executed
- Stop Airflow
```
docker-compose -f docker-compose-CeleryExecutor.yml down
```
