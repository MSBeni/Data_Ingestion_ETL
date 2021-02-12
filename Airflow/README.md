# Airflow README

## installation
First create a virtual environment and name it whatever you want.
Then activate the environment and run this command on your terminal to install airflow on your system. (I assume you are working on ubuntu which is pretty normal)
```bash
pip3 install apache-airflow==2.0.0 --constraint https://gist.githubusercontent.com/marclamberti/742efaef5b2d94f44666b0aec020be7c/raw/5da51f9fe99266562723fdfb3e11d3b6ac727711/constraint.txt
```
run this command for your database initialization.
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
