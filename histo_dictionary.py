# To run in terminal, type: "python3" + "histo_dictionary.py" + file name
import sys

def histogram():
    f = open(sys.argv[1], "r").read().split()
    dict = {} #Creates empty dictionary
    for entry in f: #Time to iterate through the whole shebang!
        if entry in dict: #If dictionary DOES ALREADY contain entry, append +1
            dict[entry] += 1
        else: #If dictionary DOESN'T ALREADY contain entry, create an entry with {entry_word: 1} as {key: value} pair
            dict[entry] = 1
    return dict

if __name__ == '__main__':
    print(histogram())

#Thanks to Sean Glancy, Drake Vorndran, Dylan Finn
