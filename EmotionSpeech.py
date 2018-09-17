import sys
import scipy.io.wavfile

sys.path.append("../api")
from api import Vokaturi


class EmotionState:
    def EmotionState (self):

        Vokaturi.load("lib/open/macos/OpenVokaturi-3-0-mac64.dylib")
        # g = CriminalWords.convert_speech_to_text()
        print ("Reading sound file...")
        # file_name = "/Users/raneem/Desktop/voice/2.wav"
        file_name = "/Users/raneem/Downloads/AudioData/DC/a01.wav"
        (sample_rate, samples) = scipy.io.wavfile.read(file_name)

        buffer_length = len(samples)
        c_buffer = Vokaturi.SampleArrayC(buffer_length)
        if samples.ndim == 1:  # mono
	        c_buffer[:] = samples[:] / 32768.0
        else:  # stereo
	        c_buffer[:] = 0.5*(samples[:,0]+0.0+samples[:,1]) / 32768.0

        # Creating VokaturiVoice.
        voice = Vokaturi.Voice (sample_rate, buffer_length)

        # Filling VokaturiVoice with samples
        voice.fill(buffer_length, c_buffer)

        print ("Extracting emotions ...")
        quality = Vokaturi.Quality()
        emotionProbabilities = Vokaturi.EmotionProbabilities()
        voice.extract(quality, emotionProbabilities)


        Emotion = ""
        neutral = emotionProbabilities.neutrality
        happy = emotionProbabilities.happiness
        sad = emotionProbabilities.sadness
        angre = emotionProbabilities.anger
        fear = emotionProbabilities.fear



        print("Emotion Speach of the speaker is ..")
        if Emotion == neutral:
            print ("Neutral")

        elif Emotion == happy:
            print("Happy")

        elif Emotion == sad:
            print("Happy")

        elif Emotion == angre:
            print("Happy")

        elif Emotion == fear:
            print("Fear")

        else:
            print("Not enough sonorancy to determine emotions")


        voice.destroy()

