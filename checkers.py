from CheckerBoard import CheckerBoard
from Point import Point
from CheckersGUI import CheckersGUI
from GameState import GameState

class Checkers:

	# The Checkboard object. This stores the state of the board 
	# and contains functions for manipulating it
	board = None
	
	# The Checkerboard GUI. This displays the game to the user
	# and takes user input
	view = None

	# The last point clicked by the user
	last_clicked = None

	# The state of the game (Black's turn, paused, etc)
	state = None

	#Fields
	#---------
	#checkersGui gui	The Gui Object "checkers.py"
	#Player white		The white player object
	#Player black		The black player object
	#Board b			The board object
	#int whiteScore		White's score (number of games won)
	#int blackScore		Black's score (number of games won)
	
	def player_click(self, widget):
		print widget.row
		print widget.column
		if self.view.get_checker(widget.row, widget.column)[0]:
			kind = "king"
		else: 
			kind = "regular"
		color = self.view.get_checker(widget.row, widget.column)[1]	
		print "Kind: "+kind
		print "Color: "+color		

		if not color == "none":
			self.view.set_checker(widget.row, widget.column, "highlight_"+kind, color)
			self.last_clicked = Point(widget.row, widget.column)
			

	def main(self):
		var = raw_input("End game: ")

	def __init__(self):
		self.board = CheckerBoard()
		self.view = CheckersGUI(self)
		self.state = GameState(GameState.WhitesTurn)

if __name__ == "__main__":
	checkers = Checkers()
	checkers.main()
