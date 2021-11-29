# Setting up custom logging
- Start Airflow
```
docker-compose -f docker-compose-CeleryExecutor.yml up -d
docker ps
```
- Check the logs of Airflow scheduler
```
docker logs -f <container-id-of-scheduler>
```
- Open airflow.cfg
  - base_log_folder: specifies where the logs will be stored
  - loggig_level
- Restart Airflow and view logs
```
./restart.sh
docker ps
docker logs -f <container-id-of-scheduler>
```
- Notice that we have much less logs
- Open airflow.cfg
  - Set logging_level = INFO
  - fab_logging_level: Logging level of flask-app-builder UI
  - logging_config_class: To do customization in the logging
  - Section - Log Format
  - Section - Log filename format
- Open Airflow UI
- Enable logger_dag
- Open IDE
- Open folder logs. There are 3 folders in it
  - dag_processor_manager
    - Contains the logs related to the processing by Airflow
    - It parses and analyses the DAGs to see what tasks should be run
    - Creating appropriate tasks instances in the database, recording any errors, killing any task instances belonging to the DAGs that haven't issued a heartbeat in a while and so on
    - Open the log file and review it
  - scheduler
    - Contains logs related to the schedule of tasks
    - If we look at the task t1 which is a task of the DAG logging_dag, you can see when the task has been scheduled and triggered
  - When we schedule a DAG, a folder with the DAG name is created in the logs. Then a folder is created for each task with the corresponding logs
    - If we open the folder logger_dag folder, t1 and the most recent execution date, then open the file 1.log. We will obtain the output produced by the execution of the task - t1. Notice that 1 here corresponds to how many times the task has been tried. So here t1 is executed 1 time.
    - If the task was retried 2 times, then we would have 2.log instead of 1.log
