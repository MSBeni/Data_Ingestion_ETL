# how to Use Sqoop to import data from MySQL to HFDS/Hive


After connecting to the mysql database, please make sure to give the necessary privileges to the user
want to import the data. It is important to redefine the username and password.
 
# Configure MYSQL
Before doing this we should set the mysql database in hadoop. To do so follow these steps:
```bash
su root

systemctl stop mysqld

systemctl set-environment MYSQLD_OPTS="--skip-grant-tables --skip-networking"

systemctl start mysqld

mysql -uroot
```
In the mysql database follow these steps:
```sql
FLUSH PRIVILEGES;

ALTER USER 'root'@'localhost' IDENTIFIED BY 'hadoop';

FLUSH PRIVILEGES;

QUIT;
```
Then in the terminal follow these steps:
```bash
systemctl unset-environment MYSQLD_OPTS

systemctl restart mysqld

exit
```
Now you can simply connect ot the database as the ```maria_dev``` user:
```bash

mysql -uroot -phadoop
```
in the database define the privilege for the maria_dev user to import expected data from mysql.
The total solution is as follows:
```sql
grant all privileges on mydb.* to myuser@'xxx.xxx.xxx.xxx' identified by 'mypassword';
```
In my example this was like this:
```sql
GRANT ALL PRIVILEGES ON movielens.* TO 'maria_dev'@'localhost' identified by 'maria_dev';
```

Then after quiting mysql, you can simply run this structure to import your data from MySQL to HFDS.
```bash
sqoop import --connect jdbc:mysql://<mysql-host>/test 
    --table test 
    --username <username> 
    --password <password> 
    --target-dir sqoop_test 
    -m 1 
    --driver com.mysql.jdbc.Driver
</password></username></mysql-host>
```

In my example this was like this:
```bash
sqoop import --connect jdbc:mysql://localhost/movielens --username maria_dev -password maria_dev --driver com.mysql.jdbc.Driver --table movies -m 1
```
