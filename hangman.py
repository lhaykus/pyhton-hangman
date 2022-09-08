#import the array 'words' and import the data
from words import words
import random
import string

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

# funciton to keep track of which letters have been guessed and which are correctly guessed 
def hangman():
    word = valid_word(words)
    word_letters = set(word) #counting the letters in the word to keep tracked of which ones have been guessed
    alphabet = set(string.ascii_uppercase) #calling predetermined uppercase letters in the english alpahbet
    used_letters = set() #keeping track of what letters the user has already guessed 
