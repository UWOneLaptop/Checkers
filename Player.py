from Move import Move
import copy
from GameState import GameState
import random

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
		if board.checkMove(start, end, state, False) == Move.MOVE_INVALID:
			return Move.MOVE_INVALID
		return board.move(start, end, state)


# The AI player searches the board for the best move available. It only takes the board
# as a parameter and will return the updated board and the move made (so that the GUI
# can be updated) 
class AI_Player():
	
	color = None
	checkers = None
	best_move = None
	
	#Constructor
	def __init__(self, color, checkers):
		self.color = color
		self.checkers = checkers
		self.best_move = None
		
	def get_best(self):
		return self.best_move
		
	def set_best(self, best):
		self.best_move = best
	
	def turn(self, board, state):
		
		# Toughness of CPU
		depth = 5
		
		alpha = -999
		beta = 999
		player = True # True means Max, False means Min
		board_orig = copy.deepcopy(board.board)
		
		value_best = self.alphabeta(board, depth, alpha, beta, player, state)
		
		# we found it so actually make the move
		updateGUI = 1
		board.board = copy.deepcopy(board_orig)
		[best_start, best_end] = self.get_best()
		last_cell = board.board[best_start.row][best_start.column]
		return_code = board.move(best_start, best_end, state)
		self.checkers.move(best_start, best_end, last_cell, return_code)
		self.jumpAgain(board, state, return_code, updateGUI)

		#board.printBoard()
		print "AI chose board value: ", value_best
		print "AI turn complete"

	def jumpAgain(self, board, state, return_code, updateGUI):
		while return_code == Move.JUMP_AVAILABLE:
			moves = board.getAllPlayerMoves(state)
			if not moves:
				break
			move = moves.pop()
			end = move.pop()
			start = move.pop()
			last_cell = board.board[start.row][start.column]

			return_code = board.move(start, end, state)
			if updateGUI:
				self.checkers.move(start, end, last_cell, return_code)
				
	def alphabeta(self, board, depth, alpha, beta, player, state):
		if depth == 0 or board.gameOver(state):
			return board.getValue(state, player)
		moves = board.getAllPlayerMoves(state)
		if not moves:
			return			
		# variables for finding the best move for this turn
		board_orig = copy.deepcopy(board.board)
		updateGUI = 0
		random.shuffle(moves)
		[start, end] = moves[0]
		local_best = [start, end]
		if player: # If player is true, then it is Max, else Min
			for move in moves:
				board.board = copy.deepcopy(board_orig)
				end = move.pop()
				start = move.pop()
				return_code = board.move(start, end, state)
				self.jumpAgain(board, state, return_code, updateGUI)
				alpha_new = self.alphabeta(board, depth - 1, alpha, beta, not player, state)
				if alpha_new > alpha:
					alpha = alpha_new
					local_best = [start, end]
					#print "The new best for", player, " is ", alpha
				if (beta <= alpha):
					break
			self.set_best(local_best)
			return alpha
		else:
			for move in moves:
				board.board = copy.deepcopy(board_orig)
				end = move.pop()
				start = move.pop()
				return_code = board.move(start, end, state)
				self.jumpAgain(board, state, return_code, updateGUI)
				beta_new = self.alphabeta(board, depth - 1, alpha, beta, not player, state)
				if beta_new < beta:
					beta = beta_new
					local_best = [start, end]
					#print "The new best for", player, " is ", beta
				if (beta <= alpha):
					break
			self.set_best(local_best)
			return beta