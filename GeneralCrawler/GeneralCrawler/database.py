from pymysql import Connection

class DatabaseConnection:
    def __init__(self):
        self.connection = Connection(
            host='localhost',
            port=3306,
            user = 'root',
            password = '123456',
            database='test_crawler',
        )
        
    def get_connection(self):
        return self.connection