
WHITE = 1
BLACK = 2

TURN_COMPLETE = 0
MOVE_INVALID = 1
JUMP_AVAILABLE = 2

# The Player classes take turns in games of checkers. They are called by checkers.py

# The human player recieves input from a human player telling it where the human
# wants to move. This class makes sure the move is valid and checks for jumps
class Human_Player():

	color = None
	
	#Constructor
	def __init__(self, color):
		self.color = color

	# The turn method should receive the start and end points of the desired move
	# and the board object to make the move on. This method should check that the move
	# is valid (by using the board's methods) and then update the board with that move. 
	# 
	# Returns a code indicating if the turn is over, and the reason if it is not
	def turn(self, start, end, board, state):
		if not board.checkMove(start, end, state):
			print "returning move invalid"
			return MOVE_INVALID

		if board.move(start, end, state):
			print "jump available"
			return JUMP_AVAILABLE

		print "player turn complete"
		return TURN_COMPLETE


# The AI player searches the board for the best move available. It only takes the board
# as a parameter and will return the updated board and the move made (so that the GUI
# can be updated) 
class AI_Player():
	
	color = None
	#Constructor
	def __init__(self, color):
		self.color = color
	
	def turn(self, start, end, board, state):
                print "Start: " + str(start.row) + ", " + str(start.column)
                print "End: " + str(end.row) + ", " + str(end.column)
		if board.move(start, end, state):
                        #self.turn(start, end, board, state)
                        print "AI should move again, but this is not implemented"
		print "AI turn complete"
		return TURN_COMPLETE
		
