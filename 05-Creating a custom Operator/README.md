# Creating a custom Operator
- Airflow allows you to create new operators to suit the requirements of you or your team
- The extensibility is one of the many reasons which makes Apache Airflow powerful.
- You can create any operator you want by extending the airflow.models.baseoperator.BaseOperator

- There are two methods that you need to override in a derived class:
  - Constructor - Define the parameters required for the operator. You only need to specify the arguments specific to your operator. You can specify the default_args in the dag file. See Default args for more details.
  - Execute - The code to execute when the runner calls the operator. The method contains the airflow context as a parameter that can be used to read config values.

- Let's implement an example HelloOperator in a new file hello_operator.py:
```  
from airflow.models.baseoperator import BaseOperator
class HelloOperator(BaseOperator):
      def __init__(self, name: str, **kwargs) -> None:
          super().__init__(**kwargs)
          self.name = name
      def execute(self, context):
          message = f"Hello {self.name}"
          print(message)
          return message
```

- You can now use the derived custom operator as follows:
```
from custom_operator.hello_operator import HelloOperator
with dag:
    hello_task = HelloOperator(task_id="sample-task", name="foo_bar")
```

- You also can keep using your plugins folder for storing your custom operators. If you have the file hello_operator.py within the plugins folder, you can import the operator as follows:
```
from hello_operator import HelloOperator
```

## Hooks
- Hooks act as an interface to communicate with the external shared resources in a DAG. For example, multiple tasks in a DAG can require access to a MySQL database. Instead of creating a connection per task, you can retrieve a connection from the hook and utilize it.
- Hook also helps to avoid storing connection auth parameters in a DAG.
- Let's extend our previous example to fetch name from MySQL:
```
class HelloDBOperator(BaseOperator):
    def __init__(self, name: str, mysql_conn_id: str, database: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name
        self.mysql_conn_id = mysql_conn_id
        self.database = database

    def execute(self, context):
        hook = MySqlHook(mysql_conn_id=self.mysql_conn_id, schema=self.database)
        sql = "select name from user"
        result = hook.get_first(sql)
        message = f"Hello {result['name']}"
        print(message)
        return message
```


- When the operator invokes the query on the hook object, a new connection gets created if it doesn't exist. The hook retrieves the auth parameters such as username and password from Airflow backend and passes the params to the airflow.hooks.base.BaseHook.get_connection(). You should create hook only in the execute method or any method which is called from execute. The constructor gets called whenever Airflow parses a DAG which happens frequently. And instantiating a hook there will result in many unnecessary database connections. The execute gets called only during a DAG run.


## User interface
- Airflow also allows the developer to control how the operator shows up in the DAG UI. Override ui_color to change the background color of the operator in UI. Override ui_fgcolor to change the color of the label.

```
class HelloOperator(BaseOperator):
    ui_color = "#ff0000"
    ui_fgcolor = "#000000"
    # ...
```

## Templating
- You can use Jinja templates to parameterize your operator. Airflow considers the field names present in template_fields for templating while rendering the operator.
```
class HelloOperator(BaseOperator):

    template_fields = ["name"]

    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name

    def execute(self, context):
        message = f"Hello from {self.name}"
        print(message)
        return message
```

- You can use the template as follows:
```
with dag:
    hello_task = HelloOperator(
        task_id="task_id_1", dag=dag, name="{{ task_instance.task_id }}"
    )
```

## Sensors
- Airflow provides a primitive for a special kind of operator, whose purpose is to poll some state (e.g. presence of a file) on a regular interval until a success criteria is met.
- You can create any sensor your want by extending the airflow.sensors.base.BaseSensorOperator defining a poke method to poll your external state and evaluate the success criteria.
- Sensors have a powerful feature called 'reschedule' mode which allows the sensor to task to be rescheduled, rather than blocking a worker slot between pokes. This is useful when you can tolerate a longer poll interval and expect to be polling for a long time.
