# Templating tasks
- Refer template_dag.py
- Only some parameters are templated in Operators
- Refer to the task t0. Notice the templating using in the Operator. ds is predefined variable
- Start Airflow
```
docker-compose -f docker-compose-CeleryExecutor.yml up -d
docker ps
```
- Open Airflow UI
- Enable template_dag
- Trigger DAG
- Refresh the page
- Open DAG -> Graph View
- Open task t0 and view the logs
- Notice that date is printed in the logs

## Create variable
- Open Airflow UI -> Admin -> Variables
- Create variable named - CASSANDRA_LOGIN
- Open template_dag.py and specify new variable name - var.value.CASSANDRA_LOGIN instead of ds
```
bash_command="echo {{ ds }}"
#bash_command="echo {{ var.value.CASSANDRA_LOGIN }}"
#bash_command="echo {{ts_nodash}} - {{ macros.ds_format(ts_nodash, '%Y%m%dT%H%M%S', '%Y-%m-%d-%H-%M') }}"
)
```
- Run DAG again and notice that value is printed in the logs

## Use macro
- Update dag code
```
macros.ds_format(ts_nodash, '%Y%m%dT%H%M%S', '%Y-%m-%d-%H-%M')
```
- Trigger DAG again
- View the logs
