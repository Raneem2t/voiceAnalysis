import sys
import scipy.io.wavfile

sys.path.append("../api")
from api import Vokaturi
import ConvertAudio

co = ConvertAudio


class EmotionState:


    def EmotionState (self):

        Vokaturi.load("lib/open/macos/OpenVokaturi-3-0-mac64.dylib")
        # g = CriminalWords.convert_speech_to_text()
        # file_name = "/Users/raneem/Desktop/voice/2.wav"

        file_name = "/Users/raneem/PycharmProjects/databaseEG/venv/lib/python2.7/site-packages/test/data/happy.mp3"

        file_name = co.convert(file_name)


        # file_name = "/Users/raneem/Downloads/OpenVokaturi-3-0a/examples/hello.wav"
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



        neutral = emotionProbabilities.neutrality
        happy = emotionProbabilities.happiness
        sad = emotionProbabilities.sadness
        angre = emotionProbabilities.anger
        fear = emotionProbabilities.fear

        Emotion = [neutral, happy, sad, angre, fear]

        x = max(Emotion)


        print("Emotion Speach of the speaker is ..")
        if x == neutral:
            print ("Neutral\n")

        elif x == happy:
            print("Happy\n")

        elif x == sad:
            print("Sad\n")

        elif x == angre:
            print("Angry\n")

        elif x == fear:
            print("Fear\n")

        else:
            print("Not enough sonorancy to determine emotions\n")


        voice.destroy()

