from Particle import Particle

class Emitter:
	def __init__(self, x, y, vx, vy, color, nbr):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.color = color
		self.nbr = 0
		self.nbrMax = nbr
		
	
	def add_particle(self, engine):
		if self.nbr < self.nbrMax:
			engine.add_part(Particle(self.x, self.y, self.vx, self.vy, self.color))
			self.nbr += 1

