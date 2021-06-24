import tkinter as tk
from tkinter import ttk

class Login_Page(tk.Frame):
	def __init__(self,parent,App):
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

		self.Choose_level()
		self.Choose_Username()


	def Choose_level(self):
		self.choose_level = tk.Label(self.main_frame,text='Level :',font = ('Arial',18,"bold"),bg = 'blue',fg='white')
		self.choose_level.pack(pady = 5)
		option = [1,2,3,4,5,6]
		self.clicked = tk.StringVar()
		self.clicked.set(option[0])
		self.drop = tk.OptionMenu(self.main_frame,self.clicked,*option)
		self.drop.pack(pady=20)
		
	def Choose_Username(self):
		self.label_Username = tk.Label(self.main_frame,text='username',font = ('Arial',18,"bold"),bg = 'blue',fg='white')
		self.label_Username.pack(pady = 5)
		self.var_username = tk.StringVar()
		self.entry_username = tk.Entry(self.main_frame,font =("Arial",16,'bold'), textvariable = self.var_username)
		self.entry_username.pack(pady = 5)
		self.btn_login = tk.Button(self.main_frame,text="LOGIN",font=('Arial',18,'bold'),command = lambda: self.application.auth_login())
		self.btn_login.pack(pady=5)