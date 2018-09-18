import EmotionSpeech
import CriminalWords
import timeit



if __name__ == '__main__':

    start = timeit.default_timer()

    c= CriminalWords.CriminalWords()
    e= EmotionSpeech.EmotionState()

    e.EmotionState()
    c.find_criminal_words()
    c.find_abnormalWord()


    stop = timeit.default_timer()

    print('Time: ', stop - start)