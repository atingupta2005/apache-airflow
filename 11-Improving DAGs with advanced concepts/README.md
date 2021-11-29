# Improving DAGs with advanced concepts


# Improving DAGs with advanced concepts

<span style="color:#24292F">Minimising Repetitive Patterns With</span>  <span style="color:#24292F">SubDAGs</span>

<span style="color:#24292F">Grouping tasks with</span>  <span style="color:#24292F">SubDAGs</span>  <span style="color:#24292F">and Deadlocks</span>

<span style="color:#24292F">Making different paths in DAGs with Branching</span>

<span style="color:#24292F">Make First Conditional Task Using Branching</span>

<span style="color:#24292F">Trigger rules for tasks</span>

<span style="color:#24292F">Changing how tasks are triggered</span>

<span style="color:#24292F">Avoid hard coding values with Variables\, Macros and Templates</span>

<span style="color:#24292F">Templating tasks</span>

<span style="color:#24292F">How to share data between tasks with XCOMs?</span>

<span style="color:#24292F">Sharing \(big?\) data with XCOMs</span>

<span style="color:#24292F">Trigger</span>  <span style="color:#24292F">DagRunOperator</span>  <span style="color:#24292F">or when DAG controls another DAG</span>

<span style="color:#24292F">Trigger a DAG from another DAG</span>

<span style="color:#24292F">Dependencies between DAGs with the</span>  <span style="color:#24292F">ExternalTaskSensor</span>

<span style="color:#24292F">Make DAGs dependent with the</span>  <span style="color:#24292F">ExternalTaskSensor</span>

# An Overview

SubDags: pros and troubles

Exchanging data withXComs

Different paths with Branching

Dynamic DAGs with Templates\, Macros and Variables

Customizing the trigger rules of your tasks

And more …\.

# Minimising Repetitive Patterns With SubDAGs

How to make yourdagscleaner

# USE Case

![](img/11-Improving%20DAGs%20with%20advanced%20concepts1.png)

# Use Case

WithSubDags:

Tasks are grouped into the two boxes with bold borders\.

![](img/11-Improving%20DAGs%20with%20advanced%20concepts2.png)

# How to create SubDAG?

![](img/11-Improving%20DAGs%20with%20advanced%20concepts3.png)

# Important Notes

The main DAG manages all thesubDAGsas normal tasks\.

Airflow UI only shows the main DAG\.

SubDagsmust be scheduled the same as their parent DAG\.

UseSubDagswith caution

# Making different paths in your DAGs with Branching

Choose the right path

# Use Case

LET'S start from a use case\.\.\.

![](img/11-Improving%20DAGs%20with%20advanced%20concepts4.png)

# Definition

Branching is the mechanism allowing your DAG to choose between different paths according to the result of a specific task =BranchPythonOperator\.

# How Does It Work?

![](img/11-Improving%20DAGs%20with%20advanced%20concepts5.png)

# Depends_on_past and Branching

You can usedepends\_on\_pastwith branching in your tasks

![](img/11-Improving%20DAGs%20with%20advanced%20concepts6.png)

# Important Notes

![](img/11-Improving%20DAGs%20with%20advanced%20concepts7.png)
