# Data Pipeline for Google Analytics Simulated data logs
This project aims to represent a simple data pipeline using the ETL techniques in order to simulated the logs saved from google analytics and create a data pipeline in order to transform and save the data in sqlite db and load the processed data which represents the number of visits of each unique ip each day.

# Test the code:
Please run these files each one with the mentioned priority:
- 1- fake_logFile.py
- 2- storing_logs.py
- 3- count_db_data.py

# check the sqlite database on your linux terminal
```bash
$ sqlite3
``` 
in the database bash then you can open the related dataset:
```bash
# .open db.sqlite
# SELECT * FROM logs;
```
 To quit the db, please type the following command or press ctrl + d
 ```bash
# .exit
```