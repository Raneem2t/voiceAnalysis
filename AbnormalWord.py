import psycopg2

import DatabaseConnect
import speechToText

class cc:

    connect = DatabaseConnect.DatabaseConnection

    def find_abnormalWord():
        # self.connect.__init__(self)
        text = speechToText.convert_speech_to_text()
        d = []

        # Spilt text into words

        wordList = text.split(" ")  # split text into words
        # for words in wordList:
        #     print(words)
        conn = ""
        try:
            conn = psycopg2.connect("dbname= 'postgres' user='raneem' host='localhost' password='123456' port='5432'")
        except:
            print("I am unable to connect to the database.")

        cur = conn.cursor()

        try:

            table_name = input('Enter name of case: ')

            create_table_command = "CREATE TABLE "+table_name+"(name varchar (100))"
            cur.cursor.execute(create_table_command)

            wordfreq = input('Enter abnormal word ').split()

            print("abnormal word ", wordfreq)

            for i in range(len(wordfreq)):
                cur.cursor.execute("INSERT INTO "+table_name+"(name) VALUES('" + wordfreq[i] + "')")

            try:
                print("The abnormal words were detected are: ...")

                for i in range(len(wordList)):
                    cur.cursor.execute("SELECT name FROM "+table_name+" WHERE name = '%s'" % wordList[i])

                    for row in cur.cursor:
                        row == ""
                        d.append("\n".join(map(str, row)))
                return d

            except:
                print("No abnormal words detect...")

        except:
            print("Error")


        return d


if __name__ == '__main__':

    cf = cc()
    l= cf.find_abnormalWord()
    abnormal ="\n".join(str(e) for e in l)
    print(abnormal)



