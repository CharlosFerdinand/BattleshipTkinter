import tkinter as tk
from random import randint

from ship import Ship
from player import Player
from config import Config
from board import Board
from login_page import Login_Page
from Login_Board import LoginBoard
from Login_Board2 import LoginBoard2




class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game
		self.config = Game.config

		super().__init__()
		self.title(self.config.app_title)
		self.geometry(self.config.screen)

		self.create_container()

		self.pages = {}
		self.create_login_page()

	def change_page(self,page):
		self.create_board()
		page = self.pages[page]
		page.tkraise()

	def Retry(self):
		self.change_page('LoginPage')
		self.location = self.game.ship.setup_location()

	def create_container(self):
		self.container = tk.Frame(self, bg="white")
		self.container.pack(fill="both", expand=True)

	def create_board(self):
		self.pages["board"] = Board(self.container, self.game)

	def create_Login_Board(self):
		self.pages["Login_Board"] = LoginBoard(self.container, self.game)

	def create_Login_Board2(self):
		self.pages["Login_Board2"] = LoginBoard2(self.container, self.game)

	def create_login_page(self):
		self.pages['LoginPage'] = Login_Page(self.container,self.game)



class Battleship:

	def __init__(self):
		self.config = Config()
		self.ship = Ship(self)
		self.player = Player()
		self.window = Window(self)
		
	def check_Answer(self):
		self.location = self.ship.setup_location()
		player = self.player.location
		if self.location == player:
			return True
		return False


	def button_clicked(self,x,y,button):
		self.player.current_location(x,y)
		win = self.check_Answer()
		self.window.pages['board'].change_img_button(x,y,win)


	def get_level(self):
		level = (self.window.pages['LoginPage'].clicked.get())
		return level

	def auth_login(self):
		self.level = self.get_level()
		self.Username = self.window.pages['LoginPage'].var_username.get()
		self.player = Player(self.Username)
		self.config = Config(int(self.level))
		self.window.change_page('board')

	def run(self):
		self.window.mainloop()

if __name__ == '__main__':
	my_battleship = Battleship()
	my_battleship.run()