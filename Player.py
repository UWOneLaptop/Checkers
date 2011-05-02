from Move import Move

WHITE = 1
BLACK = 2

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
			return Move.MOVE_INVALID

		return board.move(start, end, state)


# The AI player searches the board for the best move available. It only takes the board
# as a parameter and will return the updated board and the move made (so that the GUI
# can be updated) 
class AI_Player():
	
	color = None
	checkers = None
	#Constructor
	def __init__(self, color, checkers):
		self.color = color
		self.checkers = checkers
	
	def turn(self, board, state):
		moves = board.getAllMoves(state)
		if not moves:
			return
		move = moves.pop()
		end = move.pop()
		start = move.pop()
		last_cell = board.board[start.row][start.column]

		return_code = board.move(start, end, state)
		self.checkers.move(start, end, last_cell, return_code)

		while return_code == Move.JUMP_AVAILABLE:
			moves = board.getAllMoves(state)
			if not moves:
				break
			move = moves.pop()
			end = move.pop()
			start = move.pop()
			last_cell = board.board[start.row][start.column]

			return_code = board.move(start, end, state)
			self.checkers.move(start, end, last_cell, return_code)
			
		print "AI turn complete"

		
		
