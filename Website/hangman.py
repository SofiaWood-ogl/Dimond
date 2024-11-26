from hangman_functions import *
from typing import List
from stopwatch import *
from hangman_game_class import *


game = hangman_game('word_list.txt', 7) # Takes word.txt files and number of guesses as parameters
game.display_intro()
game.start_game()
#score = points() # Kept consistent, per user. Does not reset after each game.


n = 1 # Variable used to break out of loop when game ends.

while n != 0:
        
        while not game.check_game_completion(): # Game runs as long as it is it isn't finished.
            
            #score.show_points() # Show points after each game (they don't reset as of now)
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
                    #score.add_point()

                else: #Word wrong and removes guess.
                    game.subtract_guess()
                    
            elif len(user_response) == 1: # User is guessing a letter.
                game.guess_letter(user_response) #Checks whether letter is right or not.
                    
        
        # GAME PROGRESS (Lives & Word Progress)
            if game.get_guesses() == 0: # User loses when all lives are lost
                game.stop_timer()
                game.display_lose_message()
                game.set_game_completion()
               # if score.get_points() > 0:
                   # score.remove_point()
                    
            elif game.guess_letter_check(): # User wins when all letters are filled.
                game.stop_timer
                game.display_win_message()
                game.set_game_completion()
                #score.add_point()
            
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
