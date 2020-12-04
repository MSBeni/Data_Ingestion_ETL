import pandas as pd
import sqlite3
from datetime import datetime
import logging
import csv

# df = pd.read_csv('weather.csv')
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
# Conn = sqlite3.connect('weather.db', detect_types=sqlite3.PARSE_DECLTYPES)
# c = Conn.cursor()

def parse_day(text):
    return datetime.strptime(str(text), '%Y%m%d')


def parse_temp(text):
    celsius = float(text) * 10
    return (celsius * 9/5) + 32


converts = [
    ('DATE', 'day', parse_day),
    ('TMIN', 'min_temp', parse_temp),
    ('TMAX', 'max_temp', parse_temp),
    ('SNOW', 'snow', int),
]


def row2db(row):
    obj = {}
    for src, dest, conv in converts:
        try:
            obj[dest] = conv(row[src])
        except ValueError:
            return None
    return obj


def iter_records(df):
    name_ = df
    with open(df) as bp:
        for lnum, row in enumerate(csv.DictReader(bp), 2):
            # print(row)
            obj = row2db(row)
            if not obj:
                logging.warning('%s:%d skipping bad row', name_, lnum)
                continue
            yield obj
#
# iter_records('weather.csv')

schema_sql = '''
CREATE TABLE IF NOT EXISTS weather (
    day DATE,	    -- day of measurements
    min_temp FLOAT, -- min temperature in Fahrenheit
    max_temp FLOAT, -- max temperature in Fahrenheit
    snow INTEGETR   -- snow in inches
);

CREATE INDEX IF NOT EXISTS weather_day ON weather(day);
'''


insert_sql = '''
INSERT INTO weather (
    day,
    min_temp,
    max_temp,
    snow
) VALUES (
    :day,
    :min_temp,
    :max_temp,
    :snow
)
'''


def etl(csv_file, db_file):
    with sqlite3.connect(db_file) as db:
        cur = db.cursor()
        cur.executescript(schema_sql)
        cur.executemany(insert_sql, iter_records(csv_file))
        return cur.rowcount



if __name__ == '__main__':
    count = etl('weather.csv', 'weather.db')
    print(f'inserted {count} records')

# # Create table
# c.execute('''
# CREATE TABLE IF NOT EXISTS weather (
#     day DATE,	    -- day of measurements
#     min_temp FLOAT, -- min temperature in Fahrenheit
#     max_temp FLOAT, -- max temperature in Fahrenheit
#     snow INTEGETR   -- snow in inches
# );
#          ''')
#
# c.execute('''CREATE INDEX IF NOT EXISTS weather_day ON weather(day);''')
#
# insert_sql = '''
# INSERT INTO weather (
#     day,
#     min_temp,
#     max_temp,
#     snow
# ) VALUES (
#     :day,
#     :min_temp,
#     :max_temp,
#     :snow
# )
# '''
# # print(datetime.datetime.strptime(str(df['DATE'][1]), '%Y%m%d'))
# weather_data = []
# for i in range(len(df['DATE'])):
#     weather_data.append((datetime.datetime.strptime(str(df['DATE'][i]), '%Y%m%d').date(), df['TMIN'][i], df['TMAX'][i],
#                          df['SNOW'][i]))
#     weather_data[(datetime.datetime.strptime(str(df['DATE'][i]), '%Y%m%d').date(), df['TMIN'][i], df['TMAX'][i],
#                          df['SNOW'][i])]
#     c.executemany(insert_sql, weather_data)
#
#
#
# # c.executemany(insert_sql, weather_data)
# print(c.rowcount)

