# Managing Connections
- Airflow needs to know how to connect to your environment. Information such as hostname, port, login and passwords to other systems and services is handled in the Admin->Connections section of the UI. The pipeline code you will author will reference the 'conn_id' of the Connection objects.

- Connections can be created and managed using either the UI or environment variables.

## Creating a Connection with the UI
- Open the Admin->Connections section of the UI. Click the Create link to create a new connection.
  - Fill in the Connection Id field with the desired connection ID. It is recommended that you use lower-case characters and separate words with underscores.
  - Choose the connection type with the Connection Type field.
  - Fill in the remaining fields. See Encoding arbitrary JSON for a description of the fields belonging to the different connection types.
  - Click the Save button to create the connection


## Editing a Connection with the UI
- Open the Admin->Connections section of the UI. Click the pencil icon next to the connection you wish to edit in the connection list.
- Modify the connection properties and click the Save button to save your changes

## Creating a Connection from the CLI
- You may add a connection to the database from the CLI.
- Obtain the URI for your connection
- Then add connection like so:
```
airflow connections add 'my_prod_db' \
    --conn-uri 'my-conn-type://login:password@host:port/schema?param1=val1&param2=val2'
```

- Alternatively you may specify each parameter individually:
```
airflow connections add 'my_prod_db' \
    --conn-type 'my-conn-type' \
    --conn-login 'login' \
    --conn-password 'password' \
    --conn-host 'host' \
    --conn-port 'port' \
    --conn-schema 'schema' \
    ...
```

## Exporting Connections from the CLI
- You may export connections from the database using the CLI. The supported formats are json, yaml and env.
- You may mention the target file as the parameter:
```
airflow connections export connections.json
```
- Alternatively you may specify format parameter for overriding the format:
```
airflow connections export /tmp/connections --format yaml
```

- You may also specify - for STDOUT:
```
airflow connections export -
```

- The JSON format contains an object where the key contains the connection ID and the value contains the definition of the connection. In this format, the connection is defined as a JSON object. The following is a sample JSON file.
```
{
  "airflow_db": {
    "conn_type": "mysql",
    "host": "mysql",
    "login": "root",
    "password": "plainpassword",
    "schema": "airflow",
    "port": null,
    "extra": null
  },
  "druid_broker_default": {
    "conn_type": "druid",
    "host": "druid-broker",
    "login": null,
    "password": null,
    "schema": null,
    "port": 8082,
    "extra": "{\"endpoint\": \"druid/v2/sql\"}"
  }
}
```

- The YAML file structure is similar to that of a JSON. The key-value pair of connection ID and the definitions of one or more connections. In this format, the connection is defined as a YAML object. The following is a sample YAML file.
```
airflow_db:
  conn_type: mysql
  extra: null
  host: mysql
  login: root
  password: plainpassword
  port: null
  schema: airflow
druid_broker_default:
  conn_type: druid
  extra: '{"endpoint": "druid/v2/sql"}'
  host: druid-broker
  login: null
  password: null
  port: 8082
  schema: null
```

You may also export connections in .env format. The key is the connection ID, and the value describes the connection using the URI
```
airflow connections export /tmp/connections --format env
```

The following is a sample ENV file.
```
airflow_db=mysql://root:plainpassword@mysql/airflow
druid_broker_default=druid://druid-broker:8082?endpoint=druid%2Fv2%2Fsql
```

## Connection URI format
- In general, Airflow's URI format is like so:
```
my-conn-type://my-login:my-password@my-host:5432/my-schema?param1=val1&param2=val2
```

- The above URI would produce a Connection object equivalent to the following:
```
Connection(
    conn_id="",
    conn_type="my_conn_type",
    description=None,
    login="my-login",
    password="my-password",
    host="my-host",
    port=5432,
    schema="my-schema",
    extra=json.dumps(dict(param1="val1", param2="val2")),
)
```

- Additionally, if you have created a connection, you can use airflow connections get command.
```
airflow connections get my_prod_db
```


## Securing Connections
- Airflow uses Fernet to encrypt passwords in the connection configurations stored the metastore database. It guarantees that without the encryption password, Connection Passwords cannot be manipulated or read without the key
