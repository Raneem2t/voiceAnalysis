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



    # create table
def create_table(self):
    create_table_command = "CREATE TABLE pet(id serial PRIMARY KEY, name varchar (100), age integer NOT NULL)"
    self.cursor.execute(create_table_command)



    # insert new record
def insert_new_record(self):
    new_record = ("meo", "3")
    insert_command = "INSERT INTO pet(name,age) VALUES('" + new_record[0] + "','" + new_record[1] + "')"
    pprint(insert_command)
    self.cursor.execute(insert_command)

    # display all records
def query_all(self):
    self.cursor.execute("SELECT * FROM pet")
    cats = self.cursor.fetchall()
    for cat in cats:
        pprint("each pet : {0}".format(cat))

    # update record
def update_record(self):
    update_comoand = "UPDATE pet SET age=10 where id=1"
    self.cursor.execute(update_comoand)


    # delete table
def drop_table(self):
    drop_table_command = "DROP TABLE pet "
    self.cursor.execute(drop_table_command)
