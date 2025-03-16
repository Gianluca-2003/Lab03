class Dictionary:
    def __init__(self):
        self.dictionary = []

    def loadDictionary(self,path):
        try:
            with open(path,'r') as file:
                for line in file:
                    self.dictionary.append(line.strip())
        except FileNotFoundError:
            print("File not found")


    def printAll(self):
        for word in self.dictionary:
            print(word)

    def __contains__(self, word):
        return word in self.dictionary


    @property
    def dict(self):
        return self.dictionary