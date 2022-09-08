#import the array 'words' and import the data
from words import words
import random

#define a function to get valid words without extra characters in them
def valid_word(words):
    word = random.choice(words) #randomly chooses from a list
    # make a while loop for if there is a space or dash in the word, keep choosing for another word
    #loop will keep going until a word with spaces or dashes is found
    while '-' in word or " " in word:
        #word = a random word chosen from the words array
         word = random.choice(words)

    #return the word in uppercase
    return word.upper()

