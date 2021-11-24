# Organizing your DAGs folder
- Refer: packaged_dag.py
- Create a new folder named - functions in the folder - dags
- Create a new python file in it - helpers.py
- Move the 3 functions from packaged_dag.py to helpers.py
- Create a new blank file name __init__.py in functions
- Now in file - packaged_dag.py, import from package - functions
```
from functions.helpers import  first_task, second_task, third_task
```
- Open terminal
- Package code into zip file
```
cd mnt/airflow/dags
ls
zip -rm packaged_dag.zip packaged_dag.py functions/
ls
```

- Move to the last directory
```
cd -
./stop.sh
./start.sh
```

- Open Airflow UI and notice that packaged_dag is successfully loaded

## DagBag
- Check web server logs on terminal
```
docker logs -f airflow
```

- Check the logs - "Filling Up the DagBag" - every 30 seconds
- Can change the interval from airflow.cfg

```
./stop.sh
```

- Edit add_dagbags.py
```
vi mnt/airflow/dags/add_dagbags.py
```
- It has the paths of DagBags
- Uncomment and save it
- Notice that there are DAG file in below 2 folders which will now be scanned by Airflow due to DagBag
```
mnt\airflow\project_a\
mnt\airflow\project_b\
```

- Start Airflow
```
./start.sh
```
- Check web server logs on terminal
```
docker logs -f airflow
```

- Open airflow UI
- Notice that both the DAGs are now available
- Note that there must be no errors in our DAG files, else they will not be shown on UI
- Now if we make an error on one of the DAGs then that DAG will not be available
