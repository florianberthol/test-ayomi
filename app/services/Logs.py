import os
import mysql.connector
import csv
import io

__host = None
__port = None
__user = None
__password = None

class Logs:
    def __init__(self):
        self.__host = os.environ['MYSQL_HOST']
        self.__port = os.environ['MYSQL_PORT']
        self.__user = os.environ['MYSQL_USER']
        self.__password = os.environ['MYSQL_PASSWORD']

    def __connect(self):
        return mysql.connector.connect(
            host="db",
            user="fastapi_user",
            password="fastapi_password",
            database="fastapi_db",
        )

    def log(self, data):
        db = self.__connect()
        cursor = db.cursor()

        cursor.execute('insert into logs(operation, result) values (%s, %s)', (data['operation'], data['result']))
        db.commit()

    def dump(self):
        db = self.__connect()
        cursor = db.cursor(dictionary=True)
        cursor.execute('select * from logs order by id desc')
        data = cursor.fetchall()

        output = io.StringIO()
        writer = csv.writer(output)

        writer.writerow(('id','operation','result'))
        for row in data:
            writer.writerow((row['id'], row['operation'], row['result']))

        output.seek(0)
        return output
