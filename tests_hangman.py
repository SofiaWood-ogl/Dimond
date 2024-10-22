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
