# Game State
# Josh Scotland

# Class to get and set the game state
class GameState():
	# All the game states are constants
	GameHasBegun = 0
	WhitesTurn = 1
	BlacksTurn = 2
	GameIsPaused = 3
	GameIsResumed = 4
	GameHasEnded = 5

	def __init__(self, state=0):
		self.state = state

	def reset(self):
		self.state = 0
	
	def get_state(self):
		return self.state
		
	def set_state(self, state):
		self.state = state

