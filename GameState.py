# Game State
# Josh Scotland

# All the game states as constants
GameHasBegun = 0
RedsTurn = 1
BlacksTurn = 2
GameIsPaused = 3
GameIsResumed = 4
GameHasEnded = 5

# Class to get and set the game state
class GameState():
        def __init__(self, state=0):
                self.state = state

        def reset(self):
                self.state = 0
        
        def get_state(self):
                return self.state
                
        def set_state(self, state):
                self.state = state
