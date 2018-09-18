from pydub import AudioSegment


def convert(file_path):

    path = file_path
    new_path = "audio_file/test.wav"

    # convert wav to mp3
    sound = AudioSegment.from_mp3(path)
    sound.export(new_path, format="wav")

    return new_path