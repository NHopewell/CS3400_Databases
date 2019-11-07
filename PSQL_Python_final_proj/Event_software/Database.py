from psycopg2 import pool

#def connect():
#    return psycopg2.connect(user = 'postgres', password = 'Hopeless14', database = 'Learning', host = 'localhost')

class Database:
    __connection_pool = None  # property belongs to class not object - not inside init, belongs to all objects
    # pull of max 10 connections to use
    # only needs to be called once for all db objects since connection_pool is a class property not a self.property
    @staticmethod  # no reference to class or current method, allows us to directly call initialise without self param
    def initialise(**kwargs):
        Database.__connection_pool = pool.SimpleConnectionPool(1,
                                                               10,
                                                               **kwargs) # accept any number of named params

    @classmethod
    def get_connection(cls):  # get connection from pool
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):  # connection to put back as param
        return Database.__connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):  # stop all commits and close connections
        Database.__connection_pool.closeall()



# first SimpleConnectionPool param = min # of connections
# second SimpleConnectionPool param = max # pool can handle at once
class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None  # create connection property
        self.cursor = None  # initialize cursor

    def __enter__(self):
        self.connection = Database.get_connection()  # when entering with statement, get connection from the pool
        self.cursor = self.connection.cursor()  # get cursor from connection
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # if an exception value is raised when inserting data (e.g.TypeError, AttributeError, ValueError ect),
        #  roll back the connection and remove data
        if exc_val:  # same as.. "if exc_val is not None:"
            self.connection.rollback()
        else:
            # when exiting with, close cursor, commit to db and put connection back in pool
            self.cursor.close()
            self.connection.commit()

        Database.return_connection(self.connection) # always want to put connection back

''' Note on the above methods, we want connection_pool to be private (not directly accessible)
    so that other methods from other areas of the program (or other users) cannot
    change this pool by simply calling Database.connection_pool.getconn()
    This would be very necessary if getconn() also did some set up. This is why
    connection_pool has two leading underscores __ to make the variable private and hidden
    from other programs'''