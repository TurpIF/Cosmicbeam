from PySFML import sf
import Geometry
from Engine import Obstacle
from math import *

class Mirror(Obstacle):

	use_imgs = False

	img = sf.Image()
	#img.LoadFromFile("./img/mirror_bg.png")
	img.LoadFromFile("./img/mirror_bg_big.png")
	
	def __init__(self, x1, y1, x2, y2, is_a_barrier = False):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.is_a_barrier = is_a_barrier
		
		if is_a_barrier:
			self.shape = sf.Shape.Line(self.x1, self.y1, self.x2, self.y2, 6, sf.Color(100, 0, 0))
		else:
			self.shape = sf.Shape.Line(self.x1, self.y1, self.x2, self.y2, 4, sf.Color(150, 150, 190))
			
			if Mirror.use_imgs:
				self.sprMirror = sf.Sprite(Mirror.img)
				self.length = Geometry.distance(x1,y1,x2,y2)
				
				#self.angle = abs(atan((x2-x1)/(self.length)))
				#self.angle = atan((x2-x1)/(self.length))
				self.angle = atan((x2-x1)/(y2-y1))
				self.sprMirror.SetRotation(degrees(self.angle)+90)
				#self.sprMirror.SetRotation(45)
				self.shape = sf.Shape.Line(self.x1, self.y1, self.x2, self.y2, 2, sf.Color(150, 150, 150))

	
	def collides(self,p):
		#if Geometry.intersec_seg(self,{'x':p}):
		#try:
		#	if Geometry.intersect(self.x1,self.y1,self.x2,self.y2,p.x,p.y,p.old_x,p.old_y):
		#		p.kill()
		#except ZeroDivisionError:
		#	pass
		i = Geometry.intersect_seg(self.x1,self.y1,self.x2,self.y2,p.x,p.y,p.old_x,p.old_y)
		#if i is not None: p.kill()
		#if i is not None: p.engine.rem_part(p)
		if i is not None:
			if self.is_a_barrier:
				p.kill()
			else:
				#print "Mirror intersection!! ", p.id
				# ix,iy = i
				# p.x = ix
				# p.y = iy
				# p.x = p.old_x
				# p.y = p.old_y
				p.x = (i[0]*9+p.old_x)/10.0
				p.y = (i[1]*9+p.old_y)/10.0
				p.vx, p.vy = Geometry.reflect(self.x2-self.x1, self.y2-self.y1, p.vx, p.vy)
		
	def drawTo(self, window):
		if self.is_a_barrier:
			window.Draw(self.shape)
		else:
			window.Draw(self.shape)
			"""
			for i in range(int(self.length)):
				self.sprMirror.SetPosition(self.x1+i*tan(self.angle), self.y1 + i)
				#window.Draw(self.sprMirror)
				#self.sprMirror.SetPosition(self.x1+i, self.y1 + i)
				window.Draw(self.sprMirror)
			"""
			"""
			man_dist = int(abs(self.x1-self.x2) + abs(self.y1-self.y2))/20
			for i in range(man_dist):
				x = self.x1+i*(self.x2-self.x1)/man_dist
				y = self.y1+i*(self.y2-self.y1)/man_dist
				self.sprMirror.SetPosition(x,y)
				window.Draw(self.sprMirror)
			#self.sprMirror.SetPosition(self.x1, self.y1)
			#window.Draw(self.sprMirror)
			#window.Draw(self.img)
			"""
			"""
			x = self.x1
			y = self.y1
			for i in range(int(self.length/20)):
				x = self.x1+(self.x2-self.x1)/20*i
				y = self.y1+(self.y2-self.y1)/20*i
				self.sprMirror.SetPosition(x,y)
				window.Draw(self.sprMirror)
			"""
			if Mirror.use_imgs:
				img_len = 9.5
				x = self.x1
				y = self.y1
				xinc = (self.x2-self.x1)/self.length*img_len
				yinc = (self.y2-self.y1)/self.length*img_len
				for i in range(int(self.length/img_len)+1):
				#while x < self.x2 and y < self.y2:
					self.sprMirror.SetPosition(x,y)
					window.Draw(self.sprMirror)
					x += xinc
					y += yinc
			





