# Game State
# Josh Scotland

# All the game states as constants
GameHasBegun = 0
RedsTurn = 1
BlacksTurn = 2
GameHasEnded = 3
GameIsPaused = 4
GameIsResumed = 5

# Class to get and set the game state
class GameState(object):
	def get_state(self):
		return self._state
		
	def set_state(self, state):
		self._state = state
	
	state = property(get_state, set_state)

# Testing
GameState.state = BlacksTurn
print (GameState.state)
