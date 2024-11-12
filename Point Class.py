
from timer import stopwatch
from hangman_functions import user_guess_letter

class point:

 def __init__(self):
    self.point=1
    self.starting_score=0
    self.score=self.starting_score
# just makes the defines the varibles of the class.
def add_point(self):
    if user_guess_letter:
        self.score=self.score+self.point
# is supposed to add point to the score.
def no_point(self):
    if not user_guess_letter:
        return self.score
# is supposed to make the score stay the same if youre wrong.you nethier get a point or lose a point.
def reset_point(self):
    if not stopwatch:
        self.score=0
#resets the score to 0.   
