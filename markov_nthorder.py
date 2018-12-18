'''There are two options for running this file. (1) To view in browser, open terminal and type: "export FLASK_APP=hello.py". Then type "flask run". Terminal will then say "* Running on http://127.0.0.1:5000/". Navigate to http://127.0.0.1:5000/ in browser. (2) To run solely in terminal, see comments added to random_output method in Markov class and global main function. Once those changes are made, type the following into terminal: "python3" + "markov_nthorder.py" + filename + desired output length. Default length of output is set to 20'''
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
        # output_length = int(sys.argv[2]) #Uncomment this and comment out the following line if you want to run the file in terminal. To do so you also need to alter the global main() function - see the comments there to see what to uncomment and comment. When running in terminal, type: "python3" + "markov_nthorder.py" + filename + desired output length.
        output_length = 20 #Change this number to tweak length of output
        string = "" #Initialize string
        random_word = random.choice(list(self)) #Picks random key
        next_word = weighted_random(self[random_word]) #Passes this random key in as histogram to weighted_random fxn from freq_analysis.py
        string = string + ' '.join(random_word) + ' ' + next_word #Update string

        for i in range(output_length - self.order - 1):
            ephem = list(random_word) #get it? short for ephemeral
            ephem.append(next_word)
            random_word = tuple(ephem)
            try:
                next_word = weighted_random(self[string])
            except KeyError: #Try again
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
