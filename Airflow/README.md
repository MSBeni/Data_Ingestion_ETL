# Airflow README

## installation
First create a virtual environment and name it whatever you want.
Then activate the environment and run this command on your terminal to install airflow on your system. (I assume you are working on ubuntu which is pretty normal)
```bash
pip3 install apache-airflow==2.0.0 --constraint https://gist.githubusercontent.com/marclamberti/742efaef5b2d94f44666b0aec020be7c/raw/5da51f9fe99266562723fdfb3e11d3b6ac727711/constraint.txt
```
run this command for airflow matastore initialization and also creating files and folders needed by airflow. We just use this comamnd once.
```bash
airflow db init
```
Now if you check your system list using ```ls``` you will have a folder named airflow and you can check
it simply by typing ```cd airflow/```.

To run the airflow webserver just type this command on your terminal:
```bash
airflow webserver
```
If now you check your localhost at port 8080, you will be in the interface admin page.
Now to create a user to login to the admin page, you can use this command:
```bash
airflow users create -u admin -p admin -f MS -l Beni -r Admin -e admin@airflow.com
```
Now you have a user with username and password admin which has an Admin ROLE.
Note: By typing the help method you can find a good guidance how to do it:
```bash
airflow users create -h
```
you will this such result:
```
usage: airflow users create [-h] -e EMAIL -f FIRSTNAME -l LASTNAME
                            [-p PASSWORD] -r ROLE [--use-random-password] -u
                            USERNAME

Create a user

optional arguments:
  -h, --help            show this help message and exit
  -e EMAIL, --email EMAIL
                        Email of the user
  -f FIRSTNAME, --firstname FIRSTNAME
                        First name of the user
  -l LASTNAME, --lastname LASTNAME
                        Last name of the user
  -p PASSWORD, --password PASSWORD
                        Password of the user, required to create a user without --use-random-password
  -r ROLE, --role ROLE  Role of the user. Existing roles include Admin, User, Op, Viewer, and Public
  --use-random-password
                        Do not prompt for password. Use random string instead. Required to create a user without --password 
  -u USERNAME, --username USERNAME
                        Username of the user

examples:
To create an user with "Admin" role and username equals to "admin", run:

    $ airflow users create \
          --username admin \
          --firstname FIRST_NAME \
          --lastname LAST_NAME \
          --role Admin \
          --email admin@example.org

```
Then please run the command below to run the scheduler:
```bash
airflow scheduler
```

## Other useful commands:
- Start the Scheduler
```bash
airflow scheduler
```
- Start a Worker Node If you are in distributed mode (Celery)
```bash
airflow worker
```

- Print the List of Active DAGs
```bash
airflow list_dags
```
You can use ```airflow tasks list name_of_dag``` to check that every thing is good with your data pipeline. it should show all the necessary tasks.

- Print the List of Tasks of the dag_id
```bash
airflow list_tasks dag_id
```
Exemple:
```bash
airflow list_tasks hello_world
```

- Print the Hierarchy of Tasks in the dag_id
```bash
airflow list_tasks dag_id --tree
```
Exemple:
```bash
airflow list_tasks hello_world --tree
```

- Test your Tasks in your DAG
```bash
airflow test dag_id task_id execution_date
```
Exemple:
```bash
airflow test hello_world hello_task 2018-10-05
```