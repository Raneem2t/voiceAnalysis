#!/usr/bin/env python3

import speech_recognition as sr
import timeit

# obtain path to "english.wav" in the same folder as this script
from os import path

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "/Users/raneem/Desktop/voice/arb.wav")



# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:

    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
start = timeit.default_timer()

try:
    print(r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

stop = timeit.default_timer()

print('Time: ', stop - start)