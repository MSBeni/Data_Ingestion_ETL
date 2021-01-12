from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(minconn=1, maxconn=10,
                                            database='learning',
                                            user='i-sip_iot',
                                            password='Your_Password',
                                            host='localhost')

# def connect():
#     return psycopg2.connect("dbname='learning' user='i-sip_iot' password='Your_Password'")