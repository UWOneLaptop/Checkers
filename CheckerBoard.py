class SquareState:
    EMPTY=0
    RED=1
    REDKING=2
    BLACK=3
    BLACKKING=4
       
    """
    This method is used for printing the board in ascii. It is only useful until the GUI is built.
    Remove for production
    """
    @staticmethod
    def printSquare(state, isWhite):
        if state == SquareState.EMPTY and isWhite: return "   "
        elif state == SquareState.EMPTY and not isWhite: return "|||"
        elif state == SquareState.RED and isWhite: return " O "
        elif state == SquareState.RED and not isWhite: return "|O|"
        elif state == SquareState.REDKING and isWhite: return " 0 "
        elif state == SquareState.REDKING and not isWhite: return "|0|"
        elif state == SquareState.BLACK and isWhite: return " X "
        elif state == SquareState.BLACK and not isWhite: return "|X|"
        elif state == SquareState.BLACKKING and isWhite: return " K "
        elif state == SquareState.BLACKKING and not isWhite: return "|K|"
        
class CheckerBoard:
    board = []
	#Number of white pieces
	#Number of black pieces
    
    def __init__(self):
		#All initialization
        for col in range(8):
            self.board.append([])
            for row in range(8):
                if row < 3 and (col + row) % 2 == 1:
                    self.board[col].append(SquareState.BLACK)
                elif row > 4 and (col + row) % 2 == 1:
                    self.board[col].append(SquareState.RED)
                else:
                    self.board[col].append(SquareState.EMPTY)
            
            
    """
    This method is used for printing the board in ascii. It is only useful until the GUI is built.
    Remove for production
    """    
    def printBoard(self):
        result = "|---|---|---|---|---|---|---|---|\n"
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                result += "|" + SquareState.printSquare(self.board[col][row],(row+col)%2==0) 
            result +="|\n|---|---|---|---|---|---|---|---|\n"
            
        print result
		
    # Returns whether or not the game is over 
    def gameOver(whoseTurn):
    	if getAllMoves(whoseTurn) == None:
    		return True
    	return False
    	
	
	# Returns the colorInt of the winner (-1 if game not over)
	# Input is the color of the player who most recently had a turn
	def gameWinner(whoseTurnLast):
		return Player.RED
	
	# Checks to see if the given move is legal (i.e. it is diagonal one square, there is no other
	# piece in the end point, or it is a jump, etc). 
	# Inputs are two Point objects: the start point and the end point
	def checkMove(start, end):
		return False
	
	# Makes the given move.  Returns true if the player has another move, else false
	# Inputs are two point objects: the start point and the end point
	def move(start, end):
		return False
	
	# Returns a list of all available Points that can be moved to from Start
	# Input is a point object
	def getMoves(start):
		return None
	
	# Returns a list of all possible moves this player can make
	def getAllMoves(whoseTurn):
		return None
	
	