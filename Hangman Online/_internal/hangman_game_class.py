from hangman_functions import *
from timer import *
import random
import builtins
from ctypes.wintypes import WORD
from leaderboard import Player, Leaderboard

class hangman_game: 

# GAME ATTRIBUTES
    def __init__(self, word_set, guesses_left, player_name):
        self.word_list = create_word_set(word_set) # Specific set of words the game pulls from and creates list.
        self.word_to_guess = choose_random_word(self.word_list) # Chooses word out of list.
        self.guesses_left = guesses_left # Number of lives left.
        self.letters_used = [] #Shows user what letters they used to guess for the game.
        self.game_timer = stopwatch() # Timer for the game
        self.word_progress = create_blank_guess_list(self.word_to_guess) # Gives user visual on progress of word.
        self.game_finished = False
        self.player = Player(player_name) # Created player object to store name, score, time
        self.leaderboard = Leaderboard() #Add leaderboard instance

# GAME GUI (WHAT USER SEES)
    def display_intro(self): # Shows at the start of the program.
        print("Hello! Welcome to Hangman! Guess the letters to reveal the hidden word!")
        print("You can guess the word in full, however, the correct letters will not show!")
        print()
        print("Let's get started shall we?")
        print("Type anything to start!")
        print("P.S. You can quit the game any time by typing quit")
        print("*" * 41)
    
    def display_win_message(self): # What user sees when they win.
        print(f"The word was {self.word_to_guess} You win! :)")
        print(f"You had {self.guesses_left} lives left!")
        print(f"The game lasted for: {self.game_timer.display_time()}")
        print()

    def display_lose_message(self): # What user sees when they lose
        print(f"The word was {self.word_to_guess} You lose! :(")
        print(f"You have {self.guesses_left} lives left!")
        print(f"The game lasted for: {self.game_timer.display_time()}")
        print()
    
    def display_game_progress(self): # Shows User the progress of the word guessed as well as lives.
        # print(self.word_to_guess)  # Debugging to make sure word matches word_progress
        print(f"{self.word_progress}")
        print(f"Letters used: {self.letters_used}")
        print()
        print(f"You have {self.guesses_left} lives left!")
        print("Would you like to guess a letter or a word?")
        print("Type a word to guess a word. Type only a letter to guess a letter.")
        print("*" * 66)
        print()
    
    def display_ask_replay_game(self):
        print("Do you want to play again?")
        print("Type NO to quit.")
        print("Type Anything to replay!")
        print("*" * 24)     

# ALTER GAME DATA (Guesses left, timer, game_completion)
    def start_game(self): # Initiates the game as it shows the User the blank word and starts timer.
        self.game_timer.start() # Starts timer.
    
    def subtract_guess(self): # Subtracts life by 1
        self.guesses_left -= 1
    
    def stop_timer(self): # Stops game timer.
        self.game_timer.stop()
    
    def restart_timer(self): # Sets game timer to 0
        self.game_timer.reset()
    
    def set_game_completion(self):
        self.game_finished = True
        
    def set_game_unfinished(self):
        self.game_finished = False  
        
    def set_score(self, score):  # Set the score for the player based on remaining guesses
        score = self.guesses_left * 10 # Each remaining guess gives 10 points 
        self.player.set_score(score)   # Set the score for the player

    def set_time(self):
        self.player.set_time(self.game_timer.get_time()) #Set the time for the player when the game ends
        
    def stop_game(self):
        self.stop_timer() # Stopping the timer once the game ends
        self.set_time()
        self.set_score(self.guesses_left)# Set the score for the player
        self.leaderboard.add_players([self.player]) # Add player to the leaderboard
        self.display_leaderboard()

    def display_leaderboard(self):
        self.leaderboard.display_leaderboard()  # Display the leaderboard at the end of each game


    def reset_game(self, player_name):
        self.game_timer.reset()
        self.guesses_left = 7  # Reset the number of guesses for the next game
        self.letters_used = []
        self.word_progress = create_blank_guess_list(self.word_to_guess)
        self.game_finished = False
        self.player = Player(player_name)  # Reset player info
    
# GAME OUTPUTS (True or False, Checks guesses)
    def check_game_completion(self): # Returns true or false value if game is done or not.
        return self.game_finished # True if Game is finished, false if not.
            
    def guess_word(self, user_guess): # When user decides to guess word instead of letter. Returns false or true.
        guess_state = user_guess_word(user_guess, self.word_to_guess) # Checks if word matches word to guess.
        if guess_state: # Guess correct
            return True
        else:
            return False
            
    def guess_letter(self, user_guess): # When user decides to guess letter instead of a word.
        word_to_guess_list = list(self.word_to_guess) # Turns word to guess into a list for comparison.
        guess_state = user_guess_letter(user_guess, self.word_to_guess) # Check if letter is in word.
        self.letters_used.append(user_guess.upper()) # Add letter to letters used list.
        if guess_state: # Guess is right, will replace blank space with word.
            print("You guessed the right letter!")
            print()
            for i in range(len(self.word_to_guess)): 
                if word_to_guess_list[i] == user_guess.upper():
                    self.word_progress[i] = user_guess.upper()
        else: # Guess wrong and game continues.
            print("Wrong letter!")
            print()
            self.guesses_left -= 1
    
    def guess_letter_check(self): # True or False to see if all letters are filled
        word_to_guess_list = list(self.word_to_guess) # Turns word to guess into a list for comparison.
        if self.word_progress == word_to_guess_list:
            return True
        else:
            return False
    
    def get_guesses(self): # Returns number of lives left for comparison.
        return self.guesses_left
    
    """ FOR ITERATION 4
    def get_remaining_spaces(self): # Returns number of empty spaces left when guessing letters.
        i = 0
        for '_' in self.word_progress:
            i += 1
        return i
    """  