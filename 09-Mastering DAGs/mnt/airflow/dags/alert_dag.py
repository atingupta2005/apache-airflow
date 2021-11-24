from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2019, 1, 1),
    'owner': 'Airflow',
    #'retries': 3,
    #'retry_delay': timedelta(seconds=60),
    #'emails': ['owner@test.com'],
    #'email_on_failure': True,
    #'email_on_retry': False,
    #'on_failure_callback': on_failure_task,
    #'on_success_callback': on_success_task,
    #'execution_timeout': timedelta(seconds=60),
    #'email': 'owner@test.com',
}


def on_success_task(dict):
    print("on_success_task")
    print(dict)

def on_failure_task(dict):
    print("on_failure_task")
    print(dict)

def on_success_dag(dict):
    print("on_success_dag")
    print(dict)

def on_failure_dag(dict):
    print("on_failure_dag")
    print(dict)

#with DAG(dag_id='alert_dag', schedule_interval="0 0 * * *", default_args=default_args, catchup=False, dagrun_timeout=timedelta(seconds=75), on_success_callback=on_success_dag, on_failure_callback=on_failure_dag) as dag:
with DAG(dag_id='alert_dag', schedule_interval="0 0 * * *", default_args=default_args, catchup=False) as dag:
    # Task 1
    t1 = BashOperator(task_id='t1', bash_command="sleep 30; echo 'first task after sleeping 30 sec'; exit 0")

    # Task 2
    t2 = BashOperator(task_id='t2', bash_command="echo 'second task'")

    t1 >> t2
