# Encrypting sensitive data with Fernet
- Start Airflow
```
./start.sh
```

- Create a connection on Airflow UI - Admin -> Connection -> Create
  - Conn Id: my_conn
  - Type: HTTP
  - Login: my_login
  - Password: my_password
  - Extra: {"access_key": "my_key", "secret_key": "my_secret"}
- Save connection
- Connect to docker container - postgres
```
docker ps
docker exec -it <container-id-postgres> psql -d airflow -U airflow
```
- Check tables
```
\dt
```

- Show the columns of table connection
```
\d connection
```

- Query data from connection table
```
SELECT login, password, extra FROM connection WHERE conn_id='my_conn';
\q
```
- Notice password is stored in plain text
- We need to encrypt the secret values
- First we need to install crypto. For this update Dockerfile to specify the crypto package
```
vi docker/airflow/Dockerfile
```
```
&& pip install apache-airflow[crypto,celery,postgres,ssh${AIRFLOW_DEPS:+,}${AIRFLOW_DEPS}]==${AIRFLOW_VERSION} --constraint /requirements-python3.7.txt \
```
- Now restart docker container and image will be rebuilt
```
./restart.sh
```

- Let's define fernet key used to encrypt sensitive data
- Open airflow.cfg and look for fernet_key
```
cat mnt/airflow/airflow.cfg | grep fernet
```
- Fernet is a symmatric encryption method to make sure the encrypted value can not be read without fernet key
-  Let's generate fetnet key
```
docker ps
docker exec -it <container-id-of-web-server> bash
```
- Run command
```
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```
- Copy the key generated and paste it in airflow.cfg
vi mnt/airflow/airflow.cfg
- Exit container and restart web server
```
exit
```
```
docker-compose -f docker-compose-CeleryExecutor.yml restart webserver
docker ps
```
- Edit the connection - my_conn, so that it can now be encrypted
- Connect to postgres
```
docker exec -it <container-id-of-postgres> psql -d airflow -U airflow
```
- Query data from connection table
```
SELECT login, password, extra FROM connection WHERE conn_id='my_conn';
```
- Notice values are now encrypted
