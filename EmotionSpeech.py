import sys
import scipy.io.wavfile

sys.path.append("../api")
from api import Vokaturi
import CriminalWords


class d:
    def r (self):
# print ("Loading library...")
# Vokaturi.load("../lib/open/macos/OpenVokaturi-3-0-mac64.dylib")
        Vokaturi.load("lib/open/macos/OpenVokaturi-3-0-mac64.dylib")
        g = CriminalWords.convert_speech_to_text()
        file_name = g.gu()
        print ("Reading sound file...")
# file_name = sys.argv[1]
# file_name = "/Users/raneem/Desktop/voice/2.wav"
# file_name = "/Users/raneem/Desktop/voice/01_samples_trimmed_noise_reduced/04_voices_org.wav"
# file_name = "/Users/raneem/Downloads/noise_reduction-master/00_samples/01_counting.m4a"
        (sample_rate, samples) = scipy.io.wavfile.read(file_name)

        buffer_length = len(samples)
        c_buffer = Vokaturi.SampleArrayC(buffer_length)
        if samples.ndim == 1:  # mono
	        c_buffer[:] = samples[:] / 32768.0
        else:  # stereo
	        c_buffer[:] = 0.5*(samples[:,0]+0.0+samples[:,1]) / 32768.0

# print ("Creating VokaturiVoice...")
        voice = Vokaturi.Voice (sample_rate, buffer_length)

# print ("Filling VokaturiVoice with samples...")
        voice.fill(buffer_length, c_buffer)

        print ("Extracting emotions ...")
        quality = Vokaturi.Quality()
        emotionProbabilities = Vokaturi.EmotionProbabilities()
        voice.extract(quality, emotionProbabilities)

        if quality.valid:
	        print ("Neutral: %.3f" % emotionProbabilities.neutrality)
	        print ("Happy: %.3f" % emotionProbabilities.happiness)
	        print ("Sad: %.3f" % emotionProbabilities.sadness)
	        print ("Angry: %.3f" % emotionProbabilities.anger)
	        print ("Fear: %.3f" % emotionProbabilities.fear)

        else:
	        print ("Not enough sonorancy to determine emotions")

        voice.destroy()

