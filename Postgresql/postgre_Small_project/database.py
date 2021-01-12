from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(minconn=1, maxconn=1,
                                            database='learning',
                                            user='i-sip_iot',
                                            password='Your_Password',
                                            host='localhost')


class ConnectionFromPool:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        """
        get a new connection from the pool and then return it
        :return: a new connection from the pool
        """
        self.connection = connection_pool.getconn()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        backing the connection into connection pool
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return: None
        """
        self.connection.commit()
        connection_pool.putconn(self.connection)
