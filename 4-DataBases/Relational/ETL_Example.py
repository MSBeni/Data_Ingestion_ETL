import pandas as pd
import sqlite3 as sql

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
Conn = sql.connect('wether.db')
