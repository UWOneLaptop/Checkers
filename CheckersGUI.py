#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import sys
import os
from gettext import gettext as _

# need to work folloowing http://wiki.laptop.org/go/Python_i18n
# language	locale
# English	en
# Spanish	es
# Catalan	ca
# Chinese	zh
# Japanese	ja
# French	fr

class CheckersGUI:
<<<<<<< HEAD
=======
	controller = None

>>>>>>> 13d49b04b4b622a5626f8848234fbf2bd586ac8c
	def new_game(self, widget, data=None):
		print "Creating new game"
		dialog = gtk.MessageDialog(self.window, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_YES_NO, _("Are you sure you want to delete the current game?"))
		dialog.set_title("Checkers 1.0")
		response = dialog.run()
		dialog.destroy()
		if response == gtk.RESPONSE_YES:
			python = sys.executable
			os.execl(python, python, * sys.argv)
			return True
		else:
			return False

	def win(self):
		if self.playing == "whites":
<<<<<<< HEAD
			dialog_image = gtk.image_new_from_file("white_king.svg")
			string_displayed = _("Whites win!")
		else:
			dialog_image = gtk.image_new_from_file("black_king.svg")
=======
			dialog_image = gtk.image_new_from_file("images/white_king.svg")
			string_displayed = _("Whites win!")
		else:
			dialog_image = gtk.image_new_from_file("images/black_king.svg")
>>>>>>> 13d49b04b4b622a5626f8848234fbf2bd586ac8c
			string_displayed = _("Blacks win!")
		dialog = gtk.Dialog(string_displayed, None, gtk.DIALOG_MODAL, (gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
		dialog_label = gtk.Label(string_displayed)
		dialog_image.show()
		dialog_label.show()
		dialog.vbox.pack_start(dialog_image)
		dialog.vbox.pack_start(dialog_label)
		dialog.run()
		dialog.destroy()
	
	def change_turn(self):
		if self.playing == "whites":
			self.playing = "blacks"
<<<<<<< HEAD
			self.p1_box.get_children()[0].set_from_file("black_king_active.svg")
			self.p2_box.get_children()[0].set_from_file("white_king.svg")
		else:
			self.playing = "whites"
			self.p1_box.get_children()[0].set_from_file("black_king.svg")
			self.p2_box.get_children()[0].set_from_file("white_king_active.svg")
	
	def set_checker(self, row, column, kind=None, player=None):
		cell = self.table.get_children()[(row*8)+column]
=======
			self.p1_box.get_children()[0].set_from_file("images/black_king_active.svg")
			self.p2_box.get_children()[0].set_from_file("images/white_king.svg")
		else:
			self.playing = "whites"
			self.p1_box.get_children()[0].set_from_file("images/black_king.svg")
			self.p2_box.get_children()[0].set_from_file("images/white_king_active.svg")
	
	def set_checker(self, row, column, kind=None, player=None):
		cell = self.table.get_children()[((7-row)*8)+(7-column)]
		
>>>>>>> 13d49b04b4b622a5626f8848234fbf2bd586ac8c
		if player == "white":
			if kind == "regular":
				cell.king = False
				cell.color = 'white'
<<<<<<< HEAD
				cell.get_child().set_from_file("light_box_white_piece.svg")
			elif kind == "king":
				cell.king = True
				cell.color = 'white'
				cell.get_child().set_from_file("light_box_white_king.svg")
			elif kind == "highlight_regular":
				cell.get_child().set_from_file("light_box_white_piece_available_black.svg")
			elif kind == "highlight_king":
				cell.get_child().set_from_file("light_box_white_king_available_black.svg")
			else:
				cell.get_child().set_from_file("light_box_available_white.svg")
=======
				cell.get_child().set_from_file("images/light_box_white_piece.svg")
			elif kind == "king":
				cell.king = True
				cell.color = 'white'
				cell.get_child().set_from_file("images/light_box_white_king.svg")
			elif kind == "highlight_regular":
				cell.get_child().set_from_file("images/light_box_white_piece_available_black.svg")
			elif kind == "highlight_king":
				cell.get_child().set_from_file("images/light_box_white_king_available_black.svg")
			else:
				cell.get_child().set_from_file("images/light_box_available_white.svg")
>>>>>>> 13d49b04b4b622a5626f8848234fbf2bd586ac8c
		elif player == "black":
			if kind == "regular":
				cell.king = False
				cell.color = 'black'
<<<<<<< HEAD
				cell.get_child().set_from_file("light_box_black_piece.svg")
			elif kind == "king":
				cell.king = True
				cell.color = 'black'
				cell.get_child().set_from_file("light_box_black_king.svg")
			elif kind == "highlight_regular":
				cell.get_child().set_from_file("light_box_black_piece_available_white.svg")
			elif kind == "highlight_king":
				cell.get_child().set_from_file("light_box_black_king_available_white.svg")
			else:
				cell.get_child().set_from_file("light_box_available_white.svg")
		else:
			cell.color = 'none'
			cell.get_child().set_from_file("light_box.svg")

	def get_checker(self, row, column):
		cell = self.table.get_children()[(row*8)+column]
=======
				cell.get_child().set_from_file("images/light_box_black_piece.svg")
			elif kind == "king":
				cell.king = True
				cell.color = 'black'
				cell.get_child().set_from_file("images/light_box_black_king.svg")
			elif kind == "highlight_regular":
				cell.get_child().set_from_file("images/light_box_black_piece_available_white.svg")
			elif kind == "highlight_king":
				cell.get_child().set_from_file("images/light_box_black_king_available_white.svg")
			else:
				cell.get_child().set_from_file("images/light_box_available_white.svg")
		else:
			cell.color = 'none'
			cell.get_child().set_from_file("images/light_box.svg")

	def get_checker(self, row, column):
		cell = self.table.get_children()[(row*8)+(column)]
>>>>>>> 13d49b04b4b622a5626f8848234fbf2bd586ac8c
		return [cell.king, cell.color]

	def update_counter(self, value):
		if self.playing == "whites":
			self.right_label.set_markup('<span size="xx-large">'+str(value)+'</span>')
		else:
			self.left_label.set_markup('<span size="xx-large">'+str(value)+'</span>')

	def exit(self, widget, data=None):
		print "Exiting"
		return self.delete_event(widget)

	def cell_clicked(self, widget, data=None):
<<<<<<< HEAD
		print "Cell clicked"
		# clicked checker variables
		print widget.row
		print widget.column
		# player color
		print widget.color
		# is king
		print widget.king
		self.set_checker(0, 0, None, None)
		self.set_checker(1, 0, "regular", "white")
		self.set_checker(1, 1, "king", "white")
		self.set_checker(1, 2, "highlight_regular", "white")
		self.set_checker(1, 3, "highlight_king", "white")
		self.set_checker(1, 4, None, "white")
		self.set_checker(2, 0, "regular", "black")
		self.set_checker(2, 1, "king", "black")
		self.set_checker(2, 2, "highlight_regular", "black")
		self.set_checker(2, 3, "highlight_king", "black")
		self.set_checker(2, 4, None, "black")
		# returns is_king, player_color
		print self.get_checker(0, 0)
		self.update_counter(10)
		self.win()
		self.change_turn()
=======
		self.controller.player_click(widget)
		
		# clicked checker variables
		#print widget.row
		#print widget.column
		# player color
		#print widget.color
		# is king
		#print widget.king
		#self.set_checker(0, 0, None, None)
		#self.set_checker(1, 0, "regular", "white")
		#self.set_checker(1, 1, "king", "white")
		#self.set_checker(1, 2, "highlight_regular", "white")
		#self.set_checker(1, 3, "highlight_king", "white")
		#self.set_checker(1, 4, None, "white")
		#self.set_checker(2, 0, "regular", "black")
		#self.set_checker(2, 1, "king", "black")
		#self.set_checker(2, 2, "highlight_regular", "black")
		#self.set_checker(2, 3, "highlight_king", "black")
		#self.set_checker(2, 4, None, "black")
		# returns is_king, player_color
		#print self.get_checker(0, 0)
		#self.update_counter(10)
		#self.win()
		#self.change_turn()
>>>>>>> 13d49b04b4b622a5626f8848234fbf2bd586ac8c

	def delete_event(self, widget, event=None, data=None):
		print "destroy signal occurred"
		dialog = gtk.MessageDialog(self.window, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_YES_NO, _("Are you sure you want to exit?"))
		dialog.set_title("Checkers 1.0")
		response = dialog.run()
		dialog.destroy()
		if response == gtk.RESPONSE_YES:
			gtk.main_quit()
			return False
		else:
			return True

<<<<<<< HEAD
	def __init__(self):
=======
	def __init__(self, controller):
		self.controller = controller

>>>>>>> 13d49b04b4b622a5626f8848234fbf2bd586ac8c
		self.playing = "whites"
		self.new_game_button = gtk.Button(_("New Game"))
		self.exit_button = gtk.Button(_("Exit"))
		self.top_box = gtk.HBox(False, 0)
		self.checkers_box = gtk.HBox(False, 0)
		self.main_box = gtk.VBox(False, 0)
		self.p1_box = gtk.VBox(False, 0)
		self.p2_box = gtk.VBox(False, 0)
		self.left_label = gtk.Label("0")
		self.right_label = gtk.Label("0")
		self.black_king_image = gtk.Image()
		self.white_king_image = gtk.Image()
		self.table = gtk.Table(8, 8, True)
		self.ebs =  range( 64 )
		counter = -1
<<<<<<< HEAD
		blacks = [0, 2, 4, 6, 9, 11, 13, 15, 16, 18, 20, 22]
		whites = [41, 43, 45, 47, 48, 50, 52, 54, 57, 59, 61, 63]
		light = False
=======
		blacks = [1, 3, 5, 7, 8, 10, 12, 14, 17, 19, 21, 23]
		whites = [40, 42, 44, 46, 49, 51, 53, 55, 56, 58, 60, 62]
		
		light = True
>>>>>>> 13d49b04b4b622a5626f8848234fbf2bd586ac8c
		for i in range(8):
			light = not light
			for j in range(8):
				counter = counter +1
				self.ebs[counter] = gtk.EventBox()
				self.ebs[counter].row = i
				self.ebs[counter].column = j
				
				if counter in blacks:
					if light == True:
<<<<<<< HEAD
						self.ebs[counter].add(gtk.image_new_from_file('light_box_black_piece.svg'))
					self.ebs[counter].color = 'black'
				elif counter in whites:
					if light == True:
						self.ebs[counter].add(gtk.image_new_from_file('light_box_white_piece.svg'))
					self.ebs[counter].color = 'white'
				else:
					if light == True:
						self.ebs[counter].add(gtk.image_new_from_file('light_box.svg'))
					else:
						self.ebs[counter].add(gtk.image_new_from_file('dark_box.svg'))
=======
						self.ebs[counter].add(gtk.image_new_from_file('images/light_box_black_piece.svg'))
					self.ebs[counter].color = 'black'
				elif counter in whites:
					if light == True:
						self.ebs[counter].add(gtk.image_new_from_file('images/light_box_white_piece.svg'))
					self.ebs[counter].color = 'white'
				else:
					if light == True:
						self.ebs[counter].add(gtk.image_new_from_file('images/light_box.svg'))
					else:
						self.ebs[counter].add(gtk.image_new_from_file('images/dark_box.svg'))
>>>>>>> 13d49b04b4b622a5626f8848234fbf2bd586ac8c
					self.ebs[counter].color = 'none'
				self.ebs[counter].light = light
				light = not light
				self.ebs[counter].king = False
				self.ebs[counter].set_events(gtk.gdk.BUTTON_PRESS_MASK)
				self.ebs[counter].connect("button_press_event", self.cell_clicked)
				self.table.attach(self.ebs[counter], j, j+1, i, i+1)
		
<<<<<<< HEAD
		self.black_king_image.set_from_file('black_king.svg')
		self.white_king_image.set_from_file('white_king.svg')
=======
		self.black_king_image.set_from_file('images/black_king.svg')
		self.white_king_image.set_from_file('images/white_king.svg')
>>>>>>> 13d49b04b4b622a5626f8848234fbf2bd586ac8c
		
		self.left_label.set_markup('<span size="xx-large">0</span>')
		self.right_label.set_markup('<span size="xx-large">0</span>')
		
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title('Checkers')
		self.window.connect("delete_event", self.delete_event)
		self.new_game_button.connect("clicked", self.new_game, None)
		self.exit_button.connect("clicked", self.exit, None)
		
		self.top_box.pack_start(self.new_game_button, False, False, 5)
		self.top_box.pack_end(self.exit_button, False, False, 5)
		self.main_box.pack_start(self.top_box, False, True, 5)
		self.p1_box.pack_start(self.black_king_image, False, False, 0)
		self.p1_box.pack_start(self.left_label, False, False, 0)
		self.checkers_box.pack_start(self.p1_box, False, False, 5)
		self.checkers_box.pack_start(self.table, True, False, 0)
		self.p2_box.pack_start(self.white_king_image, False, False, 0)
		self.p2_box.pack_start(self.right_label, False, False, 0)
		self.checkers_box.pack_end(self.p2_box, False, False, 5)
		self.main_box.pack_start(self.checkers_box, True, True, 5)
		self.window.add(self.main_box)
		
		self.window.show_all()

	def main(self):
		gtk.main()

if __name__ == "__main__":
	checkers = CheckersGUI()
	checkers.main()
