from CheckerBoard import CheckerBoard
from Point import Point
from CheckersGUI import CheckersGUI
from GameState import GameState
from SquareState import SquareState
from Move import Move
import Player
import time

import pygtk
pygtk.require('2.0')
import gtk

class Checkers:

	# This method is called when the user clicks a box in the GUI. This could be called at any time,
	# including times when it is not the players turn. Any human supplied moves come through this
	# method. The moves are passed on the Human_Player objects to be validated. 
	# The widget parameter indicates where the user clicked (widget.row, widget.column) 
	def player_click(self, widget):
		# Look up that status of the cell that the user clicked from the board object
		
		cell = self.board.board[widget.column][widget.row]
			
		# This condition checks if the user is on the second click (already selected a piece
		# in their first click). This click is meant to place the piece
		if not self.last_clicked==None:
			# Look up the piece to move
			last_cell = self.board.board[self.last_clicked.column][self.last_clicked.row]
						
			# Store the move into start and end points to be passed to the player
			start = Point(self.last_clicked.column, self.last_clicked.row)
			end = Point(widget.column, widget.row)	

			
			#Make Human Move
			if self.state.get_state() == GameState.WhitesTurn and isinstance(self.white_player, Player.Human_Player):
				return_code = self.white_player.turn(start, end, self.board, self.state)
				self.move(start, end, last_cell, return_code)

			elif self.state.get_state() == GameState.BlacksTurn and isinstance(self.black_player, Player.Human_Player):
				return_code = self.black_player.turn(start, end, self.board, self.state)
				self.move(start, end, last_cell, return_code)
		
			
			#Make AI Move
			if self.state.get_state() == GameState.WhitesTurn and isinstance(self.white_player, Player.AI_Player):
				self.white_player.turn(self.board, self.state)
			if self.state.get_state() == GameState.BlacksTurn and isinstance(self.black_player, Player.AI_Player):
				self.black_player.turn(self.board, self.state)

			# Listen for next move
			self.last_clicked = None

		# If we are here this is the first click. The user is selecting  a piece to move. Only 
		# allow them to select their own pieces. Otherwise ignore the click
		elif self.state.get_state() == GameState.WhitesTurn and isinstance(self.white_player, Player.Human_Player):
			if cell == SquareState.WHITE:
				# Highlight the clicked spot and store it in the last_clicked field
				self.view.set_checker(widget.row, widget.column, "highlight_regular", "white")
				self.last_clicked = Point(widget.row, widget.column)
			elif cell == SquareState.WHITEKING:
				self.view.set_checker(widget.row, widget.column, "highlight_king", "white")
				self.last_clicked = Point(widget.row, widget.column)

		elif self.state.get_state() == GameState.BlacksTurn and isinstance(self.black_player, Player.Human_Player):
			if cell == SquareState.BLACK:
				self.view.set_checker(widget.row, widget.column, "highlight_regular", "black")
				self.last_clicked = Point(widget.row, widget.column)
			if cell == SquareState.BLACKKING: 
				self.view.set_checker(widget.row, widget.column, "highlight_king", "black")
				self.last_clicked = Point(widget.row, widget.column)
	
		
	def move(self, start, end, last_cell, return_code):
		if (self.state.get_state() == GameState.WhitesTurn and isinstance(self.white_player, Player.AI_Player) or
			self.state.get_state() == GameState.BlacksTurn and isinstance(self.black_player, Player.AI_Player)):
				time.sleep(0) # Delay for AI for lower depths
		
		#If the move was not valid, unhighlight the previous cell	
		if return_code == Move.MOVE_INVALID:
			if last_cell == SquareState.WHITE:
				self.view.set_checker(start.column, start.row, "regular", "white")
			elif last_cell == SquareState.WHITEKING: 
				self.view.set_checker(start.column, start.row, "king", "white")
			elif last_cell == SquareState.BLACK:
				self.view.set_checker(start.column, start.row, "regular", "black")
			elif last_cell == SquareState.BLACKKING: 
				self.view.set_checker(start.column, start.row, "king", "black")
		else:
			# Move was successful. Display the old square as empty
			self.view.set_checker(start.column, start.row, "none", "none")
			
			#If the piece was kinged, display it as a king
			if return_code == Move.KINGED or return_code == Move.JUMPED_AND_KINGED:
				if last_cell == SquareState.WHITE:
					self.view.set_checker(end.column, end.row, "king", "white")
				elif last_cell == SquareState.BLACK:
					self.view.set_checker(end.column, end.row, "king", "black")
			else:
				#Display the piece in the new square					
				if last_cell == SquareState.WHITE:
					self.view.set_checker(end.column, end.row, "regular", "white")
				elif last_cell == SquareState.WHITEKING: 
					self.view.set_checker(end.column, end.row, "king", "white")
				elif last_cell == SquareState.BLACK:
					self.view.set_checker(end.column, end.row, "regular", "black")
				elif last_cell == SquareState.BLACKKING:
					self.view.set_checker(end.column, end.row, "king", "black")

			#If a piece was jumped, remove it from the board
			if return_code == Move.JUMPED or return_code == Move.JUMP_AVAILABLE or return_code == Move.JUMPED_AND_KINGED:
				self.view.set_checker((start.column+end.column)/2, (start.row+end.row)/2, "none", "none")
			
			#If there is no jump available: next turn
			if not return_code == Move.JUMP_AVAILABLE:
				if self.state.get_state() == GameState.WhitesTurn:
					self.state.set_state(GameState.BlacksTurn)

					#Check if white won
					if self.board.gameOver(self.state):
						self.white_win_count = self.white_win_count + 1	
						self.view.update_counter(self.white_win_count)
						self.view.win_color("whites")					
					
					self.view.change_turn_color("whites")
				else:
					self.state.set_state(GameState.WhitesTurn)

					if self.board.gameOver(self.state):
						self.black_win_count = self.black_win_count + 1	
						self.view.update_counter(self.black_win_count)
						self.view.win_color("blacks")	

					
					self.view.change_turn_color("blacks")
	
	#Start a new game. Create all new objects except the gui (to keep track of score) and the win counts
	#For the gui use the reset function		
	def reset_board(self):
		self.board = CheckerBoard()
		self.board.printBoard()
		self.state = GameState(GameState.WhitesTurn)
		self.last_clicked = None
		
		#Reset the AI to the correct settings
		if self.ai_active and self.ai_color == Player.WHITE:
			self.white_player = Player.AI_Player(Player.WHITE, self)
			self.black_player = Player.Human_Player(Player.BLACK)
		elif self.ai_active and self.ai_color == Player.BLACK:
			self.white_player = Player.Human_Player(Player.WHITE)
			self.black_player = Player.AI_Player(Player.BLACK, self)
		else:
			self.white_player = Player.Human_Player(Player.WHITE)
			self.black_player = Player.Human_Player(Player.BLACK)
	
	#Set the AI on or off. Reset the player objects accordingly	
	def set_ai(self, ai_state):
		self.ai_active = ai_state

		#If turning AI on and white is the AI player, set white player to AI and 
		#black player to human
		if self.ai_active and self.ai_color == Player.WHITE:
			self.white_player = Player.AI_Player(Player.WHITE, self)
			self.black_player = Player.Human_Player(Player.BLACK)

			#If its whites turn, since white is AI, have white take its turn
			if self.state.get_state() == GameState.WhitesTurn:
				self.white_player.turn(self.board, self.state)
				
		elif self.ai_active and self.ai_color == Player.BLACK:
			self.white_player = Player.Human_Player(Player.WHITE)
			self.black_player = Player.AI_Player(Player.BLACK, self)

			if self.state.get_state() == GameState.BlacksTurn:
				self.black_player.turn(self.board, self.state)

		#If ai is off set both players to human
		else:
			self.white_player = Player.Human_Player(Player.WHITE)
			self.black_player = Player.Human_Player(Player.BLACK)
		
	def set_ai_color(self, color):
		self.ai_color = color
		self.set_ai(self.ai_active)

	def main(self):
		gtk.main()

	def __init__(self):
		self.board = CheckerBoard()
		self.view = CheckersGUI(self)
		self.state = GameState(GameState.WhitesTurn)
		self.white_player = Player.Human_Player(Player.WHITE)
		self.black_player = Player.AI_Player(Player.BLACK, self)
		self.white_win_count = 0
		self.black_win_count = 0
		self.last_clicked = None
		self.ai_active = True
		self.ai_color = Player.BLACK

if __name__ == "__main__":
	checkers = Checkers()
	checkers.main()
