from psycopg2 import pool


class Database:
    __connection_pool = None

    @classmethod
    def initialize(cls, **kwargs):
        cls.__connection_pool = pool.SimpleConnectionPool(minconn=1, maxconn=1, **kwargs)

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        return cls.__connection_pool.putconn(connection)

    @classmethod
    def close_all_connection(cls, connection):
        return Database.__connection_pool.closeall()


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """
        get a new connection from the pool and then return it
        :return: a new connection from the pool
        """
        self.connection = Database.get_connection()
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
            """if there is an error, e.g., TypeError, AttributeError, ValueError, revert the changes"""
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)
