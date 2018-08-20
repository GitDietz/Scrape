from psycopg2 import pool

'''connection_pool = pool.SimpleConnectionPool(1, 1, database='learning',
                                            user='dieterthierry',
                                            password='Wagter10',
                                            host='localhost')
'''
class Database:
    __connection_pool = None # makes it a property of the class iteself

    #@staticmethod could be used
    @classmethod
    def initialise(cls,**kwargs):
        Database.__connection_pool = pool.SimpleConnectionPool(1, 1, **kwargs)

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls,connection):
        Database.__connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        Database.__connection_pool.closeall()


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit() #required to commit due to modification of the with effect
        Database.return_connection(self.connection)



