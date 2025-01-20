import os
import mysql.connector

class DB:
    __host = None
    __port = None
    __user = None
    __password = None
    __instance = None
    __db = None
    __init = None

    def __init__(self):
        if not self.__init:
            self.__host = os.environ['MYSQL_HOST']
            self.__port = os.environ['MYSQL_PORT']
            self.__user = os.environ['MYSQL_USER']
            self.__password = os.environ['MYSQL_PASSWORD']
            self.__init = True

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(DB, cls).__new__(cls)
            cls.__instance.__connect()
        return cls.__instance


    def __connect(self):
        self.__db = mysql.connector.connect(
            host="db",
            user="fastapi_user",
            password="fastapi_password",
            database="fastapi_db",
        )

    def commit(self):
        self.__db.commit()

    def getCursor(self, dictionary = False):
        return self.__db.cursor(dictionary=dictionary)