# To run in terminal, type: "python3" + "freq_analysis.py" + file name
import random
from collections import Counter
from fractions import Fraction #Tried using this for word_freq fxn but haven't yet figured out how to use it without "Fraction" and commas being included in the return. Very ugly
import sys

def histogram():
    f = open(sys.argv[1], "r").read().split()
    dict = {} #Creates empty dictionary
    for entry in f: #Time to iterate through the whole shebang!
        if entry in dict: #If dictionary already contains entry, append +1
            dict[entry] += 1
        else: #If dictionary doesn't already contain entry, create an entry with {entry_word: 1} as {key: value} pair
            dict[entry] = 1
    return dict

def random_word(histogram):
    accumulator = 0 #instantiate accumulator
    histo_length = sum(histogram.values()) #Stores length of histogram
    random_num = random.randint(0, histo_length - 1)
    for key, value in histogram.items(): #need .items() to iterate
        accumulator += value
        if accumulator > random_num:
            return key
        else:
            continue #Must be continue, not pass, because continue makes the fxn iterate again. Pass concludes with no return.

def weighted_random(histogram):
    counter = 0 #Initialize counter
    total_frequency_list = histogram.values()
    total_frequency_number = 0 #Tallied up frequency
    for frequency in total_frequency_list:
        total_frequency_number += frequency
    random_count = random.randrange(0, total_frequency_number)
    for key,value in histogram.items():
        counter += value
        if counter > random_count:
            return key

# This returns histogram with ratio of (instances of a word):(number of words in entire corpus)
# Still need to figure out how to print ratios as proper fractions, but purely mathematically, this is ok
def word_freq(histogram):
    f = open(sys.argv[1], "r").read().split()
    for key in histogram:
        histogram[key] = histogram[key]/len(f) #For short .txt files, current code is fine. For longer files, we get vexingly tiny decimals in scientific notation
    return histogram

if __name__ == '__main__':
    # print(word_freq(histogram()))
    print(weighted_random(histogram()))
