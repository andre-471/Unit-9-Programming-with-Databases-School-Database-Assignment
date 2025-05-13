import atexit
import os
import sys
import signal

import mysql.connector
from dotenv import load_dotenv, find_dotenv
from mysql.connector import errorcode
from mysql.connector.abstracts import MySQLConnectionAbstract


class DBConnection:
    def __init__(self, name):
        self.connection: MySQLConnectionAbstract = None

        atexit.register(self.disconnect)
        signal.signal(signal.SIGINT, self.disconnect)
        signal.signal(signal.SIGTERM, self.disconnect)

        self.connect(name)

    def connect(self, name):
        if self.connection:
            print("Connection already exists")
            return

        if not find_dotenv():
            raise FileNotFoundError(".env file doesn't exist!")

        load_dotenv()

        user = os.environ.get('DB_USERNAME')
        password = os.environ.get('DB_PASSWORD')

        try:
            self.connection = mysql.connector.connect(
                user=user,
                password=password,
                host='10.8.37.226',
                database=name,
                autocommit=True,
                raise_on_warnings=True
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

            sys.exit(1)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Connection closed")
        else:
            print("No connection to close")

    def query(self, query, params=None) -> list[tuple]:
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)

            return cursor.fetchall()
