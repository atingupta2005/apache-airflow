# Manipulating start_date
- Open mnt/dags/start_and_schedule_dag.py
- Notice start date of dag
- Notice schedule_interval which is set to run every hour
- Run - start.sh
- Run - stop.sh
- Set date just before the start date - 20-03-2019 1:00 AM
```
sudo date --set "20 Mar 2019 01:00:00"
```
- Run - start.sh
- Open Airflow UI
- Enable dag - start_and_schedule_dag
- Notice DAG will not run as our start date of dag is in future
- Increase system date - 29-03-2019 00:00 AM
```
sudo date --set "29 Mar 2019 00:00:00"
```
- Refresh UI and wait
- DAG should not start as well now

- Now only change the current time from 00:00 AM to 02:00 AM
  - Since DAG starts at 1 AM in UTC, we add the schedule_interval which gives 2 AM in UTC
  ```
  sudo date --set "29 Mar 2019 02:00:00"
  ```
- Refresh UI after 1 min
- Now DAG will run. Notice the Execution dates
- Next Dag run will trigger at 3 AM UTC
- Change the time to 3 AM UTC
```
sudo date --set "29 Mar 2019 03:00:00"
```
- Refresh page after 1 min
- Second DAG Run will now be executed
- We can also use Timedelta instead of Cron. Change DAG code
```
schedule_interval=timedelta(hours=1)
```
- Change date to 4 AM
```
sudo date --set "29 Mar 2019 04:00:00"
```
- Wait and Refresh page
- We should get the next DAG run triggerred
