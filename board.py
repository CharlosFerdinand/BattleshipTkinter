import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime




class Board(tk.Frame):

	def __init__(self, parent, Game):

		self.game = Game #battleship object
		self.config = Game.config #Config dalam battelship
		self.life = Game.config.life
		self.player_name = Game.player.name

		# Config time
		self.start_time = datetime.now()
		self.start_menit = self.start_time.minute
		self.start_detik = self.start_time.second
		
		#CONFIG FRAME
		super().__init__(parent)
		self.configure(bg="black")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		#CONFIG BUTTON
		self.buttonPixel = tk.PhotoImage(width=1, height=1)

		self.create_mainframe()
		self.update_board()
		
	# Create Board
	def create_mainframe(self):
		self.mainframe = tk.Frame(self, height=self.config.side, width=self.config.side, bg="black")
		self.mainframe.pack(expand=True)

	def create_board(self):
		self.frame_rows = [] # [0, 1, 2, 3, 4]
		color = 756867 #hexadecimal code

		n_row, n_column = self.config.row, self.config.column
		row_height, row_width = self.config.side//n_row, self.config.side

		for i in range(n_row):
			row_color = f"#{color}"
			frame = tk.Frame(self.mainframe, height=row_height, width=row_width, bg=row_color)
			self.frame_rows.append(frame)
			color += 500

	def show_board(self):
		for frame in self.frame_rows:
			frame.pack()

	# Photo configuration

	def put_and_resize_photo(self,oriImg,scale):
		n_column = self.config.column
		button_width = self.config.side//n_column-10

		image = Image.open(oriImg)
		image_w,image_h = image.size
		ratio = image_w/button_width
		image = image.resize((int(image_w//ratio//scale),int(image_h//ratio//scale)))
	
		return ImageTk.PhotoImage(image)

	def change_img_button(self, x, y, win):
		if win:
			img = self.init_img_win
			self.Create_new_score(self.life)
			self.game.window.create_Login_Board()
		else:
			img = self.init_img_wrong
			self.life -= 1
		if self.life == 0 :
			self.game.window.create_Login_Board2()
		self.button_board[x][y].configure(image= img,command = lambda:None)


	 # Time Calculation
	def Time_calculation(self):
		last_time = datetime.now()
		last_menit = last_time.minute
		last_detik = last_time.second
		first_time_Calculation = self.start_detik + (self.start_menit*60)
		last_time_Calculation = last_detik + (last_menit*60)
		time = last_time_Calculation - first_time_Calculation
		return time

	
	def Create_new_score(self,life_spawn):
		time = self.Time_calculation()
		data = {self.player_name:{'sisa life':life_spawn,'waktu':time}} 
		self.config.Write_Data(data)

	def create_button_board(self):
		self.button_board = []
		n_row, n_column = self.config.row, self.config.column
		button_height, button_width = self.config.side//n_row-10, self.config.side//n_column-10

		self.init_img_btn = self.put_and_resize_photo(oriImg=self.config.first_logo,scale=2)
		self.init_img_wrong = self.put_and_resize_photo(oriImg=self.config.lose_logo,scale=2)
		self.init_img_win = self.put_and_resize_photo(oriImg=self.config.win_logo,scale=2)

		for i in range(n_row):
			row = []
			for j in range(n_column):
				button = tk.Button(self.frame_rows[i], bg="black", image=self.init_img_btn, compound="c", height=button_height, width=button_width,command= lambda x=i,y=j: self.game.button_clicked(x,y,self.button_board))
				row.append(button)
			self.button_board.append(row)


	def show_button_board(self):
		n_row, n_column = self.config.row, self.config.column
		for i in range(n_row):
			for j in range(n_column):
				self.button_board[i][j].pack(side="left")
			
	def update_board(self):
		self.create_board()
		self.show_board()
		self.create_button_board()
		self.show_button_board()