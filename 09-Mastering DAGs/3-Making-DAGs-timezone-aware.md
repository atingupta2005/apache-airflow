# Making DAGs timezone aware
- Manipulate dates and time zone of dags and make then timezone aware

- Refer - tz_dag.py
  - Notice state_date and schedule_interval
    - schedule_interval works based on the timezone which is specified in airflow.cfg. So it would be UTC in case it's UTC in airflow.cfg
  - Notice the print statements which print the date/time to understand when DAG tasks ran

- Set timezone to Europe/Amsterdam (UTC+1)
```
date
timedatectl
sudo timedatectl set-timezone Europe/Amsterdam
timedatectl
date
```

- Change the date/time of computer
```
sudo date --set "30 Mar 2019 02:15:00"    # 2:15 Local Time and 1:15 in UTC
```
- Uncomment the print statements from tz_dag.py
- Start - sh start.sh
- Open Airflow UI
- Turn on tz_dag
- Refresh page after 1 min and notice the dates of execution
- Check logs on terminal
```
docker logs -f airflow
```
- Notice the output of DAG run
- If we want to execute our next DAG run then change date to 31-03-2019 after 1 AM UTC
- Before changing the date, let's understand about Daylight Saving time (DST)
  - This time - 31-03-2019 after 1 AM UTC corresponds to when the Daylight Saving Time happens in Europe.
    - At 2 AM it will be 3 AM local time. The time zone will shift from UTC+1 to UTC+2
- Now change the date/time to 31-03-2019 1:59 AM (UTC+1) - this is just before DST will happen
```
timedatectl
sudo date --set "31 Mar 2019 01:59:00"
timedatectl
```
- Now wait and refresh the Airflow UI page, nothing should be executed as expected
- Wait for 1 minute so that DST can happen
- Also notice the local time is changed to 3 AM - 2 hours difference (UTC+2) instead of 1 hour difference
- Also notice that DAG is triggered
- Now let's understand the problem
  - Change the date to 01-04-2019 at 2 AM (UTC+1) local time. This is the time when we expect our DAG to be triggered.
  - Refresh Airflow UI page after 1 min. DAG will still not be executed
  - Why? Because our DAG is configured in UTC in tf_dag.py. Notice value schedule_interval which specified that DAG should be run every day at 1 AM in UTC. As we are now in UTC+2 due to DST, the DAG now would not be triggered at 2 AM local time but at 3 AM.
- This can be a problem as we don't want to see our DAG being run 1 hour later just because of time zone has changed
- If we want our DAGs to be run at 2 AM, it should still be the case even after the DST
- How to fix?
  - You need to specify the time zone in which your DAG works
  - To do this we can use Python library - Pendulum, to get the timezone that we want
    - We specify the time zone in the start_date of the DAG - tzinfo=local_tz
    - We also change the start_date from 1 AM to 2 AM.
    ```
    'start_date': datetime(2019, 3, 29, 2, tzinfo=local_tz),
    ```
    - Since we are now setting our DAG in local time, we change the schedule_interval to indicate that DAG must be triggered everyday at 2 AM local time.
    ```
    with DAG(dag_id='tz_dag', schedule_interval="0 2 * * *", default_args=default_args) as dag:
    ```
  - Save the file and move back to the terminal
  - Run - stop.sh
  - Change the date back to 30-03-2019 2:15 AM
  ```
  sudo date --set "30 Mar 2019 02:15:00"    # 2:15 Local Time and 1:15 in UTC
  ```
  - Start docker container - start.sh
  - Open Airflow UI and enable the dag - tz_dag
  - wait for 1 min and refresh the page
  - Notice that DAG is executed as expected
