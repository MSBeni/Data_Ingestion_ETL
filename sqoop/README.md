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
Then in the 

systemctl unset-environment MYSQLD_OPTS

systemctl restart mysqld

GRANT ALL PRIVILEGES ON movielens.* TO 'maria_dev'@'localhost' identified by 'maria_dev';

sqoop import --connect jdbc:mysql://localhost/movielens --username maria_dev -password maria_dev --driver com.mysql.jdbc.Driver --table movies -m 1