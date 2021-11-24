# Set up the Airflow cluster with Celery Executors
- Refer - docker-compose-CeleryExecutor.yml
  - Redis service
    - The message broker system required by Celery from which the worker node will pull out the tasks to execute
    - We can also use another message broker if we want. We just need to change the Docker image of this service
  - postgres service
    - We can uncomment the lines to persist the data of CeleryExecutor. Currently we don't want to persist
  - Webserver service
    - Look at environment variables
      - FERNET_KEY - to encrypt the connection so that our passwords are secure
      - EXECUTOR
    - Volumes
  - flower service
    - Tool for monitoring Celery tasks and workers
    - It is a web based application and allows us to see task progress, details and worker status
    - We can start it using the command - airflow flower
  - scheduler service
    - The volumes of scheduler service and webservice service must match
  - worker service
    - Here the Celery processes will be created in order to execute the tasks pulled from the queues in a controlled way
- Start
```
#There should be no existing containers
docker ps
docker rm <container id>
docker-compose -f docker-compose-CeleryExecutor.yml up -d
docker ps
```

- Open Web Browser
- Open localhost:8080
- Open localhost:5555 in new tab
  - It should show 1 worker with the status Online
- To check if there are any errors in Airflow, check by
```
docker logs -f 10-distributingapacheairflow_worker_1
```
