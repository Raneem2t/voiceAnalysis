# #!/usr/bin/env python3
#
# import speech_recognition as sr
# import timeit
#
# # obtain path to "english.wav" in the same folder as this script
# from os import path
#
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "/Users/raneem/Desktop/voice/arb.wav")
#
#
#
# # use the audio file as the audio source
# r = sr.Recognizer()
# with sr.AudioFile(AUDIO_FILE) as source:
#
#     audio = r.record(source)  # read the entire audio file
#
# # recognize speech using Sphinx
# start = timeit.default_timer()
#
# try:
#     print(r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))
#
# stop = timeit.default_timer()
#
# print('Time: ', stop - start)

import requests

APP_ACCESS_TOKEN = 'P637HVIWSHN73DKHIB2SPGVTKLVRZWSI'

# Arabic
# APP_ACCESS_TOKEN = 'O7HE56PBUUTIC4IUZGO3EDDWCX2VTRIL'

base_url = 'https://api.wit.ai/speech'


def read_audio(file_path):
    # function to read audio(wav) file
    with open(file_path, 'rb') as f:
        audio = f.read()
    return audio


def convert_speech_to_text():
    file = "/Users/raneem/Desktop/voice/Noise_Test/My_voice/T2_24.wav"
    audio = read_audio(file)
    headers = {'authorization': 'Bearer ' + APP_ACCESS_TOKEN,
               'Content-Type': 'audio/wav'}
    data_response = requests.post(base_url, headers=headers, data=audio).json()

    text = data_response['_text']
    print(text)
    return text


