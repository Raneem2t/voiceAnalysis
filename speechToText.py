
import requests
import gui

APP_ACCESS_TOKEN = 'P637HVIWSHN73DKHIB2SPGVTKLVRZWSI'

base_url = 'https://api.wit.ai/speech'


# gui_file = gui

def read_audio(file_path):
    # function to read audio(wav) file
    with open(file_path, 'rb') as f:
        audio = f.read()
    return audio


# class speechToText:


def convert_speech_to_text(self):
    # file gui_file.answer
    file = "/Users/mac/Desktop/Voice/1.mp3"
    # file = "/Users/raneem/Desktop/voice/01_samples_trimmed_noise_reduced/04_voices_org.wav"
         # file = tryGui.path_name
    audio = read_audio(file)
    headers = {'authorization': 'Bearer ' + APP_ACCESS_TOKEN,
               'Content-Type': 'audio/wav'}
    data_response = requests.post(base_url, headers=headers, data=audio).json()
    # self.find_criminal_words(wordList)

        # print(data_response['_text']) # Print the text

    return data_response['_text']

def spilt_into_words(self):
    text = self.convert_speech_to_text()

    try:
        print(text)  # Print the text
        wordList = text.split(" ")  # Split text into words

            # Print each word in line
        for word in wordList:
            print(word)
    except:
        print("Error")



# if __name__== '__main__':
#     speech_to_Text = speechToText()
#     # database_connection.create_table()       # create table
#     # database_connection.insert_new_record()  # insert new record
#     # database_connection.query_all()          # display all records
#     # database_connection.update_record()      # update record
#     # database_connection.drop_table()         # delete table
#     # database_connection.audio_to_text()
#     speech_to_Text.spilt_into_words()
