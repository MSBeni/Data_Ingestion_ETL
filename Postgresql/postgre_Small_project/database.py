from psycopg2 import pool


class ConnectionPool():
    def __init__(self):
        self.connection_pool = pool.SimpleConnectionPool(minconn=1, maxconn=10,
                                                         database='learning',
                                                         user='i-sip_iot',
                                                         password='Your_Password',
                                                         host='localhost')

    def __enter__(self):
        return self.connection_pool.getconn()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


