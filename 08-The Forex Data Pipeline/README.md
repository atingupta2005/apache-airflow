# Data Pipeline Instructions
- Refer to the Dags in - ./mnt/airflow/dags
## Task 1
- I created some sample data in JSON for forex rates
- Goal is to verify that the URL having forex rates in available or not
- Refer - 08-The Forex Data Pipeline\mnt\airflow\dags\forex_data_pipeline.py
  - is_forex_rates_available
- Start airflow instance
```
./start.sh
```
- Open URL: <dns-name>:8080
  - Credentials: airflow/airflow
- Create HTTP connection named - forex_api
  - https://gist.githubusercontent.com
- Run the task
```
docker ps
docker exec -it <container-id> bash
airflow tasks test forex_data_pipeline is_forex_rates_available 2021-01-01
```

## Task 2
- Refer - 08-The Forex Data Pipeline\mnt\airflow\dags\forex_data_pipeline.py
  - is_forex_currencies_file_available
- Use file sensor - checks every 60 seconds for file existence
  - airflow.sensors.filesystem
- Create File (path) connection - forex_path
  - Extra
  ```
  {"path":"/opt/airflow/dags/files"}
  ```
- Run the task
```
docker ps
docker exec -it <container-id> bash
cd /opt/airflow/dags/files
ls
pwd  # Mounted from host system
airflow tasks test forex_data_pipeline is_forex_currencies_file_available 2021-01-01
```

## Task 3
- Refer - 08-The Forex Data Pipeline\mnt\airflow\dags\forex_data_pipeline.py
  - downloading_rates  
    - It download the corresponding pair of currencies according to base currency
    - Once we have those pair of currencies a new file - forex_rates.json will be created to store those values
- Run the task
```
docker ps
docker exec -it <container-id> bash
cd /opt/airflow/dags/files
ls
pwd
airflow tasks test forex_data_pipeline downloading_rates 2021-01-01
```
- Notice a new file is created in - ./airflow/dags/files/forex_rates.json

## Task 4
- if the downloaded file (forex_rates.json) is very big then we need to use HDFS. This task is all about this
- Refer - 08-The Forex Data Pipeline\mnt\airflow\dags\forex_data_pipeline.py
  - saving_rates
- Open Hue
  - <dns-name>:32762
  - Credentials: root/root
- Refer to the files/folders in Hue from left menu
  - Open root folder
  - We should get a new folder in it once we run the task

- Run the task
```
docker ps
docker exec -it <container-id> bash
cd /opt/airflow/dags/files
ls
pwd
airflow tasks test forex_data_pipeline saving_rates 2021-01-01
```
- Open Hue and notice if the file is created or not


## Task 5 - Create hive table to store forex rates from the HDFS
- Refer - 08-The Forex Data Pipeline\mnt\airflow\dags\forex_data_pipeline.py
  - creating_forex_rates_table
- Create hive server 2 thrift connection - hive_conn
  - Host: hive-server
  - Login: hive
  - Password: hive
  - Port: 10000
- Run the task
```
docker ps
docker exec -it <container-id> bash
cd /opt/airflow/dags/files
ls
pwd
airflow tasks test forex_data_pipeline creating_forex_rates_table 2021-01-01
```
- Notice the table is created in hive - <dns-name>:32762
- Select data from table in Hive:
```
Select * FROM forex_rates
# Nothing will be returned. We will insert data in next task
```

## Task 6 - Process Forex rates with Spark
- To process big data
- We will use Spark for that
- Refer - 08-The Forex Data Pipeline\mnt\airflow\dags\forex_data_pipeline.py
  - forex_processing
- Refer Spark script: airflow/dags/scripts/forex_processing.py
- Create the connection - spark_conn
  - Conn Type: Spark
  - Host: spark://spark-master
  - Port: 7077
- Run the task
```
docker ps
docker exec -it <container-id> bash
cd /opt/airflow/dags/files
ls
pwd
airflow tasks test forex_data_pipeline forex_processing 2021-01-01
```
Open Hue - <dns-name>:32762
- Select data from table in Hive
```
Select * FROM forex_rates
```

## Task 7 - Sending Email
- We need to create a token if we want to use gmail
  - Note 2fa should be active for this to work
  - Enable 2fa - https://myaccount.google.com/security
  - Create token using below URL:
    - https://security.google.com/settings/security/apppasswords
- Open - mnt/airflow/airflow.cfg
- Change SMTP settings
  - smtp.gmail.com
  - smtp_user: <your-email-address>
  - smtp_password: <token>
  - smtp_port: 587
  - smtp_mail_from: <your-email-address>
- Save and Close the file
- Restart airflow
```
./restart
```
- Open yopmail.com
  - Create an inbox
- Refer - 08-The Forex Data Pipeline\mnt\airflow\dags\forex_data_pipeline.py
  - send_email_notification
    - Change email address
- Run the task
```
docker ps
docker exec -it <container-id> bash
cd /opt/airflow/dags/files
ls
pwd
airflow tasks test forex_data_pipeline send_email_notification 2021-01-01
```
- Open yupmail.com and check for new mails


## Task 8 - Sending Slack Notification
- Create Slack account
- Create workspace in slack
- Create an app in Slack
  - api.slack.com/apps
    - Activate Incoming Webhooks
    - Click Add new Webhook to Workspace
  - Copy Webhook URL
- Refer - 08-The Forex Data Pipeline\mnt\airflow\dags\forex_data_pipeline.py
  - send_slack_notification
    - Specify workspace name
- Create slack connection - slack_conn
  - Conn_type: http
  - Host: Webhook URL

- Run the task
```
docker ps
docker exec -it <container-id> bash
cd /opt/airflow/dags/files
ls
pwd
airflow tasks test forex_data_pipeline send_slack_notification 2021-01-01
```
- Notice message in slack

## Add dependencies between tasks
- Refer - 08-The Forex Data Pipeline\mnt\airflow\dags\forex_data_pipeline.py


## Execute Pipeline
 - Refer - 08-The Forex Data Pipeline\mnt\airflow\dags\forex_data_pipeline.py
 - Clean exisiting artifacts
    - Remove file - forex_rates.json
    - Open Hue and drop table - Drop Table forex_rates
 - Run pipeline
    - Open Airflow UI
    - Enable pipeline
    - Trigger pipeline manually
 - Inspect the Hive table has data
