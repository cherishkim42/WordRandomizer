# To run in terminal, type: "python3" + "markov_firstorder.py" + file name
from dictogram import Dictogram

class Markov(Dictogram): #Takes dictionary histogram (dictogram) --> dictionary of dictograms of words after a word

    def __init__(self, words=None):
        super(Markov, self).__init__()
        if words is not None:
            words_length = len(words)
            for word_index in range(words_length - 1): #Final index lacks subsequent word, so it's not included
                self.add_count(words[word_index],words[word_index+1])

    def add_count(self, word, next_word):
        if word in self: #Word is in self
            if next_word in self[word]: #[word][next_word] has appeared before
                self[word][next_word] += 1 #Add 1
            else: #First time seeing [word][next_word]
                self[word][next_word] = 1 #Start with 1
        else: #Word not in self - it's new
            self[word] = {next_word:1} #New entry entirely

    def frequency(self, word, next_word):
        if next_word in self[word]: #Whenever [word][next_word] exists....
            return self[word][next_word] #...returns the # of times that happens
        else: #If [word][next_word] just never happens....
            return 0 #...return 0. Because it never happens.

if __name__ == '__main__':
    import sys
    f = open(sys.argv[1], "r").read().split()
    markov = Markov(f)
    print('Markov Dictionary of Dictograms: {}'.format(markov))
