# Configuring Airflow with Elasticsearch
- Enable Airflow to send log events to ELK
- Airflow needs that each log message has the field - offset
  - Number to read in the right order
  - Its defined through filebeat
- Airflow needs that each log message has the field - log_id
  - {dag_id}-{task_id}-{execution_date}-{try_number}
  - Must be defined through Logstash

## Practice
- Review docker-compose-CeleryExecutorELK.yml
  - Notice services
    - Elasticsearch
    - Kibana
    - Logstash
      - Has the volume which corresponds to the folder containing the Logstash pipelines where the logs will be shipped and processed.

- Review - logstash/pipeline/airflow-logs.conf
- The logs of Airflow will go through this pipeline
- This pipeline is divided in 3 parts
  - The input: We specify here that the log event will come from Filebeat on the port 5044
  - Filter: Defined transformations in order to parse JSON data. It generates the log_id field and move the field offset to the root of the JSON document
  - Output: Here the processed log event is redirected to Elasticsearch

- Modify airflow.cfg
  - remote_logging = True
  - remote_log_conn_id =
  - remote_base_log_folder =
  - host = http://elasticsearch:9200
  - write_stdout =
  - json_format = True
- Start Airflow
```
docker-compose -f docker-compose-CeleryExecutorELK.yml up -d
docker ps
```
- Open localhost:9200
- Open localhost:5601
- Open Airflow UI - localhost:8080
- Connect docker worker
```
docker ps
docker exec -it <worker-container-id> bash
```
- Now Airflow is configured to read task logs from Elasticsearch.
- Now we need to setup Filebeat on order to ship the logs into Logstash to finally store them into Elasticsearch so that we will be able to read them from the Airflow UI
- Download Filebeat
```
curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.5.2-linux-x86_64.tar.gz
tar xvzf filebeat-7.5.2-linux-x86_64.tar.gz
ls
cd filebeat-7.5.2-linux-x86_64
ls
vim filebeat.yml
```
- Configure filebeat.yaml
```
  enabled: true
  paths:
      - /usr/local/airflow/logs/*/*/*/*.log
  #output.elasticsearch:
     #host: ["localhost:9200"]
  output.logstash:
    hosts: ["logstash:5044"]

```
- Save and Quit
- Run filebeat
```
./filebeat -e -c filebeat.yml -d "publish"
```
- Open Airflow UI
- Enable logger_dag
- Refresh the page
- Open Kibana - localhost:5601
- Click - Explore on my own
- From left panel, click on last icon - > Index Management
  - Notice we have an index named airflow-logs-<current-date>
- Click index patterns
- Click - Create Index Pattern
- Type the index pattern that should match with the Elasticsearch index below
  - airflow-logs-*
- Click - Next Step
- Select - @timestamp
- Click - Create index pattern
- Review the mapping
- From left panel, click - Discover
  - Notice that the log events are there from Airflow
  - Review and open the log entries
- Notice log level, log id, offset, task id in the log entry
- Notice the transformation we made to the field - offset
- We also have the field log.offset which is created by default by Filebeat and by applying our transformation we copied the same value by to the field - offset. This is required since Airflow requests on a field called offset and not log.offet
- Open Airflow UI
- Open logger_dag -> Graph View
- Open t2 and click View Log
- Notice that Airflow is able to retrieve the logs from Elasticsearch
- We can also build Dashboard to monitor Dags using Kibana and Elasticsearch. We will do it next
- Cleaning
  - Disable logger_dag
  - Open Browse -> Task Instances
  - Select all the tasks and click Clear
  - Open Browse -> Task Instances
  - Select all the Dag Runs and click Delete
  - Open IDE and delete the folder mnt/airflow/logs/logger_dag
  - Open Kibana
  - Click last icon from left panel
  - Open Index Management
  - Select Index -> Click Manage Index -> Delete Index
  - Click Index Pattern -> Select Pattern -> Click Red button from top right to delete it
