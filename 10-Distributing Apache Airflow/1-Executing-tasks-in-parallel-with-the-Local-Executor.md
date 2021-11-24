# Executing tasks in parallel with the Local Executor
## Enable Parallism=1
- Refer
  - parallel_dag.py
  - docker-compose-LocalExecutor.yml
    - Notice the database details
    - Notice environment variable - EXECUTOR=Local
    - Set parallelism = 1
- Run docker compose file. It will take 5-10 min to finish

```
docker-compose -f docker-compose-LocalExecutor.yml up -d
```
- Open Browser
- Enable parallel_dag
- Refresh the page after 1 min
- Check Gantt view - one task at a time

## Enable Parallism=3
- Increase parallelism = 3
- Restart
```
docker-compose -f docker-compose-LocalExecutor.yml down
docker-compose -f docker-compose-LocalExecutor.yml up -d
```

- Open Airflow UI and Refresh
- Enable the toggle and refresh after 1 min
- Check Gantt view - 3 tasks at a time

## Enable dag_concurrency to specify how many tasks to run in parallel for each DAG
- Change dag_concurrency = 2
- Restart
```
docker-compose -f docker-compose-LocalExecutor.yml down
docker-compose -f docker-compose-LocalExecutor.yml up -d
```
- Open Airflow UI and Refresh
- Enable the toggle and refresh after 1 min
- Check Gantt view - 2 tasks at a time

## Understand the impact of dag_concurrency on 2 DAGs combined
- Make a copy of parallel_dag.py in same folder as next_dag.py
- Change the DAG id in next_dag.py
- Restart
```
docker-compose -f docker-compose-LocalExecutor.yml down
docker-compose -f docker-compose-LocalExecutor.yml up -d
```
- Open Airflow UI and Refresh
- Enable the toggle of both the DAGs and refresh after 1 min
- Check Gantt view of parallel_dag - 2 tasks initially and then 1 task
  - As we limited the number of tasks per dag run to 2
- Check Gantt view of next_dag - 1 task initially and then 2 tasks
  - As the total tasks for all DAG runs is set to 3

## Understand max_active_runs_per_dag
- Open parallel_dag.py and set catchup to True
- Restart
```
docker-compose -f docker-compose-LocalExecutor.yml down
docker-compose -f docker-compose-LocalExecutor.yml up -d
```
- Open Airflow UI and Refresh
- Enable the toggle for parallel_dag and refresh after 1 min
- Check Gantt view - Multiple instances of DAG Runs are running due to Catchup is True
- Open Tree view and refresh multiple times
- Notice the order in which the tasks of each DAG run is executed. There is something strange.
- It starts the tasks by level of dependencies for multiple DAG runs together
  - The first 3 tasks of each DAG run are trigerred
  - Then task 4 is trigerred
  - Then task 5 is triggered
  - Only 2 tasks are running in parallel. Refresh page multiple times and notice that only 2 tasks are running in parallel as defined in airflow.cfg
  - Finally, notice that Airflow stop scheduling new DAGRuns after reaching the 16th. But why?
  - It's due to the parameter max_active_runs_per_dag = 16
    - Means we can have upto 16 DAG runs per DAG
- Change the value max_active_runs_per_dag = 1
- Restart
```
docker-compose -f docker-compose-LocalExecutor.yml down
docker-compose -f docker-compose-LocalExecutor.yml up -d
```
- Open Airflow UI and Refresh
- Enable the toggle for parallel_dag and refresh after 1 min
- Check Tree View - Only 1 DAG run at a time and not 16
- If there is a dependency between DAG runs then set it to 1
- This parameters specifically matters because we use backfilling
- Stop docker container
