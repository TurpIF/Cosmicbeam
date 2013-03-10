from PySFML import sf
import Geometry
from Engine import Obstacle
import Game

class Circle(Obstacle):
	img1 = sf.Image()
	img1.LoadFromFile("./img/planete_1.png")
	
	img2 = sf.Image()
	img2.LoadFromFile("./img/planete_2.png")
	
	img3 = sf.Image()
	img3.LoadFromFile("./img/planete_3.png")
	
	img4 = sf.Image()
	img4.LoadFromFile("./img/planete_4.png")
	
	def __init__(self,x,y,r):
		self.x = x
		self.y = y
		self.r = r
		
		if r == 1:
			self.r = 25
			
			if Game.Game.high_perf_mode:
				self.spr = sf.Shape.Circle(0, 0, self.r, sf.Color(170, 0, 0), 0, sf.Color(127, 127, 127))
				self.spr.SetPosition(self.x, self.y)
			else:
				self.spr = sf.Sprite(self.img1)
				self.spr.SetPosition(self.x - self.spr.GetSize()[0]/2, self.y - self.spr.GetSize()[1]/2)
		
		elif r == 2:
			self.r = 35
			
			if Game.Game.high_perf_mode:
				self.spr = sf.Shape.Circle(0, 0, self.r, sf.Color(170, 0, 0), 0, sf.Color(127, 127, 127))
				self.spr.SetPosition(self.x, self.y)
			else:
				self.spr = sf.Sprite(self.img2)
				self.spr.SetPosition(self.x - self.spr.GetSize()[0]/2, self.y - self.spr.GetSize()[1]/2)
		
		elif r == 3:
			self.r = 50
			
			if Game.Game.high_perf_mode:
				self.spr = sf.Shape.Circle(0, 0, self.r, sf.Color(170, 0, 0), 0, sf.Color(127, 127, 127))
				self.spr.SetPosition(self.x, self.y)
			else:
				self.spr = sf.Sprite(self.img3)
				self.spr.SetPosition(self.x - self.spr.GetSize()[0]/2, self.y - self.spr.GetSize()[1]/2)
		
		else:
			self.r = 75
			
			if Game.Game.high_perf_mode:
				self.spr = sf.Shape.Circle(0, 0, self.r, sf.Color(170, 0, 0), 0, sf.Color(127, 127, 127))
				self.spr.SetPosition(self.x, self.y)
			else:
				self.spr = sf.Sprite(self.img4)
				self.spr.SetPosition(self.x - self.spr.GetSize()[0]/2, self.y - self.spr.GetSize()[1]/2)
		
		# self.shape = sf.Shape.Circle(self.x, self.y, r, sf.Color(170, 0, 0))
	
	def collides(self,p):
		#print Geometry.distance(self.x,self.y,p.x,p.y), self.r
		if Geometry.distance(self.x,self.y,p.x,p.y) < self.r:
			p.kill()
			return True
		else:
			return False
	
	def drawTo(self, window):
		window.Draw(self.spr)

