from SquareState import SquareState
from Point import Point
from Move import Move
from math import cos
from math import sin
from math import pi

class CheckerBoard:
	def __init__(self):
	# All initialization
		self.board = []
		for col in range(8):
			self.board.append([])
			for row in range(8):
				if row < 3 and (col + row) % 2 == 1:
					self.board[col].append(SquareState.BLACK)
				elif row > 4 and (col + row) % 2 == 1:
					self.board[col].append(SquareState.WHITE)
				else:
					self.board[col].append(SquareState.EMPTY)

	# Prints out the board      
	def printBoard(self):   
		result = "|---|---|---|---|---|---|---|---|\n"
		for row in range(len(self.board)):      
			for col in range(len(self.board[0])):
				result += "|" + SquareState.printSquare(self.board[col][row],(row+col)%2==0)
			result +="|\n|---|---|---|---|---|---|---|---|\n"
		print result


	# Returns whether or not the game is over 
	def gameOver(self, game_state):
		return not self.getAllMoves(game_state)
	
	
	# Returns the winning player (-1 if game not over)
	def gameWinner(self, game_state):
		if game_state.get_state()== 5:
			return game_state.get_state
		else: return -1
	
	# Returns if a move is valid, and also if it is a jumping move 
	def checkMove(self, start, end, game_state, no_printing):
		# Need to check if there are any pieces to be jumped
		jumps = self.getAllJumps(game_state)
		if jumps:
			for [start1, end1] in jumps:
				if start1.row == start.row and start1.column == start.column and end1.row == end.row and end1.column == end.column:
					return Move.JUMP_AVAILABLE
			if not no_printing: print "Invalid Move: You must jump"
			return Move.MOVE_INVALID
		else: # No jumps that need to be taken
			return self.determineTurn(start, end, game_state, no_printing)
			
	def determineTurn(self, start, end, game_state, no_printing):
		start_piece = self.board[start.row][start.column]
		if self.board[end.row][end.column] == SquareState.EMPTY:
			if game_state.get_state() == 1: # white's turn
				if start_piece == SquareState.WHITE:
					return self.checkDistance(start, end, True, False, no_printing)
				elif start_piece == SquareState.WHITEKING:
					return self.checkDistance(start, end, True, True, no_printing)
				else:
					if not no_printing: print "Invalid Move: Not your (white's) piece"
					return Move.MOVE_INVALID
			else: # black's turn
				if start_piece == SquareState.BLACK:
					return self.checkDistance(start, end, False, False, no_printing)
				elif start_piece == SquareState.BLACKKING:
					return self.checkDistance(start, end, False, True, no_printing)
				else:
					if not no_printing: print "Invalid Move: Not your (black's) piece"
					return Move.MOVE_INVALID
		else:
			if not no_printing: print "Invalid Move: End space is not empty"
			return Move.MOVE_INVALID
	
	# Helper function to check if the piece is moving (1 square) or jumping (2 squares)
	def checkDistance(self, start, end, player_flag, king_flag, no_printing):
		if end.row > 7 or end.row < 0 or end.column > 7 or end.column < 0:
			return Move.MOVE_INVALID
		# check if we're moving to the next square
		if abs(start.row - end.row) == 1 and abs(start.column - end.column) == 1:
			if king_flag: # kings can go forward and back
				return Move.MOVE_AVAILABLE
			elif player_flag and start.column - end.column == 1: # This is VERY confusing, this should be row ... (~Josh)
				return Move.MOVE_AVAILABLE
			elif (not player_flag) and start.column - end.column == -1:
				return Move.MOVE_AVAILABLE
			else:
				if not no_printing: print "Invalid Move: Piece going in the wrong direction"
				return Move.MOVE_INVALID
		# check if we're jumping to the next square
		elif abs(start.row - end.row) == 2 and abs(start.column - end.column) == 2:
			middle_piece = self.board[(start.row + end.row)/2][(start.column + end.column)/2]
			if ((player_flag and (middle_piece == SquareState.BLACK or middle_piece == SquareState.BLACKKING)) or
				((not player_flag) and (middle_piece == SquareState.WHITE or middle_piece == SquareState.WHITEKING))):
				if king_flag: # kings can jump forward and back
					return Move.JUMP_AVAILABLE
				elif player_flag and start.column - end.column == 2:
					return Move.JUMP_AVAILABLE
				elif (not player_flag) and start.column - end.column == -2:
					return Move.JUMP_AVAILABLE
				else:
					if not no_printing: print "Invalid Move: Piece jumping in the wrong direction"
					return Move.MOVE_INVALID
			else:
				if not no_printing: print "Invalid Move: No piece to jump over"
				return Move.MOVE_INVALID
		else:
			if not no_printing: print "Invalid Move: Piece is not doing an in range diagonal move or jump"
			return Move.MOVE_INVALID

	# Makes the given move.  Returns true if the player has another move, else false
	# Inputs are two point objects: the start point and the end point
	def move(self, start, end, game_state):
		jumped = False
		kinged = False
		jump_available = False

		#Make the move
		self.board[end.row][end.column] = self.board[start.row][start.column]
		self.board[start.row][start.column] = SquareState.EMPTY
		
		#Check if it was a jump
		if abs(start.row - end.row) == 2:
			self.board[(start.row+end.row)/2][(start.column+end.column)/2] = SquareState.EMPTY
			jumped = True

		#Check if the piece was kinged
		end_piece = self.board[end.row][end.column]
		if end.column == 7 and (game_state.get_state()== 2 and end_piece == SquareState.BLACK):
			self.board[end.row][end.column] = SquareState.BLACKKING
			kinged = True
		elif end.column == 0 and (game_state.get_state()== 1 and end_piece == SquareState.WHITE):
			self.board[end.row][end.column] = SquareState.WHITEKING
			kinged = True

		#Check if there are jumps available
		if self.getAllJumps(game_state):
			jump_available = True
		
		#self.printBoard()              

		if kinged and jumped:
			return Move.JUMPED_AND_KINGED
		elif kinged and not jumped:
			return Move.KINGED
		elif (not kinged) and jumped and jump_available:
			return Move.JUMP_AVAILABLE
		elif (not kinged) and jumped and (not jump_available):
			return Move.JUMPED
		elif (not kinged) and (not jumped):
			return Move.TURN_COMPLETE
	
	# Returns a list of all available Points that can be moved to from Start
	# Input is a point object
	def getMoves(self, start, game_state):
		jumpMoves = []
		possibleMoves = []
		for step in range(8):
			x = int(start.row + (step//4+1)*cos(pi/4+pi/2*step)/abs(cos(pi/4+pi/2*step)))
			y = int(start.column + (step//4+1)*sin(pi/4+pi/2*step)/abs(sin(pi/4+pi/2*step)))
			if x <= 7 and x >= 0 and y <= 7 and y >= 0:
				end = Point(x,y)
				return_code = self.determineTurn(start,end,game_state,True)
				if return_code != Move.MOVE_INVALID:
					if return_code == Move.JUMP_AVAILABLE:
						jumpMoves.append(end)
					else:
						possibleMoves.append(end)
		if jumpMoves:
			return jumpMoves
		else:
			return possibleMoves
	
	# Pre: Game state is BlacksTurn or WhitesTurn
	# Returns a list of all possible moves this player can make
	def getAllMoves(self, game_state):
		moves = []
		for row in range(len(self.board)):
			for col in range(len(self.board[row])):
				start = Point(row, col)
				if self.board[start.row][start.column] != SquareState.EMPTY:
					availbleMoves = self.getMoves(start, game_state)
					if availbleMoves:
						for end in availbleMoves:
							moves.append([start,end])
		return moves
	
	# Pre: Game state is BlacksTurn or WhitesTurn
	# Returns a list of all possible moves this player can make
	def getAllPlayerMoves(self, game_state):
		moves = []
		for row in range(len(self.board)):
			for col in range(len(self.board[row])):
				start = Point(row, col)
				start_piece = self.board[start.row][start.column]
				if (start_piece != SquareState.EMPTY and
				((game_state.get_state()== 2 and (start_piece == SquareState.BLACK or start_piece == SquareState.BLACKKING)) or
				((game_state.get_state()== 1) and (start_piece == SquareState.WHITE or start_piece == SquareState.WHITEKING)))):
					availbleMoves = self.getMoves(start, game_state)
					if availbleMoves:
						for end in availbleMoves:
							moves.append([start,end])
		return moves
	
	# Returns a list of all possible jumps this player can make
	def getAllJumps(self, game_state):
		jumps = []
		for row in range(len(self.board)):
			for col in range(len(self.board[row])):
				start = Point(row, col)
				if self.board[start.row][start.column] != SquareState.EMPTY:
					availbleJumps = self.getPlayerJumps(start, game_state)
					if availbleJumps:
						for end in availbleJumps:
							jumps.append([start,end])
		return jumps
	
	# Returns the list of pieces that can jump
	def getPlayerJumps(self,start,game_state):
		jumpMoves = []
		for step in range(8):
			x = int(start.row + (step//4+1)*cos(pi/4+pi/2*step)/abs(cos(pi/4+pi/2*step)))
			y = int(start.column + (step//4+1)*sin(pi/4+pi/2*step)/abs(sin(pi/4+pi/2*step)))
			if x <= 7 and x >= 0 and y <= 7 and y >= 0:
				end = Point(x,y)
				start_piece = self.board[start.row][start.column]
				if (start_piece != SquareState.EMPTY and
				((game_state.get_state()== 2 and (start_piece == SquareState.BLACK or start_piece == SquareState.BLACKKING)) or
				((game_state.get_state()== 1) and (start_piece == SquareState.WHITE or start_piece == SquareState.WHITEKING)))):
					if self.determineTurn(start,end,game_state,True) == Move.JUMP_AVAILABLE:
						jumpMoves.append(end)
		return jumpMoves

	# Determines the board's value for the AI to choose the best
	# TODO Fix this to know the game_state of player and if they are MAX / MIN
	def getValue(self, game_state, player):
		whiteValue = 0
		blackValue = 0
		for row in range(len(self.board)):
			for col in range(len(self.board[row])):
				if self.board[row][col] == SquareState.WHITE:
					whiteValue += 1
				elif self.board[row][col] == SquareState.WHITEKING:
					whiteValue += 5
				elif self.board[row][col] == SquareState.BLACK:
					blackValue += 1
				elif self.board[row][col] == SquareState.BLACKKING:
					blackValue += 5
		if not player:
			return whiteValue - blackValue
		else:
			return blackValue - whiteValue

	def copy(self):
		copy = []
		for row in range(len(self.board)):
			copy.append([])
			for col in range(len(self.board[row])):
				copy[col].append(self.board[col])
		return copy
				
