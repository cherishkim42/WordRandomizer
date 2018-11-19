# To run in terminal, type: "python3" + "dictionary_words.py" + (# of words you want returned in a random order from dictionary)
import random
import sys

def load_word():
    words = [] #Creates empty array
    i = 0 #Instantiate counter
    length = int(sys.argv[1]) #Stores number of words specified by user in terminal
    while i < length: #While value of counter is less than how many words the user wants
        #The following line will open file, read it, and split at the spaces
        f = open('/usr/share/dict/words', 'r').read().split() #Convention dictates mode="r" if file is only going to be read
        word = random.choice(f) #Picks word at random from f
        words.append(word) #Adds randomly picked word to array
        show = " ".join(words) #Stores a version of array without brackets, commas, and quotation marks
        i += 1 #With completion of while loop, we add 1 to counter
    return show

def random_word(words_list):
    secret_word = random.choice(words_list)
    return secret_word

if __name__ == '__main__':
    print(load_word())

# Originally sandwiched between load_word() func and if__name__ == '__main'__'
# loaded_words = load_word()

# Thanks to Dylan Finn, Ryan Nguyen, Anwar Azeez, & Erica Naglik
