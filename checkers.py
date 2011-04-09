from CheckerBoard import CheckerBoard
from Point import Point

class Checkers:

	#Fields
	#---------
	#checkersGui gui	The Gui Object "checkers.py"
	#Player white		The white player object
	#Player black		The black player object
	#Board b			The board object
	#int whiteScore		White's score (number of games won)
	#int blackScore		Black's score (number of games won)
	
	#Main sequence of operations.  Plays checkers until the user does not want to
	#
	#Use this class for testing your code. 
	#
	#There is some sample code here to see how to take input from a user on a command line (raw_input)
	#and how to call the functions you have implemented in another object. Note that we had to 
	#import the CheckerBoard class from the file called CheckerBoard. 
	#If you wanted to test the singleTurn method in Player.py, for instance, you would add to the top
	#of this file "from Player import Player". You would then add playerBlack = Player() and then
	#call playerBlack.singleTurn(). 
	
	def main(self):
		board = CheckerBoard()
		var = raw_input("Enter something: ")
		print "you entered ", var
		#board.printBoard()
		
		p = Point(2, 3)
		print p.x
		print p.y
		

if __name__ == "__main__":
	checkers = Checkers()
	checkers.main()