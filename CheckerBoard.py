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
    
    def __init__(self):
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
            
                