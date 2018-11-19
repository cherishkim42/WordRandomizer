# To run in terminal, type: "python3" + "rearrange.py" + several words to be rearranged
import random
import sys

def rearrange_words():
    user_words = sys.argv[1:] #All arguments from terminal EXCEPT [0] = file name
    words = [] #Create empty array
    while len(user_words) is not 0:
        rando = random.randrange(0, len(user_words)) #Because randrange is for indexed lists, no need for the "-1"
        #Following line swaps positions at the two indices
        user_words[rando], user_words[-1] = user_words[-1], user_words[rando] #array[-1] shorthand for len(array)-1
        words.append(user_words[-1])
        # print(words) #quick test
        user_words.pop(-1) #Removes user_words[-1] since we appended it to words[]
        # print(user_words) #quick test
        show = " ".join(words)
    return show

if __name__ == '__main__':
    print(rearrange_words())
