from hangman_functions import user_guess_letter

class points:

# ATTRIBUTES
    def __init__(self):
        self.score = 0

# ALTER DATA
    def add_point(self): # When User wins game, adds a point
        self.score += 1
    
    def reset_point(self): # Added for future functionality
        self.score = 0 #resets the score to 0.

    def remove_point(self): # When User loses game, removes a point
        self.score -= 1

    # GAME GUI (WHAT USER SEES)
    def show_points(self): # Shows User how many points they have
        print(f"Your score is: {self.score}.")
    
    # GAME OUTPUTS (RECIEVING A VALUE)
    def get_points(self): # Used for comparison values.
        return self.score
