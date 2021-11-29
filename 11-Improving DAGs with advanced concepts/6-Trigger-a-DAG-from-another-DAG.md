# Trigger a DAG from another DAG
## Controller DAG
- Open file - triggerdagop_controller_dag.py
- Notice the task - trigger which is using TriggerDagRunOperator
- Notice the function - conditionally_trigger. Notice that we have a new parameter - dag_run_obj
- This parameter is automatically given by the TriggerDagRunOperator and it corresponds to a simple class composed by run_id and a payload. This payload allows to send data from the controller DAG to the target DAG
- Payload is a dictionary with a key value pair message having the value given from the params "Hi from the controller" is assigned to the payload attribute
- If the value of condition_param = True, then the dag_run_object is returned and the target DAG triggerdagop_controller_dag is triggered

## Target DAG
- Open file triggerdagop_target_dag.py
- It has 3 tasks
- Task t1 prints the message sent from controller DAG
- Notice the function remote_value which access the context and get the value of message
- Task t2 also retries the value but in a different way
- Task t3 just execute sleep for 30 seconds. Its just show that controller DAG can finish before the target DAG
- Start docker container
```
docker-compose -f docker-compose-CeleryExecutor.yml up -d
docker ps
```
- Open Airflow UI
- First enable DAGs - triggerdagop_controller_dag
- Then enable DAG - triggerdagop_target_dag
- We need to open in this order because since the start_date of the controller DAG is one day before, it will be triggered as soon as we start scheduling it but the target DAG will not be scheduled to run.
- Refresh the page
- Notice that the controller DAG is finished but the target DAG is still running
- Once both DAGs are run, take a look at the logs of the target and notice that there is a string - "Hi from the controller"
- Keep everything running for next practical
