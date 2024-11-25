from hangman_functions import *
from typing import List
from timer import *
from hangman_game_class import *
from hangman_points import  *

game = hangman_game('word_list.txt', 7) # Takes word.txt files and number of guesses as parameters
game.display_intro()
game.start_game()
score = points() # Kept consistent, per user. Does not reset after each game.


n = 1 # Variable used to break out of loop when game ends.

while n != 0:
        
        while not game.check_game_completion(): # Game runs as long as it is it isn't finished.
            
            score.show_points() # Show points after each game (they don't reset as of now)
            game.display_game_progress() 

    
            user_response = input() # User guesses either letter or word.
            user_response = user_response.upper()
    
            # USER INPUTS
            if user_response == 'QUIT': # User manually ends game by quitting
                print("Quitting Game!")
                n = 0

            elif len(user_response) > 1: # User is guessing a word.
                if game.guess_word(user_response): # True or False on whether word was right
                    game.stop_timer()
                    game.display_win_message()
                    game.set_game_completion()
                    score.add_point()

                else: #Word wrong and removes guess.
                    game.subtract_guess()
                    
            elif len(user_response) == 1: # User is guessing a letter.
                game.guess_letter(user_response) #Checks whether letter is right or not.
                    
        
        # GAME PROGRESS (Lives & Word Progress)
            if game.get_guesses() == 0: # User loses when all lives are lost
                game.stop_timer()
                game.display_lose_message()
                game.set_game_completion()
                if score.get_points() > 0:
                    score.remove_point()
                    
            elif game.guess_letter_check(): # User wins when all letters are filled.
                game.stop_timer
                game.display_win_message()
                game.set_game_completion()
                score.add_point()
            
        # ASK USER TO REPLAY
            if game.check_game_completion(): # Ask user to play again
               game.display_ask_replay_game()
               user_response = input()
               user_response = user_response.upper()
               if user_response != "NO": # User replays game and new object made.
                   game = hangman_game('word_list.txt', 7)
                   game.start_game()
               else:
                   print("Quitting Game!")
            
    
        
            



            

# OLD CODE

"""
word_list = create_word_set('word_list.txt')
word_to_guess = choose_random_word(word_list)
user_guess = ""
guesses_left = 7 # Essentially "lives" you have when you fail a guess.
list_of_letters_used = []
is_game_over = False # Used to ask User if they want to play again.

# Create list where blank spaces filled up by guesses
word_progress = [] 
for i in range(len(word_to_guess)):
    word_progress.append("_")
    

# Stop watch object to time game.
timer = stopwatch()

# Create list to compare index of word to guess.
word_to_guess_list = list(word_to_guess)
#print(word_to_guess_list) #Debugging to see if word is accurate
print()


n = 1 # Variable used to break out of loop when game ends

while n != 0:
    
    timer.start() # Game timer runs
    
    print(word_progress)
    if len(list_of_letters_used) > 0:
        print(f"Letters used: {list_of_letters_used}")
    #print("The word is " + word_to_guess) #Debugging to see if word is accurate
    print()
    
    print(f"You have {guesses_left} lives left!")
    print("Would you like to guess a letter or a word?")
    print("Type a word to guess a word. Type only a letter to guess a letter.")
    print("*" * 66)
    print()
    
    user_response = input() # Determines if User is guessing word or letter.
    user_response = user_response.upper() # Doesn't matter if lower-case or not.
    print()

    if user_response == "QUIT": # User quits game
        print("Quitting Game!")
        n = 0
    
    elif len(user_response) > 1 : # User is guessing a word.
        guess_state = user_guess_word(user_response, word_to_guess) # Boolean Value for Guess.
        if guess_state == True:
            print("You got the word right! You win!")
            timer.stop()
            print(f"The game lasted for: {timer.display_time()}")
            print()
            is_game_over = True
        else:
            print("Wrong answer!")
            print()
            guesses_left -= 1
    
    elif len(user_response) <= 1: # User is guessing a letter
        guess_state = user_guess_letter(user_response, word_to_guess)
        list_of_letters_used.append(user_response.upper())
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
        print("The man has been hung! You lose! :(")
        print(f"The word was {word_to_guess}.")
        print("You ran out of lives!")
        timer.stop()
        print(f"The game lasted for: {timer.display_time()}")
        is_game_over = True
    
    # User wins if they guess all the letters correctly.
    elif word_progress == word_to_guess_list:
        print(f"The word was {word_to_guess} You win! :)")
        print(f"You had {guesses_left} lives left!")
        timer.stop()
        print(f"The game lasted for: {timer.display_time()}")
        is_game_over = True
    
    if is_game_over and n != 0: # Detects whether or not the game ended and asks User if they'd like to replay.
        print("*" * 29)
        print("Would you like to play again?")
        print("Type Yes to replay!")
        user_response = input()
        print("*" * 29)
        print()

        if user_response.upper() in ["YES", "Y"]: # Game replays
            is_game_over = False 
            timer.reset()
            word_to_guess = choose_random_word(word_list) # Choose new word
            word_to_guess_list = list(word_to_guess)
            list_of_letters_used = []
            word_progress = [] 
            guesses_left = 7
            word_progress = [] 
            for i in range(len(word_to_guess)):
                word_progress.append("_")
             
        else:
            n = 0 # Game Ends

             

            
"""       
    
    
        
    
    
          

                    
        
        
            
    
