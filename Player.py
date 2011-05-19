from Move import Move
import copy
from GameState import GameState
import random
import time

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

		# variables for finding the best move for this turn
		board_orig = copy.deepcopy(board.board)
		value_best = -99
		start_best = 0
		updateGUI = 0

		# search for the next best move
		random.shuffle(moves)
		for move in moves:
			board.board = copy.deepcopy(board_orig)
			
			end = move.pop()
			start = move.pop()
			return_code = board.move(start, end, state)
			self.jumpAgain(board, state, return_code, updateGUI)

			# now play the other player's move
			if (state.get_state() == 2):
				state_other = GameState(GameState.WhitesTurn)
				self.turn_other(board, state_other)
			elif (state.get_state() == 1):
				state_other = GameState(GameState.BlacksTurn)
				self.turn_other(board, state_other)
			else:
				print "Invalid player state"
			
			value = board.getValue(state)
			print "The value for this board is: ", value
			if value > value_best:
				value_best = value
				start_best = start

		# we found it so actually make the move
		updateGUI = 1
		board.board = copy.deepcopy(board_orig)
		print "Choose the move with this value: ", value_best
		last_cell = board.board[start_best.row][start_best.column]
		return_code = board.move(start, end, state)
		self.checkers.move(start, end, last_cell, return_code)
		self.jumpAgain(board, state, return_code, updateGUI)

		board.printBoard()
		print "AI turn complete"


	def turn_other(self, board, state):
		moves = board.getAllMoves(state)
		if not moves:
			return

		# variables for finding the best move for this turn
		board_orig = copy.deepcopy(board.board)
		value_best = -99
		updateGUI = 0

		# search for the next best move
		for move in moves:
			board.board = copy.deepcopy(board_orig)
			
			end = move.pop()
			start = move.pop()
			return_code = board.move(start, end, state)
			self.jumpAgain(board, state, return_code, updateGUI)
			
			value = board.getValue(state)
			if value > value_best:
				value_best = value

		# we found it so actually make the move
		board.board = copy.deepcopy(board_orig)
		return_code = board.move(start, end, state)
		self.jumpAgain(board, state, return_code, updateGUI)

		
	def jumpAgain(self, board, state, return_code, updateGUI):
		while return_code == Move.JUMP_AVAILABLE:
			moves = board.getAllMoves(state)
			if not moves:
				break
			move = moves.pop()
			end = move.pop()
			start = move.pop()
			last_cell = board.board[start.row][start.column]

			return_code = board.move(start, end, state)
			if updateGUI:
				self.checkers.move(start, end, last_cell, return_code)
				time.sleep(1)
