# Set up a Database Backend
- Choosing database backend
- Database URI
- Setting up a SQLite Database
- Setting up a MySQL Database
- Setting up a PostgreSQL Database
- Initialize the database

## Choosing database backend
- By default, Airflow uses SQLite, which is intended for development purposes only
- You should consider setting up a database backend to MySQL, PostgresSQL , MsSQL

- Airflow supports the following database engine versions, so make sure which version you have.
  - PostgreSQL: 9.6, 10, 11, 12, 13
  - MySQL: 5.7, 8
  - MsSQL: 2017, 2019
  - SQLite: 3.15.0+

## Database URI
- Airflow uses SQLAlchemy to connect to the database, which requires you to configure the Database URL
- You can do this in option sql_alchemy_conn in section [core]

- If you want to check the current value, you can use airflow config get-value core sql_alchemy_conn command as in the example below.
```
airflow config get-value core sql_alchemy_conn
```

## Setting up a SQLite Database
- SQLite database can be used to run Airflow for development purpose as it does not require any database server
- There are a few limitations of using the SQLite database
- It should NEVER be used for production.

- An example URI for the sqlite database:
```
sqlite:////home/airflow/airflow.db
```

## Setting up a MySQL Database
- You need to create a database and a database user that Airflow will use to access this database
- In the example below, a database airflow_db and user with username airflow_user with password airflow_pass will be created
```
CREATE DATABASE airflow_db CHARACTER SET utf8 COLLATE utf8mb4_unicode_ci;
CREATE USER 'airflow_user' IDENTIFIED BY 'airflow_pass';
GRANT ALL PRIVILEGES ON airflow_db.* TO 'airflow_user';
```

- An example URI
```
mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
```

## Setting up a PostgreSQL Database
- You need to create a database and a database user that Airflow will use to access this database
- In the example below, a database airflow_db and user with username airflow_user with password airflow_pass will be created
```
CREATE DATABASE airflow_db;
CREATE USER airflow_user WITH PASSWORD 'airflow_pass';
GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflow_user;
```

- An example URI
```
postgresql+psycopg2://<user>:<password>@<host>/<db>
```

## Initialize the database
- After configuring the database and connecting to it in Airflow configuration, you should create the database schema.
```
airflow db init
```
