import unittest
from hangman_functions import (
    create_word_set,
    choose_random_word,
    add_letters_to_guess_list,
    user_guess_word,
    user_guess_letter,
    create_blank_guess_list
)
from hangman_game_class import hangman_game
from hangman_points import points
from leaderboard import Player, Leaderboard
from timer import stopwatch
from unittest.mock import patch
import random


# Unit tests for functions defined in hangman_functions.py
class TestHangmanFunctions(unittest.TestCase):

    # Test the create_word_set function which reads words from a file and returns a list of words
    def test_create_word_set(self):
        # Mocking the file content
        with patch('builtins.open', unittest.mock.mock_open(read_data='apple\nbanana\ncherry\n')):
            word_list = create_word_set('test_words.txt')
            self.assertEqual(word_list, ['apple', 'banana', 'cherry'])

    # Test the choose_random_word function to ensure it returns a word from the given list
    def test_choose_random_word(self):
        word_list = ['apple', 'banana', 'cherry']
        random_word = choose_random_word(word_list)
        self.assertIn(random_word, word_list)  # The returned word should be in the list

    # Test the add_letters_to_guess_list function to ensure it correctly adds guessed letters
    def test_add_letters_to_guess_list(self):
        letters_guessed = []
        updated_letters = add_letters_to_guess_list('a', letters_guessed)
        self.assertEqual(updated_letters, ['A'])  # Ensures the letter is capitalized

    # Test the user_guess_word function when the guess is correct
    def test_user_guess_word_correct(self):
        result = user_guess_word('apple', 'apple')
        self.assertTrue(result)  # Should return True for correct guess

    # Test the user_guess_word function when the guess is incorrect
    def test_user_guess_word_incorrect(self):
        result = user_guess_word('apple', 'banana')
        self.assertFalse(result)  # Should return False for incorrect guess

    # Test the user_guess_letter function when the guessed letter is correct
    def test_user_guess_letter_correct(self):
        result = user_guess_letter('a', 'apple')
        self.assertTrue(result)  # Should return True if 'a' is in 'apple'

    # Test the user_guess_letter function when the guessed letter is incorrect
    def test_user_guess_letter_incorrect(self):
        result = user_guess_letter('z', 'apple')
        self.assertFalse(result)  # Should return False if 'z' is not in 'apple'

    # Test the create_blank_guess_list function which generates an empty word progress list
    def test_create_blank_guess_list(self):
        word_to_guess = 'apple'
        word_progress = create_blank_guess_list(word_to_guess)
        self.assertEqual(word_progress, ['_', '_', '_', '_', '_'])  # Should return a list of underscores


# Unit tests for the hangman_game class in hangman_game_class.py
class TestHangmanGame(unittest.TestCase):

    # Set up the initial test environment, create an instance of the game
    def setUp(self):
        self.game = hangman_game('test_words.txt', 7, 'TestPlayer')

    # Test that the game is initialized correctly
    def test_game_initialization(self):
        self.assertEqual(self.game.guesses_left, 7)  # The player should start with 7 guesses
        self.assertEqual(len(self.game.word_progress), len(self.game.word_to_guess))  # Blank guess list length should match word length
        self.assertFalse(self.game.game_finished)  # Game should not be finished at initialization

    # Test the win condition of the game: all letters should be guessed
    def test_game_win_condition(self):
        self.game.word_to_guess = 'apple'
        self.game.word_progress = ['A', 'P', 'P', 'L', 'E']
        self.assertTrue(self.game.guess_letter_check())  # Should return True when all letters are filled

    # Test the lose condition of the game: no guesses left
    def test_game_lose_condition(self):
        self.game.guesses_left = 0
        self.game.stop_timer()
        self.assertEqual(self.game.get_guesses(), 0)  # Should have 0 guesses left when the game ends

    # Test guessing a letter correctly
    def test_guess_letter_correct(self):
        self.game.word_to_guess = 'apple'
        self.game.guess_letter('a')  # Guessing letter 'a'
        self.assertIn('A', self.game.word_progress)  # 'A' should be in the word progress
        self.assertEqual(self.game.guesses_left, 7)  # Guesses left should remain the same

    # Test guessing a letter incorrectly
    def test_guess_letter_incorrect(self):
        self.game.word_to_guess = 'apple'
        self.game.guess_letter('z')  # Guessing letter 'z', which is not in the word
        self.assertEqual(self.game.guesses_left, 6)  # Guesses left should decrease

    # Test guessing the whole word correctly
    def test_guess_word_correct(self):
        result = self.game.guess_word('apple')
        self.assertTrue(result)  # Should return True for correct word guess

    # Test guessing the whole word incorrectly
    def test_guess_word_incorrect(self):
        result = self.game.guess_word('banana')
        self.assertFalse(result)  # Should return False for incorrect word guess

    # Test setting the score based on remaining guesses
    def test_set_score(self):
        self.game.set_score(5)  # Assuming 5 guesses left
        self.assertEqual(self.game.player.get_score(), 50)  # Score should be 50 (5 guesses * 10 points each)

    # Test the stop_game method, ensuring it stops the timer and displays the leaderboard
    def test_stop_game(self):
        with patch.object(self.game, 'display_leaderboard') as mock_display:
            self.game.stop_game()
            mock_display.assert_called_once()  # Leaderboard should be displayed once game stops


# Unit tests for the points class in hangman_points.py
class TestPoints(unittest.TestCase):

    def setUp(self):
        self.points = points()

    # Test adding a point to the score
    def test_add_point(self):
        self.points.add_point()
        self.assertEqual(self.points.get_points(), 1)  # Score should be 1 after adding a point

    # Test removing a point from the score
    def test_remove_point(self):
        self.points.add_point()
        self.points.remove_point()
        self.assertEqual(self.points.get_points(), 0)  # Score should return to 0 after removing a point

    # Test resetting the score to 0
    def test_reset_point(self):
        self.points.add_point()
        self.points.reset_point()
        self.assertEqual(self.points.get_points(), 0)  # Score should be reset to 0

    # Test showing the current score
    def test_show_points(self):
        with patch('builtins.print') as mock_print:
            self.points.add_point()
            self.points.show_points()
            mock_print.assert_called_with('Your score is: 1.')  # Print statement should show score as 1


# Unit tests for the leaderboard class in leaderboard.py
class TestLeaderboard(unittest.TestCase):

    def setUp(self):
        self.player1 = Player('Player1')
        self.player2 = Player('Player2')
        self.leaderboard = Leaderboard()

    # Test adding players to the leaderboard
    def test_add_players(self):
        self.leaderboard.add_players([self.player1, self.player2])
        self.assertEqual(len(self.leaderboard.players), 2)  # Should contain two players

    # Test updating a player's score in the leaderboard
    def test_update_score(self):
        self.leaderboard.add_players([self.player1])
        self.leaderboard.update_score('Player1', 10)
        self.assertEqual(self.player1.get_score(), 10)  # Player's score should be updated to 10

    # Test updating a player's time in the leaderboard
    def test_update_time(self):
        self.leaderboard.add_players([self.player1])
        self.leaderboard.update_time('Player1', 120)
        self.assertEqual(self.player1.get_time(), 120)  # Player's time should be updated to 120 seconds

    # Test sorting the leaderboard by score and time
    def test_sort_leaderboard(self):
        self.player1.set_score(10)
        self.player2.set_score(20)
        self.leaderboard.add_players([self.player1, self.player2])
        sorted_leaderboard = self.leaderboard.get_leaderboard()
        self.assertEqual(sorted_leaderboard[0][0], 'Player2')  # Player2 should be ranked first due to higher score

    # Test displaying the leaderboard
    def test_display_leaderboard(self):
        self.leaderboard.add_players([self.player1, self.player2])
        with patch('builtins.print') as mock_print:
            self.leaderboard.display_leaderboard()
            mock_print.assert_called()  # The display_leaderboard method should trigger a print call


# Unit tests for the stopwatch class in timer.py
class TestStopwatch(unittest.TestCase):

    def setUp(self):
        self.timer = stopwatch()

    # Test starting the stopwatch
    def test_start_timer(self):
        self.timer.start()
        self.assertTrue(self.timer.running)  # Stopwatch should be running after start

    # Test stopping the stopwatch
    def test_stop_timer(self):
        self.timer.start()
        self.timer.stop()
        self.assertFalse(self.timer.running)  # Stopwatch should not be running after stop

    # Test resetting the stopwatch
    def test_reset_timer(self):
        self.timer.start()
        self.timer.reset()
        self.assertEqual(self.timer.elapsed_time, 0)  # Elapsed time should be reset to 0
        self.assertFalse(self.timer.running)  # Stopwatch should not be running after reset

    # Test getting the time from the stopwatch
    def test_get_time(self):
        self.timer.start()
        time.sleep(1)  # Wait for 1 second
        self.assertGreater(self.timer.get_time(), 1)  # Elapsed time should be greater than 1 second

    # Test displaying the time in a readable format
    def test_display_time(self):
        self.timer.start()
        time.sleep(1)  # Wait for 1 second
        self.assertEqual(len(self.timer.display_time().split(':')), 3)  # Should display time in 'hh:mm:ss' format


# Run all tests
if __name__ == '__main__':
    unittest.main()
