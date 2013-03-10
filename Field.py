import Geometry
import Game

from PySFML import sf

class Field:
	def apply(self, particule, dt):
		raise Exception("Not implemented")
	
	def drawTo(self, window):
		raise Exception("Not implemented")

class BlackHoleField(Field):
	img = sf.Image()
	img.LoadFromFile("./img/black_hole.png")
	
	def __init__(self, x, y, intensity, cached = True):
		self.x = x
		self.y = y
		self.intensity = intensity
		if Game.Game.high_perf_mode:
			self.spr = sf.Shape.Circle(0, 0, 50, sf.Color(155, 155, 155), 0, sf.Color(127, 127, 127))
			self.spr.SetPosition(self.x, self.y)
		else:
			self.spr = sf.Sprite(self.img)
			self.spr.SetPosition(self.x - self.spr.GetSize()[0]/2, self.y - self.spr.GetSize()[1]/2)
		
		
		self.cache = {}
		self.cached = cached
		
	def apply(self, particule, dt):
		if self.cached and (particule.x, particule.y) in self.cache:
			rx, ry = self.cache[(particule.x, particule.y)]
		else:
			distance = Geometry.distance(particule.x, particule.y, self.x, self.y) 
			er = (particule.x - self.x) / distance, (particule.y - self.y) / distance
			g = - self.intensity / distance ** 2
			rx, ry = g * er[0], g * er[1]
			self.cache[(particule.x, particule.y)] = (rx,ry)
		particule.vx += rx * dt
		particule.vy += ry * dt
			
	def drawTo(self, window):
		window.Draw(self.spr)

class AntiBlackHoleField(Field):
	img = sf.Image()
	img.LoadFromFile("./img/white_hole.png")
	
	def __init__(self, x, y, intensity, cached = True):
		self.x = x
		self.y = y
		self.intensity = intensity
		
		if Game.Game.high_perf_mode:
			self.spr = sf.Shape.Circle(0, 0, 50, sf.Color(255, 255, 255), 0, sf.Color(127, 127, 127))
			self.spr.SetPosition(self.x, self.y)
		else:
			self.spr = sf.Sprite(self.img)
			self.spr.SetPosition(self.x - self.spr.GetSize()[0]/2, self.y - self.spr.GetSize()[1]/2)
		
		
		self.cache = {}
		self.cached = cached
	
	def apply(self, particule, dt):
		if self.cached and (particule.x, particule.y) in self.cache:
			rx, ry = self.cache[(particule.x, particule.y)]
		else:
			distance = Geometry.distance(particule.x, particule.y, self.x, self.y) 

			er = (particule.x - self.x) / distance, (particule.y - self.y) / distance
			g = self.intensity / distance ** 2
			rx, ry = g * er[0], g * er[1]
			self.cache[(particule.x, particule.y)] = (rx,ry)
		particule.vx += rx * dt
		particule.vy += ry * dt
	
	def drawTo(self, window):
		window.Draw(self.spr)
