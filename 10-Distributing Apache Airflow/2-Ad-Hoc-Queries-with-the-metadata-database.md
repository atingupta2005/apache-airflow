# Ad Hoc Queries with the metadata database
- Refer:
  - docker-compose-LocalExecutor.yml
  - Dockerfile
    - Based on Python 3.7
    - ARG: Are used when Docker image is built
    - Env Variables: Accessible from Docker container
    - Expose: To expose the ports

  - entrypoint.sh: Is executed when container starts. Has environment variables that will be defined inside the docker container running Airflow as well as the default value. So if the default value is not set from docker-compose file, then default value will be used.
    - export: The environment variables defined to modify the configuration of Airflow.
    - Refer - AIRFLOW__CORE__SQL_ALCHEMY_CONN
    - Refer - AIRFLOW__CELERY__RESULT_BACKEND
  - airflow.cfg
    - sql_alchemy_conn
      - Will be overwritten by AIRFLOW__CORE__SQL_ALCHEMY_CONN as specified in the env variable in entrypoint.sh
  - Run
  ```
  ls
  docker-compose -f docker-compose-LocalExecutor.yml up -d
  docker ps  
  ```
  - Open Airflow UI
  - Create connection - Admin\Connections
    - Conn Id: postgres_1
    - Conn Type: postgres
    - Host: postgres
    - Schema: airflow
    - Login: airflow
    - Password: airflow
    - Port: 5432
  - Turn on parallel_dag
  - Click on Data Profiling -> Add Hoc Query
  - Select the connection we created
  - Run below queries one by one:
    - List the Airflow tables in PostgreSQL
    ```
    SELECT * FROM
    pg_catalog.pg_tables
    WHERE
    schemaname != 'pg_catalog'
    AND schemaname != 'information_schema'
    AND tableowner = 'airflow';
    ```
    - List the task instances
    ```
    SELECT * FROM task_instance;
    ```
    - List the dag runs
    ```
    SELECT * FROM dag_run;
    ```


- Now as we see that anyone having access to Airflow UI can access our data. Its not a very secure thing. We can turn this feature off
- Modify airflow.cfg - secure_mode = True
- Restart
```
docker-compose -f docker-compose-LocalExecutor.yml down
docker-compose -f docker-compose-LocalExecutor.yml up -d
```
- Now Data Profiling -> Add Hoc Query is not available
