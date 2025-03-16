import dictionary as d
import richWord as rw
from richWord import RichWord


class MultiDictionary:

    def __init__(self):
        self.languages = {
            "italian": d.Dictionary(),
            "english": d.Dictionary(),
            "spanish": d.Dictionary()
        }
        self.load_all_dictionaries()

    def load_all_dictionaries(self):
        self.languages['italian'].loadDictionary("resources/Italian.txt")
        self.languages['english'].loadDictionary("resources/English.txt")
        self.languages['spanish'].loadDictionary("resources/Spanish.txt")


    def printDic(self, language):
        self.languages[language].printDictionary()

    def searchWord(self, words, language):
        richwords = [RichWord(word.lower()) for word in words]
        dictionary = self.languages[language]
        for word in richwords:
            if dictionary.__contains__(word.__str__()):
                word.setParolaGiusta()
        return richwords


    def searchWordLinear(self, words, language):
        richwords = [RichWord(word.lower()) for word in words]
        dictionary = self.languages[language].dictionary
        for word in richwords:
            for w in dictionary:
                if word.__str__()== w.__str__():
                    word.setParolaGiusta()
        return richwords





def searchWordDichotomic(self, words, language):
    richwords = [RichWord(word.lower()) for word in words]
    dictionary = self.languages[language].dictionary  # Lista ordinata di parole

    def binary_search(word, dictionary):
        left, right = 0, len(dictionary) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_word = dictionary[mid]

            if mid_word == word:
                return True
            elif mid_word < word:
                left = mid + 1
            else:
                right = mid - 1

        return False  # Parola non trovata

    for word in richwords:
        if binary_search(word.__str__(), dictionary):  # Cerca con il metodo dicotomico
            word.setParolaGiusta()

    return richwords












