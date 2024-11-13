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

class TestHangmanFunctions(unittest.TestCase):

    def setUp(self):
        # Setting up a testing sample for the test cases
        self.word_list = ['WORD', 'DOG', 'CAT']
        self.word_to_guess = 'DOG'

    def test_create_word_set(self):
        # Test the word set creation from a file (mocking the file reading if needed)
        word_set = create_word_set('word_list.txt')
        self.assertGreater(len(word_set), 0, "Word set should not be empty.")
        self.assertIn('DOG', word_set, "Expected word 'DOG' to be in the word set.")
        self.assertIn('CAT', word_set, "Expected word 'CAT' to be in the word set.")

    def test_choose_random_word(self):
        # Test the random word selection
        random_word = choose_random_word(self.word_list)
        self.assertIn(random_word, self.word_list, "Random word should be from the word list.")

    def test_user_guess_word_correct(self):
        # Test that correct word guess returns True
        result = user_guess_word('DOG', self.word_to_guess)
        self.assertTrue(result, "Guessing the word 'DOG' should return True.")

    def test_user_guess_word_incorrect(self):
        # Test that incorrect word guess returns False
        result = user_guess_word('CAT', self.word_to_guess)
        self.assertFalse(result, "Guessing the word 'CAT' should return False.")

    def test_user_guess_letter_correct(self):
        # Test that a correct letter guess returns True
        result = user_guess_letter('D', self.word_to_guess)
        self.assertTrue(result, "Guessing the letter 'D' should return True.")

    def test_user_guess_letter_incorrect(self):
        # Test that an incorrect letter guess returns False
        result = user_guess_letter('Z', self.word_to_guess)
        self.assertFalse(result, "Guessing the letter 'Z' should return False.")

    def test_add_letters_to_guess_list(self):
        # Test that guessed letters are added to the guess list
        letters_guessed = []
        updated_list = add_letters_to_guess_list('D', letters_guessed)
        self.assertIn('D', updated_list, "Letter 'D' should be added to the guessed list.")

class TestStopwatch(unittest.TestCase):

    def setUp(self):
        # Setting up the stopwatch instance for the test cases
        self.timer = stopwatch()

    def test_start(self):
        self.timer.start()
        self.assertTrue(self.timer.running, "Timer should be running after start.")

    def test_stop(self):
        self.timer.start()
        self.timer.stop()
        self.assertFalse(self.timer.running, "Timer should be stopped after stop.")

    def test_reset(self):
        self.timer.start()
        self.timer.stop()
        self.timer.reset()
        self.assertFalse(self.timer.running, "Timer should not be running after reset.")
        self.assertEqual(self.timer.get_time(), 0, "Timer should be reset to 0.")

    def test_display_time(self):
        self.timer.start()
        self.timer.stop()
        elapsed_time = self.timer.display_time()
        self.assertIn(':', elapsed_time, "The time should be displayed with ':'.")

class TestHangmanGameClass(unittest.TestCase):
    
    def setUp(self):
        # Set up a new hangman game with a word list and 7 guesses
        self.game = hangman_game(['DOG', 'CAT', 'BEACH'], 7)

    def test_start_game(self):
        # Test starting the game
        self.game.start_game()
        self.assertEqual(self.game.guesses_left, 7, "Initial guesses should be set to 7.")
        self.assertFalse(self.game.game_finished, "Game should not be finished when starting.")
        self.assertTrue(len(self.game.word_progress) > 0, "Word progress should be initialized.")

    def test_guess_word_correct(self):
        # Test guessing the correct word
        self.game.word_to_guess = 'DOG'
        result = self.game.guess_word('DOG')
        self.assertTrue(result, "Correct word guess should return True.")
        self.assertTrue(self.game.game_finished, "Game should be finished after correct word guess.")

    def test_guess_word_incorrect(self):
        # Test guessing the incorrect word
        self.game.word_to_guess = 'DOG'
        initial_guesses = self.game.guesses_left
        result = self.game.guess_word('CAT')
        self.assertFalse(result, "Incorrect word guess should return False.")
        self.assertEqual(self.game.guesses_left, initial_guesses - 1, "Guesses left should decrease after incorrect guess.")

    def test_guess_letter_correct(self):
        # Test guessing the correct letter
        self.game.word_to_guess = 'DOG'
        result = self.game.guess_letter('D')
        self.assertTrue(result, "Correct letter guess should return True.")
        self.assertIn('D', self.game.word_progress, "The guessed letter should be updated in word progress.")

    def test_guess_letter_incorrect(self):
        # Test guessing the incorrect letter
        self.game.word_to_guess = 'DOG'
        initial_guesses = self.game.guesses_left
        result = self.game.guess_letter('Z')
        self.assertFalse(result, "Incorrect letter guess should return False.")
        self.assertEqual(self.game.guesses_left, initial_guesses - 1, "Guesses left should decrease after incorrect guess.")

    def test_set_game_completion(self):
        # Test that the game is completed
        self.game.set_game_completion()
        self.assertTrue(self.game.game_finished, "Game should be marked as completed.")

    def test_get_guesses(self):
        # Test that get_guesses returns the correct number of guesses left
        self.assertEqual(self.game.get_guesses(), 7, "Initial guesses should be 7.")

    def test_guess_letter_check_complete_word(self):
        # Test the game recognizing when the word is fully guessed
        self.game.word_to_guess = 'DOG'
        self.game.word_progress = ['D', 'O', 'G']
        self.assertTrue(self.game.guess_letter_check(), "Game should recognize when the word is complete.")

    def test_display_game_progress(self):
        # Test displaying the game progress
        self.game.word_to_guess = 'DOG'
        self.game.word_progress = ['D', '_', '_']
        output = self.game.display_game_progress()
        self.assertIn('D _ _', output, "Displayed progress should show the correct guessed letters.")

    def test_timer_integration(self):
        # Test integrating the timer in the hangman game
        self.game.start_game()
        self.assertTrue(self.game.game_timer.running, "Timer should be running after starting the game.")
        self.game.stop_timer()
        self.assertFalse(self.game.game_timer.running, "Timer should be stopped after stopping the game.")
        elapsed_time = self.game.game_timer.display_time()
        self.assertIn(':', elapsed_time, "Elapsed time should have ':' in the format.")

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
