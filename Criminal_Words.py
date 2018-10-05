
import psycopg2
import speechToText

# Connect to the database
def __init__(self):
    try:
        self.conniction = psycopg2.connect("dbname= 'postgres' user='raneem' host='localhost' password='123456' port='5432'")
        self.conniction.autocommit = True
        self.cursor = self.conniction.cursor()

    except:
        print("Cannot connect to database")



def find_criminal_words():

    text = speechToText.convert_speech_to_text()
    print(text)
    # self.obj.gu(text)
    cr= []
    # Spilt text into words and
    # Skip some unusual words
    try:
        skipwords = ['what', 'who', 'is', 'a', 'at', 'is', 'he', "are", "the", "so", "to", "for", "if", "where", "was",
                     "ware", "by"]
        wordList = text.split(" ")  # split text into words

        resultwords = [word for word in wordList if word.lower() not in skipwords]
        result = ' '.join(resultwords)

        # print(result)
        conn = ""
        try:
            conn = psycopg2.connect("dbname= 'postgres' user='raneem' host='localhost' password='123456' port='5432'")
        except:
            print ("I am unable to connect to the database.")

        cur = conn.cursor()

        # detect the criminal words

        try:
            print("The criminal words were detected are: ...")
            for i in range(len(wordList)):

                cur.cursor.execute("SELECT name FROM pet WHERE name = '%s'" % wordList[i])

                for row in cur.cursor:
                    row == ""
                    cr = row

                    # self.obj.gu(row)

                    print(row)
                    return cr
        except:
            print("No criminal words detect...")


    except:
        print("Error")
    return cr