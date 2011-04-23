class SquareState:
	EMPTY=0
	WHITE=1
	WHITEKING=2
	BLACK=3
	BLACKKING=4

	"""
	This method is used for printing the board in ascii. It is only useful until the GUI is built
	Remove for production 	
	"""
	@staticmethod
	def printSquare(state, isWhite):
		if state == SquareState.EMPTY and isWhite: return "   "
		elif state == SquareState.EMPTY and not isWhite: return "|||"
		elif state == SquareState.WHITE and isWhite: return " O "
		elif state == SquareState.WHITE and not isWhite: return "|O|"
		elif state == SquareState.WHITEKING and isWhite: return " 0 "
		elif state == SquareState.WHITEKING and not isWhite: return "|0|"
		elif state == SquareState.BLACK and isWhite: return " X "
		elif state == SquareState.BLACK and not isWhite: return "|X|"
		elif state == SquareState.BLACKKING and isWhite: return " K "
		elif state == SquareState.BLACKKING and not isWhite: return "|K|"
