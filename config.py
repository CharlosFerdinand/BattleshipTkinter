from json import load,dump
from random import uniform
import tkinter as tk
import pygame

class Config:

	def __init__(self,level_data=1):
		self.app_title = "Battleship"
		self.data_place = "PlayerScore_Data.Json"


		#GAME CONFIG
		self.row = level_data+1 #Change with level
		self.column = level_data+1 #Change With level
		self.life = level_data+1 #Change with Level

		#WINDOW CONFIG
		base = 100
		ratio = 5
		self.side = base*ratio
		self.screen = f"{self.side}x{self.side}+500+400"

		self.first_logo = 'IMG/awal.png'
		self.lose_logo = 'IMG/kalah.png'
		self.win_logo = 'IMG/menang.jpg'
		self.lose_sound = 'SOUND/3.mp3'
		self.win_sound = 'SOUND/2.mp3'

	def Read_data(self):
		with open(self.data_place,'r') as data_place:
			self.score = load(data_place)

	def Write_Data(self,data):
		self.Read_data()
		new_score = data
		self.score.update(new_score)
		with open(self.data_place,'w') as data_place:
			dump(self.score,data_place)

	def play_lose_sound(self):
		pygame.init()
		pygame.mixer.init()
		sound = pygame.mixer.Sound(self.lose_sound)
		sound.set_volume(uniform(0.1, 0.5))
		sound.play()  

	def play_win_sound(self):
		pygame.init()
		pygame.mixer.init()
		sound = pygame.mixer.Sound(self.win_sound)
		sound.set_volume(uniform(1.5, 2))
		sound.play()
