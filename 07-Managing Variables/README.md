# Managing Variables
- Variables are a generic way to store and retrieve arbitrary content or settings as a simple key value store within Airflow. Variables can be listed, created, updated and deleted from the UI (Admin -> Variables), code or CLI.

## Storing Variables in Environment Variables
- Airflow Variables can also be created and managed using Environment Variables. The environment variable naming convention is AIRFLOW_VAR_{VARIABLE_NAME}, all uppercase. So if your variable key is FOO then the variable name should be AIRFLOW_VAR_FOO.

- For example
```
export AIRFLOW_VAR_FOO=BAR

# To use JSON, store them as JSON strings
export AIRFLOW_VAR_FOO_BAZ='{"hello":"world"}'
```


- You can use them in your DAGs as:
```
from airflow.models import Variable

foo = Variable.get("foo")
foo_json = Variable.get("foo_baz", deserialize_json=True)
```
