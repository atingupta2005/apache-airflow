# Rotating Fernet Key
- For security we should keep changing the fernet keys
- Connect to the web server
```
docker ps
docker exec -it <container-id-of-web-server> bash
```
- Run command
```
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```
- Copy new key and put in airflow.cfg
```
vi mnt/airflow/airflow.cfg
```

```
fernet_key = <new-key>,<old-key>
```
- In docker container run command
```
docker ps
docker exec -it <container-id-of-web-server> bash
```

```
airflow rotate_fernet_key
exit
```

- Exit from container and connect to postgres database
```
docker ps
docker exec -it <container-id-of-postgres> psql -d airflow -U airflow
```
- Query data from connection table
```
SELECT login, password, extra FROM connection WHERE conn_id='my_conn';
```
- Notice that this encrypted password is different from the old one
- Since encryption using new key is in place and rotation is done well
- Now let's remove old fernet key from airflow.cfg and restart web server
```
vi mnt/airflow/airflow.cfg
```
```
fernet_key = <new-key>
```
- Restart web server
```
docker-compose -f docker-compose-CeleryExecutor.yml restart webserver
```
- In fact we should save fernet key in environment variables for security
- Open airflow.cfg and cut the fernet key
```
vi mnt/airflow/airflow.cfg
```
- Open docker-compose-CeleryExecutor.yml
```
vi docker-compose-CeleryExecutor.yml
```
  ```
  environment:
    - AIRFLOW__CORE__FERNET_KEY=<paste-fernet-key-here>
  ```
- Copy this environment variable and paste it in each component of Airflow
- Save file and restart docker container
```
./restart.sh
docker ps
```
- Connect to web webserver
```
docker exec -it <container-id-of-web-server> bash
```
- Inspect environment variable
```
env
```

- Notice fernet key is there
