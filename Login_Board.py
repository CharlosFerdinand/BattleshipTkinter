import pygame
import tkinter as tk

class LoginBoard(tk.Frame):

	def __init__(self, parent, App):

		# Parent setting
		self.application = App
		self.config = App.config
		self.screen = self.config.side

		super().__init__(parent)
		self.configure(bg = 'blue')
		self.grid(row=0,column=0,sticky = 'nsew')
		parent.grid_columnconfigure(0,weight = 1)
		parent.grid_rowconfigure(0,weight=1)

		#CREATE MAIN FRAME
		self.main_frame = tk.Frame(self,height = self.screen,width=self.screen,bg = 'blue')
		self.main_frame.pack(expand = True)

		self.label_Username = tk.Label(self.main_frame,text='YOU WIN!!!',font = ('Arial',18,"bold"),bg = 'blue',fg='white')
		self.label_Username.pack(pady = 5)

		self.btn_login = tk.Button(self.main_frame,text="RETRY",font=('Arial',18,'bold'),command = lambda: self.application.window.Retry())
		self.btn_login.pack(pady=5)

		self.config.play_win_sound()
