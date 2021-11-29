# Changing how tasks are triggered
- Refer trigger_rule_dag.py
- Inspect the code
- Notice that there are commented code instructions for raising exceptions
- Notice the task dependencies
- Start Airflow UI
```
docker-compose -f docker-compose-CeleryExecutor.yml up -d
docker ps
```
- Open Airflow UI
- Open trigger_rule_dag
- Open Graph View and notice the DAG and tasks
- Notice the trigger rules set based on our DAG
- Open Airflow UI and trigger DAG
- Review the Graph View
- Do changes in trigger rules and trigger DAG multiple times to understand the impact of trigger rules
- Stop Airflow UI
```
docker-compose -f docker-compose-CeleryExecutor.yml down
docker ps
```
