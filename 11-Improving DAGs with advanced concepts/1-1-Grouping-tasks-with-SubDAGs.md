# Grouping tasks with SubDAGs and Deadlocks
- Refer - test_subdag.py and notice the operator - SubDagOperator
- Also refer to the factory method used. This factory method creates the SubDag
- We are passing the same object of default arguements to the SubDag. It's specially to have the same start date and end date for parent DAG and SubDag. It will avoid any unexpected behaviour
- Start Airflow UI
```
docker-compose -f docker-compose-CeleryExecutor.yml up -d
docker ps
```
- Open Airflow UI
- Enable test_subdag and refresh the page
- Click on the DAG in Airflow UI and open Graph View. Refer to the 2 tasks - subdag-1 and subdag-2
- Click on subdag-1 and zoom into subdag and open Graph View
- Open Gantt view and notice that tasks are executed in sequential
- We can enable parallal execution in subdags as well
- Open test_subdag.py and specify CeleryExecutor() instead of SequentialExecutor() for both subdags
- Open Airflow UI and open the DAG
- Then open Code and notice the changes are applied
- Click Trigger DAG and notice how tasks are now executed in subdag
