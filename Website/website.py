import re 
from flask import Flask
from flask import render_template
from typing import List
from stopwatch import timer
from points import points
import hangman_game_class
import random
import builtins
from ctypes.wintypes import WORD
with open ('word_list.txt','r')as file:
    wordlist=file.read()

app = Flask(__name__)


def python_funtion():
    # Here you can put any logic you want the button to trigger
    print("Python function was called!")
    return "Function executed successfully!"

@app.route("/")
def home():
    print("This is in home")
    return render_template("hello_there2.html")
   # return "Hello, Flask!"

print("This is in the middle of nothing")

@app.route('/call-function') 
def call_function(): 
    print("This is the button click")
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
    return wordlist
    


@app.route('/run_function')
def run_hangman_game(name=None, guess=7):
    game = run_hangman_game('word_list.txt', 7) # Takes word.txt files and number of guesses as parameters
    game.display_intro()
    game.start_game()
    score = points() #

    n = 1  # Variable used to break out of loop when the game ends.

    while n != 0:
        while not game.check_game_completion():  # Game runs as long as it isn't finished
            game.display_game_progress()

            user_response = input()  # User guesses either letter or word
            user_response = user_response.upper()

            # USER INPUTS
            if user_response == 'QUIT':  # User manually ends game by quitting
                print("Quitting Game!")
                n = 0
            elif len(user_response) > 1:  # User is guessing a word
                if game.guess_word(user_response):
                    game.stop_timer()
                    game.display_win_message()
                    game.set_game_completion()
                    score.add_point()
                else:  # Word wrong and removes a guess
                    game.subtract_guess()
            elif len(user_response) == 1:  # User is guessing a letter
                game.guess_letter(user_response)  # Checks whether the letter is right or not

            # GAME PROGRESS (Lives & Word Progress)
            if game.get_guesses() == 0:  # User loses when all lives are lost
                game.stop_timer()
                game.display_lose_message()
                game.set_game_completion()
                if score.get_points() > 0:
                    score.remove_point()

            elif game.guess_letter_check():  # User wins when all letters are filled
                game.stop_timer()
                game.display_win_message()
                game.set_game_completion()
                score.add_point()

            # ASK USER TO REPLAY
            if game.check_game_completion():  # Ask user to play again
                game.display_ask_replay_game()
                user_response = input()
                user_response = user_response.upper()
                if user_response != "NO":  # User replays game and new object made
                    game = run_hangman_game('word_list.txt', 7)
                    game.start_game()
                else:
                    print("Quitting Game!")
    return run_hangman_game



def result():   
    result = python_funtion()  # Call the Python function when the button is pressed
    return render_template('hello_there2.html', result=result)
    

if __name__ == '__main__':
    app.run(debug=True)
