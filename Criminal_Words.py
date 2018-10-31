
import psycopg2
import re
import csv

# Connect to the database
# def __init__(self):
#     try:
#         self.conniction = psycopg2.connect("dbname= 'postgres' user='raneem' host='localhost' password='123456' port='5432'")
#         self.conniction.autocommit = True
#         self.cursor = self.conniction.cursor()
#
#     except:
#         print("Cannot connect to database")
#
#
#
# def find_criminal_words(text):
#
#     text = text
#     # print(text)
#     # self.obj.gu(text)
#     cr= []
#     # Spilt text into words and
#     # Skip some unusual words
#     try:
#         skipwords = ['what', 'who', 'is', 'a', 'at', 'is', 'he', "are", "the", "so", "to", "for", "if", "where", "was",
#                      "ware", "by"]
#
#         wordList = text.split(" ")  # split text into words
#
#         resultwords = [word for word in wordList if word.lower() not in skipwords]
#         result = ' '.join(resultwords)
#
#         print(result)
#         conn = ""
#         try:
#             conn = psycopg2.connect("dbname= 'postgres' user='raneem' host='localhost' password='123' port='5432'")
#         except:
#             print ("I am unable to connect to the database.")
#
#         cur = conn.cursor()
#
#         # detect the criminal words
#
#         try:
#             print("The criminal words were detected are: ...")
#             for i in range(len(resultwords)):
#
#                 cur.execute("SELECT name FROM word WHERE name = '%s'" % resultwords[i])
#                 # print("2")
#                 for row in cur:
#                     row == ""
#                     cr.append(row)
#
#                     # print(row)
#
#             f = "".join(str(e) for e in cr)
#             res = re.sub('\ |\(|\.|\)|\/|\'|\:', '', f)
#
#         except:
#             res = "No criminal words detect..."
#             print("No criminal words detect...")
#
#
#
#     except:
#         res = "Error"
#         print("Error")
#
#     print(res)
#     return res

def find_criminal_words(text):

        text = text
        cr = []

        try:
            skipwords = ['what', 'who', 'is', 'a', 'at', 'is', 'he', "are", "the", "so", "to", "for", "if", "where",
                         "was", "ware", "by"]

            wordList = text.split(" ")  # split text into words

            resultwords = [word for word in wordList if word.lower() not in skipwords]
            result = ' '.join(resultwords)

            # print(result)
        except:
            res = "Error"
            print("Error")

        try:
            print("The criminal words were detected are: ...")

            with open('test.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',')

                for row in reader:
                    for field in row:
                        for w in wordList:
                            if field == w:

                                cr.append(field)
                                print(field)


            res = " ".join(str(e) for e in cr)
            # res = re.sub('\ |\(|\.|\)|\/|\'|\:', ' ', f)

        except:
            res = "No criminal words detect..."
            print("No criminal words detect...")



        print(res)
        return res




if __name__ == '__main__':

    c= find_criminal_words("hi Hi Hey")
    print(c)



