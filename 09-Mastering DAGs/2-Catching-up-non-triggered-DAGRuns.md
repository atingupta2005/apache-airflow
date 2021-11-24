# Catching up non triggered DAGRuns

- Refer backfill.py
- Refer that catchup parameter is set to true
- We can also change the catchup parameter in airflow.cfg
- Change date - 12-01-2019 00:30 AM
```
sudo date --set "12 Jan 2019 00:30:00"
```
- run - ./start.sh
- Open Airflow UI
- Turn on the toggle of DAG - backfill
- Notice that DAG is running multiple runs
