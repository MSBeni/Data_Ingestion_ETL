import sqlite3
import pandas as pd

conn = sqlite3.connect('weather.db')

c = conn.cursor()

# # Do this instead
t = (156.0,)
# c.execute('SELECT * FROM weather WHERE min_temp=?', t)
# c.execute('SELECT max_temp FROM weather')
print(c.fetchone())

# Defining Parameters
params = {
    'temp_max': 156.0,
}
# Query to read the distance form the table where the vendor condition applies
sql = 'SELECT max_temp FROM weather'
# sql = 'SELECT max_temp FROM weather WHERE max_temp = :temp_max'

# Reading all the data in Database with specific distance
datb = pd.read_sql(sql, conn, params=params)

print(datb)