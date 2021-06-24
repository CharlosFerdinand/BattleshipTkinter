from random import randint

class Ship:
	def __init__(self,Game):
		self.config = Game.config
		self.setup_location()

	def setup_location(self):
		x = randint(0,self.config.row-1)
		y = randint(0,self.config.column-1)
		setup_locations = (x,y)
		return setup_locations

