import psycopg2
from psycopg2 import sql

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='yourdbname',
            user='yourusername',
            password='yourpassword',
            host='localhost',
            port='5432'
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    # Thêm các phương thức để truy vấn dữ liệu