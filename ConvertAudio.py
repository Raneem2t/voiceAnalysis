from pydub import AudioSegment


def convert(file_path):

    src = file_path
    dst = "test.wav"

    # convert wav to mp3
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

    new_path = "test.wav"

    return new_path