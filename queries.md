- Share Docker and Kubernetes
  - https://github.com/atingupta2005/Docker-Kubernetes-AWS-LnT-Aug-2020
  -

- Webhook trigger
  - https://airflow.apache.org/docs/apache-airflow/2.0.0/stable-rest-api-ref.html#section/Overview/Versioning-and-Endpoint-Lifecycle
```
function triggerDag(dagId, dagParameters){
    var urlEncodedParameters = encodeURIComponent(dagParameters);
    var dagRunUrl = "http://airflow:8080/admin/rest_api/api/v1.0/trigger_dag?dag_id="+dagId+"&conf="+urlEncodedParameters;
    $.ajax({
        url: dagRunUrl,
        dataType: "json",
        success: function(msg) {
            console.log('Successfully started the dag');
        },
        error: function(e){
           console.log('Failed to start the dag');
        }
    });
}
```

- Dependency on 2 different DAGs which are running in different installation - One dag should run only if another DAG is created.

- Why there is attribute channel in SlackWebhookOperator

- Best practices of Airflow as an Architect to do Performance Tuning and best way to architect the cluster.
  - https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
  - https://livebook.manning.com/book/data-pipelines-with-apache-airflow/chapter-10/v-4/83
  - https://medium.com/swlh/airflow-dag-best-practices-716ac95b82d1
  - Apache Airflow Tips and Best Practices: https://towardsdatascience.com/apache-airflow-tips-and-best-practices-ff64ce92ef8

- Documentation link for Airflow installation on various sources
  - https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html

- Airflow with Azure Devops

- Airflow version upgrade
  - Why upgrade: https://www.nextlytics.com/blog/apache-airflow-why-the-upgrade-is-worth-it
  - Strategy: https://slack.engineering/reliably-upgrading-apache-airflow-at-slacks-scale/
  - Steps: https://airflow.apache.org/docs/apache-airflow/stable/upgrading-from-1-1- 0/index.html

- Clean Up Activities
  - https://github.com/teamclairvoyant/airflow-maintenance-dags
  - https://blog.clairvoyantsoft.com/automated-maintenance-for-apache-airflow-8d844f32737d
