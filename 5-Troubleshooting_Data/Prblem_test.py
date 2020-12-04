import sqlite3
import pandas as pd
from datetime import datetime

conn = sqlite3.connect('rides.db', detect_types=sqlite3.PARSE_DECLTYPES)
cur = conn.cursor()

dfB = pd.read_sql('SELECT * FROM rides', conn)
''' print(dfB.columns)
Index(['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime',
       'passenger_count', 'trip_distance', 'RatecodeID', 'store_and_fwd_flag',
       'PULocationID', 'DOLocationID', 'payment_type', 'fare_amount', 'extra',
       'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge',
       'total_amount'],
      dtype='object')
'''
dfB['duration'] = 0
for i in range(len(dfB['tpep_dropoff_datetime'])):
    dfB['duration'][i] = (datetime.strptime(str(dfB['tpep_dropoff_datetime'][i]), '%Y-%m-%d %H:%M:%S') - \
                      datetime.strptime(str(dfB['tpep_pickup_datetime'][i]), '%Y-%m-%d %H:%M:%S')).total_seconds()

# print(dfB['duration'][2].total_seconds())
BigDurations = dfB['duration'] > 18000

fill_value = dfB['duration'].median()
print(fill_value)

dfB.loc[BigDurations, 'duration'] = fill_value
print(dfB['duration'].max())

