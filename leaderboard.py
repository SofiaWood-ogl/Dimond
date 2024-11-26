# leaderboard.py

# importing stoptwatch class from timer in order to handle time tracking
from timer import stopwatch

# Player class to hold information for each player including name, score and time
class Player:
  def __init__(self,name):
    #initializing a player with their name, score, and time
    self.name = name
    self.score = 0 # default score would be 0 at the start
    self.time = 0.0 # default time would be 0.0 seconds at the start of the game

  def set_score(self, score):
    # setting the player's score
    self.score = score
  
  def set_time(self, time):
    # setting the player's time
    self.time = time
  
  def get_score(self):
    # getting the players score
    return self.time
  
  def get_time(self):
    # getting the players time
    return self.time
  
  def get_name(self):
    # Getting the players name
    return self.name

#Leaderboard class to store and manage the lists of players, scores, and times
class Leaderboard:
  def __init__(self):
    #Initialize the leaderboard with an empty list of players, scores, and times
    self.players = [] # lists holds the player object 

def add_players(self, players):
  # Add a player to the leaderboard
  self.players.append(player)

def update_score(self, player_name, score):
  #update player's score in the leaderboard based on name
  for player in self.players:
    if player.get_name() == player_name:
      player.set_score(score)
      return
  print(f"Player {player_name} was not found on the leaderboard.") # prints error message if the player is not found

def update time(self, player_name, time):
# updatin the players time based to their name
  for player in self.player:
    if player.get_name() == player.name:
      player.set_time(time)
      return 
  print(f" Player {player_name} was not found on the leaderboard.") # Prints error message if the player was not found 

def get_leaderboard(self):
  # Getting the leaderboard scored based on score in decending order then time in ascending order
  sorted_players = sorted(self.players, key= lamda x: (-x,get_score
    
  
  
  
  
  













