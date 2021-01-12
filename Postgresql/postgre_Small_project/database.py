import psycopg2

class Database:
    def __init__(self):
        pass


def connect():
    return psycopg2.connect("dbname='learning' user='i-sip_iot' password='Your_Password'")