import psycopg2
from pprint import pprint
from collections import Counter
import requests

# from langdetect import detect


APP_ACCESS_TOKEN = 'P637HVIWSHN73DKHIB2SPGVTKLVRZWSI'

base_url = 'https://api.wit.ai/speech'


def read_audio(file_path):
    # function to read audio(wav) file
    with open(file_path, 'rb') as f:
        audio = f.read()
    return audio

class CriminalWords:


    def Most_Common(lst):
        return max(set(lst), key=lst.count)

    def convert_speech_to_text(self):

        file = "/Users/mac/Desktop/Voice/1.mp3"
        # file = "/Users/raneem/Desktop/voice/01_samples_trimmed_noise_reduced/04_voices_org.wav"
        audio = read_audio(file)
        headers = {'authorization': 'Bearer ' + APP_ACCESS_TOKEN,
               'Content-Type': 'audio/wav'}
        data_response = requests.post(base_url, headers=headers, data=audio).json()

        text = data_response['_text']
        return text


    # Conشnect to the database
    def __init__(self):
        try:
            self.conniction = psycopg2.connect(
                "dbname= 'word_db' user='abrar' host='localhost' password='12345' port='5432'")
            self.conniction.autocommit = True
            self.cursor = self.conniction.cursor()

        except:
            pprint("Cannot connect to database")


    def find_criminal_words(self):

        text = self.convert_speech_to_text()
        # self.obj.gu(text)

        # Spilt text into words and
        # Skip some unusual words
        try:
            print(text,"\n")  # print the text

            skipwords = ['what', 'who', 'is', 'a', 'at', 'is', 'he', "are", "the", "so", "to", "for", "if", "where", "was", "ware", "by"]
            wordList = text.split(" ")  # split text into words

            resultwords = [word for word in wordList if word.lower() not in skipwords]
            result = ' '.join(resultwords)

            # print(result)


            # for words in resultwords:
            #     # print(words)




            # detect the criminal words

            try:
                print("The criminal words were detected are: ...")
                for i in range(len(wordList)):

                    self.cursor.execute("SELECT name FROM pet1 WHERE name = '%s'" % wordList[i])

                    for row in self.cursor:
                        row == ""

                        # self.obj.gu(row)
                        dd="".join(str(x) for x in row)
                        print (dd)
                        print(row)
            except:
                print("No criminal words detect...")

            # Detect if it is english or not



        except:
            print("Error")

    def find_detect_words(self):
        try:
            # t = "مرحبا"
            if detect(text) == 'en':
                print("\nIt is an English Speech.\n")
            else:
                print("\nIt is not English Speech.\n")
        except:
            print("\nCan not detect the language.\n")


    def find_frequent_words(self):
        try:
            text = self.convert_speech_to_text()

            skipwords = ['what', 'who', 'is', 'a', 'at', 'is', 'he', "are", "the", "so", "to", "for", "if", "where", "was", "ware", "by"]
            wordList = text.split(" ")  # split text into words

            resultwords = [word for word in wordList if word.lower() not in skipwords]
            result = ' '.join(resultwords)
            frequent = Counter(resultwords)
            most_occur = frequent.most_common()
            print("The frequent words are .. \n")
            print(most_occur, "\n")

        except:
            print("There is no frequent words")

    def find_abnormalWord(self):
        text = self.convert_speech_to_text()
        # self.obj.gu(text)
        # Spilt text into words
        dd = []
        try:
            print ("jg")
            print(text)  # print the text


            wordList = text.split(" ")  # split text into words

            print("\nTo find abnormal word ..")
            table_name = input('Enter name of case: ')

            # print("Case name is: ", table_name)

            create_table_command = "CREATE TABLE " + table_name + "(name varchar (100))"
            self.cursor.execute(create_table_command)
            # print("CREATE done")
            abnormalWord = input('Enter abnormal words :').split()
            # print("Abnormal words : ", abnormalWord)
            for i in range(len(abnormalWord)):
                self.cursor.execute("INSERT INTO " + table_name + "(name) VALUES('" + abnormalWord[i] + "')")
                # print("INSERT done")

            try:
                print("The abnormal words were detected are ..")
                for i in range(len(wordList)):
                    self.cursor.execute("SELECT name FROM " + table_name + " WHERE name = '%s'" % wordList[i])

                    for row in self.cursor:
                        row == ""


                        dd.append(row)
                        # dd.append("".join(str(x) for x in row))
                        # CwordList = dd

                        # print (dd)
                        # print(row)
                        # counts = Counter(row).most_common(1)
                        # print(counts)

            except:
                print("No abnormal words detect...")

        except:
            print("Error")
        return dd

if __name__ == '__main__':
    criminal_Words = CriminalWords()

    ss=criminal_Words.find_abnormalWord()
    print (" ".join(str(x) for x in ss))