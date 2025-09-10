import pymysql
from pymysql.cursors import DictCursor

class DBHadler:

    def __init__(self, host, user, password, database):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            cursorclass=DictCursor
        )
        self.cursor = self.conn.cursor()

    def fetch_one(self, query, params=None):
        # query = "select * from orders where id = %s"
        # params = (1,) --- trailing it necessary to make it a tuple
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def execute(self, query, params=None):
        self.cursor.execute(query, params)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()