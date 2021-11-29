# Storing logs in AWS S3
- Can store and read logs in AWS S3
- By default Airflow stores its log files locally. It can result by eating up the disk space by Airflow logs
- Storing logs on S3 the logs can be stored without worrying about that
- Login to AWS Console
## Create S3 bucket
- Open S3 service and create bucket
  - Bucket Name: atin-airflow-logs
- Open the bucket created
- We need to create a new user with only the permission to read and write to that bucket
## Create IAM User
- Open IAM and Add User
  - Username: airflow-log-s3
  - Enable Programmatic Access
  - Permission: Create Policy
    - Service: s3
    - Action: Access Level -> List->ListBucket, Read->GetObject, Write->DeleteObject, PutObject, ReplicateObject, RestoreObject
    - Resources: Specific
      - Bucket: Add ARN and specify bucket name
      - Object: Add ARN and specify bucket name and object name - any
    - Click Review policy
    - Give name to policy: ReadWriteS3AirflowLogs
    - Click Create Policy
  - Now we are back to Permission page. Click Refresh
  - Search Policy: ReadWriteS3AirflowLogs
  - Click Next and then click Create User
  - Download .csv
  - Click Close
## Start Airflow
- Open terminal and start Airflow
```
./start.sh
docker ps
```
- Open Airflow UI
- Open Admin -> Connections
  - Conn Id: AirflowS3LogStorage
  - Connection Type: S3
  - Extra: {"aws_access_key_id": "", "aws_secret_access_key": ""}
  - Fill in the values above by taking from the user file we download earlier
  - Click Save
- Open IDE
- Open airflow.cfg
- Define Parameters
  - remote_logging = True
  - remote_log_conn_id = AirflowS3LogStorage
  - remote_base_log_folder = s3://atin-airflow-logs/airflow-logs
- Open AWS S3 Dashboard
- Open Bucket and notice it's empty
- Restart Airflow UI
```
./restart.sh
docker ps
docker logs -f <container-id-of-worker>
```
- We will later review the logs to notice the connections being made from the worker to AWS S3 to store the logs
- Open Airflow UI
- Enable logger_dag
- Refresh Page
- Open DAG -> Graph View -> t1 -> Log
- Notice the first line
- Open AWS S3
- Refresh bucket and notice new folder - airflow-logs
- Notice the file created in S3 Bucket. This log file has the same content as on the Airflow UI
- Reset the logging configuration in airflow.cfg
  - remote_logging = False
  - remote_log_conn_id =
  - remote_base_log_folder =
- Stop Airflow
```
./stop.sh
```
