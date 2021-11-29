# Monitoring DAGs with Elasticsearch and Kibana
- To create a Dashboard let's generate some log events
- Open Airflow UI
- Enable data_dag
  - It has 3 tasks
  - Last task fails half of the time based on the current date
  - Open DAG -> Graph View
  - Open task fail
  - Click Rendered
  - Notice Bash command being executed by the task
  - Value of valid corresponds to the day of execution date. Since the start_date is set 10 days ago and the catchup parameter is enabled, the execution will change during the backfill process
- Open Tree View and wait for the DAG runs to finish
- Open Kibana UI
- Open Index Management and notice that we now have an index
- So the log events are now stored in Elasticsearch
- Let's create the mapping again
- Click on "Index Patterns", "Create index pattern". Type "airflow-logs-*"
- Click Next Step
- Select @Timestamp and click "Create Index Pattern"

## Create Visualization
- Composed of multiple visualizations which are based on the Elasticsearch requests
- Let's create the first one
- From left panel, click Visualize and click "Create new visualization"
- Chose Gauge. It indicates if a given value goes beyond a defined threshold. We will use it to monitor if a given DAG goes beyond a number of errors and so be warned because it may be in trouble.
- Then chose - airflow-logs-*
- In left, we have options to customize the visualization
  - Metric Label: Number of failed tasks
  - Click Buckets -> Add -> Split Group
  - Select Aggregation Terms
  - Select dag_id.keyword
- By following above steps, we will obtain one Gauge for each DAG id existing in the log events
- Open Airflow UI
- Enable logger_dag
- Refresh Page
- Open Kibana
- Click button Refresh from top right
- Notice we have new Gauge with the dag id logger_dag. The number in Gauge corresponds to the total number of log events since we don't filter anything
- Let's apply a filter so that we only keep the tasks having failed
  - From search bar, click on it and type - "message" and select message
    - message: "Task exited with return code 1"
  - Since our DAGs are scheduled to run every day, it would be better to have information on the past 7 days.
  - To do this, click on the calendar next to search bar and select last 7 days
  - Since logger_dag has no any failed tasks, if we change 1 with 0 on search bar, we obtain the 2 gauges as expected
  - Now undo the modifications and change 0 by 1 again in search bar and we obtain the number of tasks having failed from the dag - data_dag
  - Since the number is below 50, it is still considered as working fine
  - If we want to define that above 10 errors the DAG should be considered in trouble
  - Click options, here we can define the different ranges
    - 0, 10
    - 10, 100
  - Apply modifications and notice that Gauge is in Red as expected
- Save visualization with name - dag_id_gauge
- Hence our first visualization is created

## Create another visualization
- Click visualization from left menu
- Select vertical bar at bottom
- Select index
- Create Bucket - X axis - aggregation - Terms and the field - task_id-keyword
- Click Apply changes
- It will show the number of log events by tasks
- Save the visualization with name - task_id_vertical_bar

## Create Dashboard
- Open Dashboard and crate new dashboard
- Click Add and then add both the visualizations
- Notice both visualizations are added to the Dashboard
- Save Dashboard with name - Dag Monitoring
- Turn on - Store time with Dashboard and click Save

## Stop Airflow
```
docker-compose -f docker-compose-CeleryExecutorELK.yml down
docker ps
```
