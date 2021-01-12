from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(minconn=1, maxconn=1,
                                            database='learning',
                                            user='i-sip_iot',
                                            password='Your_Password',
                                            host='localhost')


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """
        get a new connection from the pool and then return it
        :return: a new connection from the pool
        """
        self.connection = connection_pool.getconn()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        backing the connection into connection pool
        :param exc_type: exception type --> type of the error
        :param exc_val: exception value --> value of the error
        :param exc_tb: exception traceback --> explaining why the error happen
        :return: None
        """
        if exc_val is not None:
            """if there is an error revert the changes"""
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        connection_pool.putconn(self.connection)
