import unittest
from hangman_functions import (
    create_word_set,
    choose_random_word,
    user_guess_word,
    user_guess_letter,
    add_letters_to_guess_list
)
from timer import stopwatch
from hangman_game_class import hangman_game

# Test cases for the functions in hangman_functions.py
class TestHangmanFunctions(unittest.TestCase):

    def setUp(self):
        #setting up a testing sample for the test cases
        self.word_list = ['WORD','DOG','CAT']
        self.word_to_guess = 'DOG'

    def test_create_word_set(self):
        # Tests to ensure the word created is from the word file
        word_set = create_word_set('word_list.txt')
        self.assertGreater(len(word_set),0, "Word set should not be empty")
        self.assertIn('DOG', word_set, "Expected word 'DOG to be in the word set.")
        self.assertIn('CAT', word_set, "Expected word 'CAT' to be in the word set.")
    
    def test_choose_random_word(self):
        #Tests that a random word can be chosen from the word list file.
        random_word = choose_random_word(self.word_list)
        self.assertIn(random_word, self.word_list, "Random word should be from the word list.")

    def test_user_guess_word_correct(self):
        #Tests that when the word is guessed correct, it would return true
        result = user_guess_word('DOG', self.word_to_guess)
        self.assertTrue(result, "Guessing the word 'DOG' should return True.")

    def test_user_guess_word_incorrect(self):
        # Tests that when the word is guessed incorrectly, it would return false.
        result = user_guess_word('CAT',self. word_to_guess)
        self.assertFalse(result, "Guessing the word 'CAT' should return False.")

    def test_user_guess_letter_correct(self):
        #Tests that when a correct letter is guessed, True should be returned
        result = user_guess_letter('D', self.word_to_guess)
        self.assertTrue(result, "Guessing the letter 'D' should return True.")

    def test_user_guess_letter_incorrect(self):
        #Tests that when an incorrect letter is guessed, False should be returned
        result = user_guess_letter("Z", self.word_to_guess)
        self.assertFalse(result, "Guessing the letter'Z' should return False.")

    def test_add_letters_to_guess_list(self):
        #Tests that the letters guessed are added to the guessed list
        letters_guessed = []
        updated_list = add_letters_to_guess_list('D', letters_guessed)
        self.assertIn('D', updated_list, "Letter 'D' should be added to the guessed list.")

class TestStopWatch(unittest.TestCase):
    # Unit Tests for the stopwatch class

    def setUp(self):
    #Setting up the stopwatch instance for the test cases
        self.timer = stopwatch()

    def test_start(self):
    # Tests that the timer was started correctly
        self.timer.start()
        self.assertTrue(self.timer.running, "Timer should be running correctly.")
    
    def test_stop(self):
    #Tests that the timer stops correctly
        self.timer.start()
        self.timer.stop()
        self.assertFalse(self.timer.running, "Timer should not be running.")

    def test_reset(self):
    # Tests that the timer has correctly resetted
        self.timer.start()
        self.timer.stop()
        self.timer.reset()
        self.assertFalse(self.timer.running, " Timer is not running after being reset.")
        self.assertEqual(self.timer.get_time(), 0, "Timer should be rest to 0.")

    def test_display_time(self):
    # Tests that timer is correctly displayed as a formatted string.
        self.timer.start()
        self.timer.stop()
        elapsed_time = self.timer.display_time()
        self.assertIn(':', elapsed_time, " The time being displayed should include ':'.")

class TestHangmanGameClass(unittest.TestCase):
    # Unit Tests for the Hangman Game Class

    def setUp(self):
    # Setting up a new instance of hangman_game that includes a word list and 7 guesses
        self.game = hangman_game(['DOG','CAT', 'BEACH'],7)

    def test_start_game(self):
    #Starting the game and cheching if the game properties are correctly applied
        self.game.start_game()
        self.assertEqual(self.game.guesses_left, 7, "The number of guesses have been initialized to (7).")
        self.assertFalse(self.game.game_completed, "Game should not have been completed at the start.")
        self.assertTrue(len(self.game.word)progress) > 0, "Word progress has been initialized.")
        
    def test_guess_word_correct(self):
    # Setting a word to be guessed and simulating that the word was guessed correctly. 
    # This tests that the game was checked as a winning round
        self.game.word_to_guess = 'DOG' 
        result = self.game.guess_word('DOG')
        self.assertTrue(result, "Correct word guess should return True.")
        self.assertTrue(self.game.game_complete, "Word guessed correctly so game must be marked as completed")
        
     def test_guess_word_incorrect(self):
    # Setting a word to be guessed and simulating how it would look like if the word was guessed incorrectly
     # This test ensures that the game was updated to indicate an incorrect guess
        self.game.word_to_guess = 'DOG'
        initial_guesses = self.game.guesses_left
        result = self.game.guess_word('CAT')  
        self.assertFalse(result, "Incorrect word guess should return False.")
        self.assertEqual(self.game.guesses_left, initial_guesses - 1, "After a wrong guess, guesses left should have decreased.")

    def test_guess_letter_correct(self):
    # Setting a word to be guessed and simulating that a letter was guessed correctly
    # Test checks that the word progress is correctly updated
        self.game.word_to_guess = 'DOG'
        result = self.game.guess_letter('D') 
        self.assertTrue(result, "Correct letter guess should return True.")
        self.assertIn('D', self.game.word_progress, "The word progress should contain the correctly guessed letter.")

     def test_guess_letter_incorrect(self):
    # Setting a word to be guessed and simulating that letter guess was incorrect.
    # Tests that the number of guesses left decreases accordingly
        self.game.word_to_guess = 'DOG'
        initial_guesses = self.game.guesses_left
        result = self.game.guess_letter('Z')  
        self.assertFalse(result, "Incorrect letter guess should return False.")
        self.assertEqual(self.game.guesses_left, initial_guesses - 1, "Number of guesses left should have decreased after wrong letter guess.")

    def test_set_game_completion(self):
    # This tests ensures that the game is marked as completed 
    # Tests ensures that the game status game_complete is updated
        self.game.set_game_completion()
        self.assertTrue(self.game.game_complete, "Game should be marked as complete.")

    def test_get_guesses(self):
    # This tests checks that the get_guesses method correctly returns the initial number of quesses
        self.assertEqual(self.game.get_guesses(), 7, "Initial guesses should match the set value (7).")

    def test_guess_letter_check_complete_word(self):
    # Setting up the game with a fully guessed word to check if the game can recognize a win
        self.game.word_to_guess = 'DOG'
        self.game.word_progress = list('DOG')  
        self.assertTrue(self.game.guess_letter_check(), "If the word is complete, guess_letter_check should return True.")
        self.assertTrue(self.game.game_complete, "If the word is fully guessed, the game should be marked as complete guessed.")

    def test_display_game_progress(self):
    # Checks that the correct game status is properly displayed and outputted 
        self.game.word_to_guess = 'DOG'
        self.game.word_progress = ['D', '_', '_']  
        output = self.game.display_game_progress() 
        self.assertIn('D _ _', output, "The displayed progress should show a partially guessed word.")
    
    def test_timer_integration(self):
    # Tests that the start, stop, and display timer methods in hangman_game class work as expected
        self.game.start_timer()  
        self.assertTrue(self.game.timer.running, "The timer should be running after starting the game.")
        self.game.stop_timer()  
        self.assertFalse(self.game.timer.running, "The timer should not be running after stopping the game.") 
        elapsed_time = self.game.timer.display_time() 
        self.assertIn(':', elapsed_time, "Displayed time format should contain ':'.")

if __name__ == '__main__':
    unittest.main()


# Old code Below
'''
import unittest
import time
from hangman_functions import (
    create_word_set,
    choose_random_word,
    user_guess_word,
    user_guess_letter,
    add_letters_to_guess_list
)

from timer import stopwatch

class TestHangmanFunctions(unittest.TestCase):
    #Unit tests for the hangman Functions

    def setUp(self):
        #setting up a testing sample for the test cases
        self.word_list = ['WORD','DOG','CAT']
        self.word_to_guess = 'DOG'

    def test_create_word_set(self):
        # Tests to ensure the word created is from the word file
        word_set = create_word_set('word_list.txt')
        self.assertGreater(len(word_set),0, "Word set should not be empty")
        self.assertIn('DOG', word_set, "Expected word 'DOG to be in the word set.")
        self.assertIn('CAT', word_set, "Expected word 'CAT' to be in the word set.")
    
    def test_choose_random_word(self):
        #Tests that a random word can be chosen from the word list file.
        random_word = choose_random_word(self.word_list)
        self.assertIn(random_word, self.word_list, "Random word should be from the word list.")

    def test_user_guess_word_correct(self):
        #Tests that when the word is guessed correct, it would return true
        result = user_guess_word('DOG', self.word_to_guess)
        self.assertTrue(result, "Guessing the word 'DOG' should return True.")

    def test_user_guess_word_incorrect(self):
        # Tests that when the word is guessed incorrectly, it would return false.
        result = user_guess_word('CAT',self. word_to_guess)
        self.assertFalse(result, "Guessing the word 'CAT' should return False.")

    def test_user_guess_letter_correct(self):
        #Tests that when a correct letter is guessed, True should be returned
        result = user_guess_letter('D', self.word_to_guess)
        self.assertTrue(result, "Guessing the letter 'D' should return True.")

    def test_user_guess_letter_incorrect(self):
        #Tests that when an incorrect letter is guessed, False should be returned
        result = user_guess_letter("Z", self.word_to_guess)
        self.assertFalse(result, "Guessing the letter'Z' should return False.")

    def test_add_letters_to_guess_list(self):
        #Tests that the letters guessed are added to the guessed list
        letters_guessed = []
        updated_list = add_letters_to_guess_list('D', letters_guessed)
        self.assertIn('D', updated_list, "Letter 'D' should be added to the guessed list.")

class TestStopWatch(unittest.TestCase):
    # Unit Tests for the stopwatch class

    def setUp(self):
    #Setting up the stopwatch instance for the test cases
        self.timer = stopwatch()

    def test_start(self):
    # Tests that the timer was started correctly
        self.timer.start()
        self.assertTrue(self.timer.running, "Timer should be running correctly.")
    
    def test_stop(self):
    #Tests that the timer stops correctly
        self.timer.start()
        self.timer.stop()
        self.assertFalse(self.timer.running, "Timer should not be running.")

    def test_reset(self):
    # Tests that the timer has correctly resetted
        self.timer.start()
        self.timer.stop()
        self.timer.reset()
        self.assertFalse(self.timer.running, " Timer is not running after being reset.")
        self.assertEqual(self.timer.get_time(), 0, "Timer should be rest to 0.")

    def test_display_time(self):
    # Tests that timer is correctly displayed as a formatted string.
        self.timer.start()
        time.sleep(1)
        self.timer.stop()
        elapsed_time = self.timer.display_time()
        self.assertIn(':', elapsed_time, " The time being displayed should include ':'.")

if __name__ == '__main__':
    unittest.main()

'''
