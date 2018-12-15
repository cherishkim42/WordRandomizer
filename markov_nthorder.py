'''To run in terminal, type: "python3" + "markov_nthorder.py". Default length of output set to 20'''
import sys, random
from dictogram import Dictogram
from freq_analysis import weighted_random

class Markov(dict):

    def __init__(self, word_list = None, order = 2): #Defaulted to Markov second-order
        super(Markov, self).__init__()
        self.order = order #As in order of Markov chain

    def create_markov(self, word_list):
        order = self.order
        for i in range(len(word_list) - self.order):
            key = tuple(word_list[i: i + order])
            value = word_list[i + order]
            self.check_key(key, value)

    def check_key(self, key, value):
        if key in self:
            self[key].add_count(value)
        else:
            self[key] = Dictogram([value])

    def random_output(self, text_list):
        # output_length = int(sys.argv[2]) #
        output_length = 20 #Change this number to tweak length of output
        string = ""
        random_word = random.choice(list(self)) #Picks random key
        next_word = weighted_random(self[random_word])
        string = string + ' '.join(random_word) + ' ' + next_word

        for i in range(output_length - self.order - 1):
            ephem = list(random_word) #get it? short for ephemeral
            ephem.append(next_word)
            random_word = tuple(ephem)
            try:
                next_word = weighted_random(self[string])
            except KeyError:
                random_word = random.choice(list(self))
                next_word = weighted_random(self[random_word])
            while next_word == None:
                next_word = weighted_random(self[random_word])
            string = string + " " + next_word
        return string

def main():
    # f = open(sys.argv[1], "r").read().split() #When running in terminal, comment out next line & un-comment this one if you want to use a different .txt file
    f = open("corpus.txt").read().split()
    random_chain = Markov(f, 2) #To change order of Markov chain, alter the integer argument
    random_chain.create_markov(f)
    return random_chain.random_output(f)

if __name__ == '__main__':
    print(main())
