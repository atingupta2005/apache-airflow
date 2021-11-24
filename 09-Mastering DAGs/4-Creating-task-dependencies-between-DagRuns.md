# Creating task dependencies between DagRuns
- Refer - depends_dag.py
- It's scheduled to run every day at mid night
- This has 3 tasks out of which 2 are python functions
- Both functions print either a message or raise an exception
- Notice the tasks dependency on the bottom of the code

## Parameter - depends_on_past
- Defines whether given task execution depends on the result of the past task execution
- Set the parameter to true in second python task
- Change date to 02-01-2019 1:00 AM local time (UTC+1)
```
sudo date --set "02 Jan 2019 01:00:00"
```
- Run - start.sh
- Open Airflow UI
- Refresh Airflow UI page
- Enable - depends_task
- Refresh the page and wait DAG run to finish
- Open Tree View
- All tasks are green
- Uncomment the exception code in 3rd task
- Change date to 03-01-2019 1:02 AM
```
sudo date --set "03 Jan 2019 01:02:00"
```
- Refresh the Page
- 3rd task is failed and entire DAG run has failed status
- Now uncomment error code from 2nd function and comment in 3rd exception
- Change date to 04-01-2019 1:05 AM
```
sudo date --set "04 Jan 2019 01:05:00"
```
- Refresh the page and notice that 2nd task is failed and 3 thirst task is marked as upstream task failed
- Change code of second_task - comment raise instruction and uncomment the print instruction
- Change date to 05-01-2019 1:10 AM
```
sudo date --set "05 Jan 2019 01:15:00"
```
- Refresh the Page, DAG should be running
- Notice that the task 2 and 3 are not executed as we set depends_on_past to true
- Now we can clear the failed status of the failed task in previous DAG run
  - Click on the red square of the failed task
  - Click on Mark Success
  - Now refresh the page and the task from last DAG run is successfully executed

## Wait for downstream
 - depends_on_past will be set to True automatically
- Refer: https://www.waitingforcode.com/apache-airflow/apache-airflow-sequential-execution/read

- Set the current date to - 19-12-2019 3-30 AM
```
sudo date --set "19 Dec 2019 03:30:00"
```
- Open terminal and run stop.sh and start.sh
- Remove the parameter - depends_on_past
- In task 1, add wait_for_downstream=True
- Enable DAG - depends_dag
- Trigger dag manually
- Notice all tasks are executed successfully
- Now enable raise error code in second_task
- Trigger DAG again
- Notice that DAG and specific task is failed
- Undo modification in the code
- Trigger DAG again
- Notice that none of the tasks are executed
- Now let's clear the error on the failed task in previous DAG run
- Now all tasks will be executed in current DAG run
