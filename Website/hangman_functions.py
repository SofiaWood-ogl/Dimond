import random
import builtins
from ctypes.wintypes import WORD

def create_word_set(file_name): # Read list & Create List for game """
    word_list = [] 
    with open(file_name, 'r') as file:
        file_content = file.readlines() # Read File & Obtain list of lines
        for i in range(len(file_content)): # Goes through each line to add to list
            word_list.append(file_content[i].strip()) # Removes /n after each word
    
    return word_list

def choose_random_word(word_list): # Chooses random word to guess out of word list.
    word = random.choice(word_list)
    return word.upper()

def add_letters_to_guess_list(user_input, letters_guessed): # Adds list of letters guessed by User
     user_guess = user_input.upper()
     letters_guessed.append(user_guess)
     return letters_guessed

def user_guess_word(user_input, word_to_guess): # See if guessed word matches word to guess
    user_guess = user_input.upper() # Make it so that caps don't matter in guess.
    word_to_guess_uppercase = word_to_guess.upper()
    if user_guess == word_to_guess_uppercase:
        return True
    else:                            # Returns Boolean Value
        return False
    
def user_guess_letter(user_input, word_to_guess): # See if guessed word matches word to guess
    user_guess = user_input.upper() # Make it so that caps don't matter in guess.
    word_to_guess_uppercase = word_to_guess.upper()
    if user_guess in word_to_guess_uppercase:
        return True
    else:
        return False
    
def create_blank_guess_list(word_to_guess): # Creates visual for word progress
    word_progress = [] 
    for i in range(len(word_to_guess)):
        word_progress.append("_")
    return word_progress
