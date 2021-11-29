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
- We can enable parallal executing in subdags as well
- Open test_subdag.py and specify CeleryExecutor() instead of SequentialExecutor() for both subdags
- Open Airflow UI and open the DAG
- Then open Code and notice the changes are applied
- Click Trigger DAG and notice how tasks are now executed in subdag

## Deadlocks
- Open the parent DAG in Airflow UI
- Open Tree view and notice that a SubDag is depicted as a tesk in parent DAG and not as a graph of tasks. Due to this deadlocks might happen
- A subdag is an abstraction of tasks but it still behaves as a task. Let's see an example of deadlock
- Disable the DAG - test_subdag
- Enable the DAG - deadlock_subdag
- Open DAG and start refreshing the page
- Even after 15 minutes, subdags will still be in running state. So why the SubDags are stuck in running state?
- With the current configuration of Airflow, upto 4 tasks can be executed in parallel as the paramer parallelism is set to 4
- If we check graph view we can see that we have 4 SubDags that can be executed in parallel where each contains 5 tasks that also can be executed in parallel as the SubDagOperators are set with the CeleryExecutor.
- A subdag is depicted as a task and so all tasks in the subdag must succeed in order to get the subdag marked as succeed as well
- So it means that a subdag takes one worker slot until all the child tasks are executed
- Since we have 4 subdags and upto 4 worker slots are available to be taken in parallel, the SubDags are all waiting to finish executing their tasks but there is no slot anymore for running them
- Its a deadlock - No tasks of any subdags can be executed since all subdag instances have taken all the available slots
- How to solve?
  - Add a queue from the SubDagOperators so that they will be executed into this dedicated queue and will not take the place of the child tasks. Then we will create a new worker node and assign that queue to it
  - You can do it as an exersice
- Stop Airflow
```
docker-compose -f docker-compose-CeleryExecutor.yml down
docker ps
```
