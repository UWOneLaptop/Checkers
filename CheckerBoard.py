from SquareState import SquareState
from Point import Point
from Move import Move
from math import*

class CheckerBoard:
	def __init__(self):
	#All initialization
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
		

		
	"""
	This method is used for printing the board in ascii. It is only useful as a debugging tool.
	Comment out for production
	"""             
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
	
	
	# Returns the colorInt of the winner (-1 if game not over)
	# Input is the color of the player who most recently had a turn
	def gameWinner(self, game_state):
		if game_state.get_state()== 5:
			return game_state.get_state
		else: return -1
	
	# Checks to see if the given move is legal.  
	# Inputs are two Point objects: the start point and the end point
	# Pre: 1)start and end are points in the 8*8 board 2)State is correct (either player is playing)
	def checkMove(self, start, end, game_state, no_printing):
		start_piece = self.board[start.row][start.column]
		if self.board[end.row][end.column] == SquareState.EMPTY:
			if game_state.get_state() == 1: # white's turn
				if start_piece == SquareState.WHITE:
					return self.checkDistance(start, end, True, False, no_printing)
				elif start_piece == SquareState.WHITEKING:
					return self.checkDistance(start, end, True, True, no_printing)
				else:
					if not no_printing: print "Invalid Move: Not your (white's) piece"
					return False
			else: # black's turn
				if start_piece == SquareState.BLACK:
					return self.checkDistance(start, end, False, False, no_printing)
				elif start_piece == SquareState.BLACKKING:
					return self.checkDistance(start, end, False, True, no_printing)
				else:
					if not no_printing: print "Invalid Move: Not your (black's) piece"
					return False
		else:
			if not no_printing: print "Invalid Move: End space is not empty"
			return False
		
	def checkDistance(self, start, end, player_flag, king_flag, no_printing):
		if end.row > 7 or end.row < 0 or end.column > 7 or end.column < 0:
			return False
		# check if we're moving to the next square
		if abs(start.row - end.row) == 1 and abs(start.column - end.column) == 1:
			if king_flag: # kings can go forward and back
				return True
			elif player_flag and start.column - end.column == 1: # This is VERY confusing, this should be row ... (~Josh)
				return True
			elif (not player_flag) and start.column - end.column == -1:
				return True
			else:
				if not no_printing: print "Invalid Move: Piece going in the wrong direction"
				return False
		# check if we're jumping to the next square
		elif abs(start.row - end.row) == 2 and abs(start.column - end.column) == 2:
			middle_piece = self.board[(start.row + end.row)/2][(start.column + end.column)/2]
			if ((player_flag and (middle_piece == SquareState.BLACK or middle_piece == SquareState.BLACKKING)) or
				((not player_flag) and (middle_piece == SquareState.WHITE or middle_piece == SquareState.WHITEKING))):
				if king_flag: # kings can jump forward and back
					return True
				elif player_flag and start.column - end.column == 2:
					return True
				elif (not player_flag) and start.column - end.column == -2:
					return True
				else:
					if not no_printing: print "Invalid Move: Piece jumping in the wrong direction"
					return False
			else:
				if not no_printing: print "Invalid Move: No piece to jump over"
				return False
		else:
			if not no_printing: print "Invalid Move: Piece is not doing an in range diagonal move or jump"
			return False
		
#		if start.row%2 + start.column%2 != 1 or end.row%2 + end.column%2 !=1:
#			return False
#		if not (self.board[start.row][start.column]+1)/2 == game_state.get_state() or not self.board[end.row][end.column] == SquareState.EMPTY:
#			return False
#		if not end.column - start.column == abs(end.column - start.column)*(game_state.get_state()*2-3) and not self.board[start.row][start.column] == SquareState.WHITEKING and not self.board[start.row][start.column] == SquareState.BLACKKING:
#			return False
#		if abs(end.column - start.column) == 1 and abs(end.row - start.row) == 1 and not self.anyJump(game_state):
#			return True
#		return abs(end.column - start.column) == 2 and abs(end.row - start.row) == 2 and self.board[(start.row + end.row)/2][(start.column + end.column)/2] == 5 - game_state.get_state()*2
		
		


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
		if end.column == 7 and game_state.get_state() == 2:
			self.board[end.row][end.column] = SquareState.BLACKKING
			kinged = True
		elif end.column == 0 and game_state.get_state() == 1:
			self.board[end.row][end.column] = SquareState.WHITEKING
			kinged = True

		#Check if there are jumps available
		if self.anyJump(game_state):
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
	def getMoves(self,start,game_state):
		possibleMoves = []
		for step in range(8):
			x = int(start.row + (step//4+1)*cos(pi/4+pi/2*step)/abs(cos(pi/4+pi/2*step)))
			y = int(start.column + (step//4+1)*sin(pi/4+pi/2*step)/abs(sin(pi/4+pi/2*step)))
			if x <= 7 and x >= 0 and y <= 7 and y >= 0:
				end = Point(x,y)
				if self.checkMove(start,end,game_state,True):
					possibleMoves.append(end)
		return possibleMoves
	
	# Pre: Game state is BlacksTurn or WhitesTurn
	# Returns a list of all possible moves this player can make
	def getAllMoves(self, game_state):
		moves = []
		for row in range(len(self.board)):
			for col in range(len(self.board[row])):
				start = Point(row, col)
				availbleMoves = self.getMoves(start, game_state)
				if not not availbleMoves:
					for end in availbleMoves:
						moves.append([start,end])
		return moves
				
	# private function 
	# Return true if there are any pieces that can jump
	def anyJump(self, game_state):
		for row in range(len(self.board)):
			for col in range(len(self.board[row])):
				start = Point(row, col)
				if self.canJumps(start, 0, game_state):
					return True
		return False

	# private function      
	# Return true if user can any jump from a particular start
	def canJumps(self, start, step, game_state):
		if step == 4:
			return False
		if not (self.board[start.row][start.column]+1)//2 == game_state.get_state():
			return False
		x = int(start.row + 2*cos(pi/4+pi/2*step)/abs(cos(pi/4+pi/2*step)))
		y = int(start.column + 2*sin(pi/4+pi/2*step)/abs(sin(pi/4+pi/2*step)))
		if x <= 7 and x >= 0 and y <= 7 and y >= 0:
			if y - start.column == abs(y - start.column)*(game_state.get_state()*2-3) or self.board[start.row][start.column] == SquareState.WHITEKING or self.board[start.row][start.column] == SquareState.BLACKKING:
				if self.board[(start.row + x)/2][(start.column + y)/2] == 5 - game_state.get_state()*2:
					if self.board[x][y] == SquareState.EMPTY and self.board[start.row][start.column] != SquareState.EMPTY:
						return True
		return True and self.canJumps(start, step+1,game_state)

	# Determines the board's value for the AI to choose the best
	def getValue(self, game_state):
		whiteValue = 0
		blackValue = 0
		for row in range(len(self.board)):
			for col in range(len(self.board[row])):
				if self.board[row][col] == SquareState.WHITE:
					whiteValue += 1
				elif self.board[row][col] == SquareState.WHITEKING:
					whiteValue += 3
				elif self.board[row][col] == SquareState.BLACK:
					blackValue += 1
				elif self.board[row][col] == SquareState.BLACKKING:
					blackValue += 3
		if game_state.get_state()== 1:
			return whiteValue - blackValue
		elif game_state.get_state()== 2:
			return blackValue - whiteValue
		else:
			print "Not in a valid state to check board value"

	def copy(self):
		copy = []
		for row in range(len(self.board)):
			copy.append([])
			for col in range(len(self.board[row])):
				copy[col].append(self.board[col])
		return copy
				
