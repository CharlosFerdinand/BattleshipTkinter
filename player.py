class Player(object):

	def __init__(self, name='John'):
		self.name = name
		self.steps = 0

	def current_location(self,pos_x,pos_y):
		self.location = (pos_x,pos_y)
		