import time
import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multi_dictionary = md.MultiDictionary()


    def handleSentence(self, txtIn, language):
        text = replaceChars(txtIn)
        words = text.split()
        start_1 = time.time()
        richwords = self.multi_dictionary.searchWord(words, language)
        end_1 = time.time()
        cnt = 0
        print("Using contains: ")
        for word in richwords:
            if word._corretta == False:
                print(word.__str__())
                cnt += 1
        print(f"Number of words uncorrected: {cnt}")
        print(f"Time elapsed: {end_1 - start_1}")
        print("-------------------------------------\nUsing linear search")
        start_2 = time.time()
        richwords_1 = self.multi_dictionary.searchWordLinear(words, language)
        end_2 = time.time()
        for word in richwords_1:
            if word._corretta == False:
                print(word.__str__())
        print(f"Number of words uncorrected: {cnt}")
        print(f"Time elapsed: {end_2 - start_1}")










    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\'*{}[]()>#+-.!?=_-$£@"
    for c in chars:
        text = text.replace(c, "")
    return text