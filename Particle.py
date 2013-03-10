from PySFML import sf

class Particle:
	nb = 0
	def __init__(self, x = 0, y = 0, vx = 0, vy = 0, color = sf.Color(255, 255, 255), engine = None, leader = None):
		self.id = Particle.nb
		Particle.nb += 1
		self.x = x
		self.y = y
		self.old_x = x
		self.old_y = y
		self.vx = vx
		self.vy = vy
		self.color = color
		self.last_indice = 1.0
		self.engine = None
		if engine is not None:
			engine.add_part(self)
		#print "new part!"
		#self.shape = sf.Shape.Circle(self.x, self.y, 3, sf.Color(255, 255, 255), 0, sf.Color(127, 127, 127))
		self.shape = sf.Shape.Circle(0, 0, 3, self.color, 0, sf.Color(127, 127, 127))
		#self.shape = sf.Shape.Line(0, 0, 0, 0, 5, sf.Color(127, 127, 127))
	
	def drawTo(self, window):
		self.shape.SetPosition(self.x, self.y)
		window.Draw(self.shape)
		shape = sf.Shape.Line(self.old_x, self.old_y, self.x, self.y, 6, self.color)
		#shape = sf.Shape.Line(self.old_x, self.old_y, self.x, self.y, 6, sf.Color(200, 200, 100))
		window.Draw(shape)

	def kill(self):
		self.engine.dead_particles += 1
		self.engine.rem_part(self)
