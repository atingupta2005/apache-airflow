# Hiding variables
- Open airflow.cfg and notice hide_sensitive_variable_fields

- We can use some special variable names to hide the values
- Open Airflow UI and create a new variable
  - Name: my_password
  - Value: TopSecretValue
- Notice the value is not visible in view
- This is because Airflow automatically hide the value if variable name is any one of:
  - password
  - secret
  - passwd
  - authorization
  - api_key
  - apikey
  - access_token
