"""Load & convert data from CSV file using Python built-in csv module"""
import bz2
import csv
from collections import namedtuple
from datetime import datetime

Column = namedtuple('Column', 'src dest convert')


def parse_timestamp(text):
    return datetime.strptime(text, '%Y-%m-%d %H:%M:%S')


columns = [
    Column('VendorID', 'vendor_id', int),
    Column('passenger_count', 'num_passengers', int),
    Column('tip_amount', 'tip', float),
    Column('total_amount', 'price', float),
    Column('tpep_dropoff_datetime', 'dropoff_time', parse_timestamp),
    Column('tpep_pickup_datetime', 'pickup_time', parse_timestamp),
    Column('trip_distance', 'distance', float),
]


def iter_records(file_name):
    with bz2.open(file_name, 'rt') as fou:
        reader = csv.DictReader(fou)
        for csv_rec in reader:
            record = {}
            for col in columns:
                val = csv_rec[col.src]
                record[col.dest] = col.convert(val)
            yield record


def example():
    from pprint import pprint

    for i, record in enumerate(iter_records('taxi.csv.bz2')):
        if i >= 10:
            break
        pprint(record)


example()
