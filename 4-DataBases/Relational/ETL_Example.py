import pandas as pd
import sqlite3
import datetime

df = pd.read_csv('weather.csv')
""" df.head(2):
                STATION      DATE  PRCP  SNWD  ...  WSF2  WSF5  PGTM  FMTM
0     GHCND:USW00094728  20000101     0 -9999  ...    72    94  1337  1337
1     GHCND:USW00094728  20000102     0 -9999  ...    72   112  2313  2314
"""
""" print(df.columns)
Index(['STATION', 'DATE', 'PRCP', 'SNWD', 'SNOW', 'TMAX', 'TMIN', 'AWND', 'WDF2', 'WDF5', 'WSF2', 'WSF5', 'PGTM', 
      'FMTM'], dtype='object')
"""

# Connect to the DB
Conn = sqlite3.connect('weather.db', detect_types=sqlite3.PARSE_DECLTYPES)
c = Conn.cursor()

# Create table
c.execute('''
CREATE TABLE IF NOT EXISTS weather (
    day DATE,	    -- day of measurements
    min_temp FLOAT, -- min temperature in Fahrenheit
    max_temp FLOAT, -- max temperature in Fahrenheit
    snow INTEGETR   -- snow in inches
);
         ''')

c.execute('''CREATE INDEX IF NOT EXISTS weather_day ON weather(day);''')

# print(datetime.datetime.strptime(str(df['DATE'][1]), '%Y%m%d'))

weather_data = []
for i in range(len(df['DATE'])):
    weather_data.append((datetime.datetime.strptime(str(df['DATE'][i]), '%Y%m%d'), df['TMIN'][i], df['TMAX'][i],
                         df['SNOW'][i]))


c.executemany('INSERT INTO weather VALUES (?,?,?,?)', weather_data)

c.execute()


