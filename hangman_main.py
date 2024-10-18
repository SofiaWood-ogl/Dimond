from hangman_functions import *
from typing import List

print("Hello! Welcome to Hangman! Guess the letters to reveal the hidden word!")
print("You can guess the word in full, however, the correct letters will not show!")
print()
print("Let's get started shall we?")
print("P.S. You can quit the game by typing quit")
print("*" * 41)
print(" ")

word_list = create_word_set('word_list.txt')
word_to_guess = choose_random_word(word_list)
user_guess = ""
guesses_left = 7 # Essentially "lives" you have when you fail a guess.
list_of_words_used = []

# Create list where blank spaces filled up by guesses
word_progress = [] 
for i in range(len(word_to_guess)):
    word_progress.append("_")

# Create list to compare index of word to guess.
word_to_guess_list = list(word_to_guess)
#print(word_to_guess_list) #Debugging to see if word is accurate
print()


n = 1 # Variable used to break out of loop when game ends

while n != 0:
    
    
    print(word_progress)
    if len(list_of_words_used) > 0:
        print(f"Letters used: {list_of_words_used}")
    #print("The word is " + word_to_guess) #Debugging to see if word is accurate
    print()
    
    print(f"You have {guesses_left} lives left!")
    print("Would you like to guess a letter or a word?")
    print("Type a word to guess a word. Type only a letter to guess a letter.")
    print("*" * 66)
    print()
    
    user_response = input() # Determines if User is guessing word or letter.
    user_response = user_response.upper() # Doesn't matter if lowercase or not.

    if user_response == "QUIT": # User quits game
        print("Quitting Game!")
        n = 0
    
    elif len(user_response) > 1 : # User is guessing a word.
        guess_state = user_guess_word(user_response, word_to_guess) # Boolean Value for Guess.
        if guess_state == True:
            print("You got the word right! You win!")
            print()
            n = 0
        else:
            print("Wrong answer!")
            print()
            guesses_left -= 1
    
    elif len(user_response) <= 1: # User is guessing a letter
        guess_state = user_guess_letter(user_response, word_to_guess)
        list_of_words_used.append(user_response.upper())
        if guess_state == True: # Guess is right, will replace blank space with word.
            print("You guessed the right letter!")
            print()
            for i in range(len(word_to_guess)):
                if word_to_guess_list[i] == user_response.upper():
                    word_progress[i] = user_response.upper()
        else:
            print("Wrong letter!")
            print()
            guesses_left -= 1
            
    # User loses if they have no more lives left.
    if guesses_left == 0:
        n = 0
        print("The man has been hung! You lose! :(")
        print(f"The word was {word_to_guess}.")
        print("You ran out of lives!")
    
    # User wins if they guess all the letters correctly.
    elif word_progress == word_to_guess_list:
        n = 0
        print(f"The word was {word_to_guess} You win! :)")
        print(f"You had {guesses_left} lives left!")
        
    
    
          

                    
        
        
            
    