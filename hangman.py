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
    #counting the letters in the word to keep tracked of which ones have been guessed
    word_letters = set(word) 
    #calling predetermined uppercase letters in the english alpahbet
    alphabet = set(string.ascii_uppercase) 
    #keeping track of what letters the user has already guessed 
    guessed_letters = set() 

    lives = 10

    #while loop using AND logical operation 
    while len(word_letters) > 0 and lives > 0:
        #tell user what letters have already been used
        #.join joins the items from a list together ['a', 'b', 'c'] to 'a, b, c'
        print('You have', lives, 'lives and have used letters:', ' '.join(guessed_letters))
        #tell user what current word is but hiding un guessed letters
        # if letter is in guessed letters and is in the word display
        #else display a dash to hide the un guessed letters in word
        word_list = [letter 
        if letter in guessed_letters 
        else '-' for letter in word]
        print('Current word: ', " ".join(word_list))

    #get user input
    #promting user to type in a letter, putting all letters to uppercase so there are no problems with lower or uppper in python
        user_letter_choice = input('Guess a letter: ').upper() 

    #if statement for if letter is a valid letter in the alphabet that hasent been used yet
        if user_letter_choice in alphabet - guessed_letters:
        #add to used letters set
            guessed_letters.add(user_letter_choice)
        #if guessed letter is in the word, remove a letter
            if user_letter_choice in word_letters:
                word_letters.remove(user_letter_choice)
                print(" ")
            # if letter guessed is not in word, take away a life
            else: 
                lives = lives - 1
                print('Letter', user_letter_choice, ' is not in word')
             #if the letter user chooses in already in the quessed letters list, print a try again message
        elif user_letter_choice in guessed_letters:
            print("This letter has already been used. Please try again")
        else: 
            print('Invalid character.Try again')

#while loop is exited when all letters is guessed or all lives are gone
    if lives == 0:
        print('You died, sorry try again. The word was', word)
    else: 
        print('Congrates you guessed the word right!', word)


if __name__ == '__main__':
    hangman()