import sqlite3
import pandas as pd

conn = sqlite3.connect('weather.db')

c = conn.cursor()

# # Do this instead
t = (200.0,)
c.execute('SELECT * FROM weather WHERE max_temp=?', t)
print(c.fetchone())


# dbf = pd.read_sql('weather.db', )

# df = pd.read_csv('weather.csv')
# print(df['TMAX'])
#
#
# # Defining Parameters
# params = {
#     'temp_max': float(170),
# }
# # Query to read the distance form the table where the vendor condition applies
# sql = 'SELECT max_temp FROM weather'
#
# # Reading all the data in Database with specific distance
# datb = pd.read_sql(sql, conn, params=params)
#
# print(datb)