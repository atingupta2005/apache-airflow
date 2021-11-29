# Monitoring Airflow with TIG stack
- Open docker-compose-CeleryExecutorTIG.yml
  - Notice services for telegraf, influxdb, grafana

## Configure Telegraf
- Open telegraf.conf
  - [[outputs.influxdb]]
    - urls = ["http://influxdb:8086"]
    - database = "telegraf"
    - skip_database_creation = true  # We will create using docker container
    - timeout = "5s"
    - username = "telegraf"   # To define the user account that will be used by Telegraf to send metrics into InfluxDB.
    - password = "telegrafpass"
    - user_agent = "telegraf"
- Now output plugin InfluxDB is configured and Telegraf os ready to send data to it. So, the output is set but the input where Telegraf will receive the metrics coming from Airflow needs to be configured as well.

- Configure input
  - [[inputs.statsd]]
    - Uncomment all the lines of this section
  - Telegraf will start a StatdD daemon listening on the port 8125 in UDP for metrics coming from Airflow
- Save file

## Configure Airflow
- Open airflow.cfg
- Look for the section statsd
  - statsd_on = True
  - statsd_host = telegraf
  - statsd_port = 8125
  - statsd_prefix = airflow

- Now Airflow is configured to send its metrics into the input plugin statsd of Telegraf.
- Now look for the parameter - remote_logging
  - remote_logging = False


## Start Airflow
```
docker-compose -f docker-compose-CeleryExecutorTIG.yml up -d
docker ps
```

## Create database telegraf and user
- It will be used by Telegraf for sending the metrics
- Connect to InfluxDB
```
docker exec -it <container-id-of-influxdb> influx
```

- InfluxDB Commands
```
create database telegraf
create user telegraf with password 'telegrafpass'
```
- Exit docker container by pressing CTRL+D
- Open Grafana - localhost:3000 and login
- Notice Grafana Dashboard
- There are 2 steps to be followed now
  - Add data source corresponding to the InfluxDB instance we set up where the metrics of Airflow are stored.
- Click "add data source" and select "InfluxDB"
- Click Add datasource - Select InfluxDB
- HTTP
  - URL - http://influxdb:8086
- InfluxDB details
  - Database: telegraf
  - User: telegraf
  - Password: telegrafpass
- Click Save and Test
- Go back to Grafan Homepage
- Click New Dashboard and click "Add query"
- Here you define the query that will fetch the metrics you want from InfluxDB
- For example if you click on "select measurement", all the measurements prefixed by "airflow_" corresponds to the different metrics available of Airflow
- Open Airflow UI
- Enable data_dag and logger_dag
- Open Grafana page and select "airflow_dagbag_size".
- Click on mean and remove
- Click on plus in SELECT and chose last from Selectors
- Remove Group By
- From left click on Visualization
- Select Gauge
- Under display click on Mean and select Last
- Notice that there is a Gauge created
- Click General from left and set Title - "Number of Imported DAGs"
- Click Save dashboard from Top right of the page. Name - Airflow

- Hence the first Dashboard for monitoring Airflow instance with Grafana, InfluxDB and Telegraf
