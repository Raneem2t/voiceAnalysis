import psycopg2
from pprint import pprint


class DatabaseConnection:

    def __init__(self):
        try:
            self.conniction = psycopg2.connect(
                "dbname= 'sample_db' user='raneem' host='localhost' password='123456' port='5432'")
            self.conniction.autocommit = True
            self.cursor = self.conniction.cursor()

        except:
            pprint("Cannot connect to database")