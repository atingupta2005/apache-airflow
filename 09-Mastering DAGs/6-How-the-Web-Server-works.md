# How the Web Server works
- Start Airflow
```
./stop.sh
./start.sh
```

- Review the logs and notice logs for the worker every 30 seconds:
```
docker logs -f airflow
```
- Refer 2 settings in airflow.cfg
  - worker_refresh_batch_size: How many workers to be refreshed at once
  - worker_refresh_interval: After how many seconds to refresh the workers
- Workers are refreshed due to parameter - worker_refresh_interval
- Notice parameter - logging_level. It is used to define how much logs should be captured. For debugging change the level
