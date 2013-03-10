from PySFML import sf
import Geometry
import math

from Engine import Obstacle
from Field import Field

class Medium(Obstacle, Field):
	def __init__(self, points, indice, color = sf.Color(255, 255, 255)):
		self.points = points
		self.indice = indice
		self.color = color
		self.color.a = 100
		
		self.shape = sf.Shape()
		self.shape.SetColor(self.color)
		for p in self.points:
			self.shape.AddPoint(p[0], p[1], self.color)
		
		self.inside = {}
	
	def apply(self, p, dt):
		if p in self.inside and self.inside[p]:
			pass
	
	def collides(self,p):
		def _collides(x1, y1, x2, y2, x3, y3, x4, y4):
			i = Geometry.intersect_seg(x1, y1, x2, y2, x3, y3, x4, y4)
			
			if i is not None:
				if y2 == y1:	n = 0 + math.pi / 2.0
				else:			n = math.atan((x2 - x1) / (y2 - y1)) + math.pi / 2.0
				
				if y4 == y3:	i1 = 0 - n
				else:			i1 = math.atan((x4 - x3) / (y4 - y3)) - n
				
				#i1 = math.pi / 2 - Geometry.angle(x1, y1, x2, y2, x3, y3, x4, y4)
				
				if self.indice == p.last_indice:
					n1 = self.indice
					n2 = p.last_indice
				else:
					n1 = p.last_indice
					n2 = self.indice
				
				sini2 = math.sin(i1) * n1 / n2
				if math.fabs(sini2) <= 1:
					i2 = math.asin(sini2)
					#print i2 / math.pi * 360
					
					c = math.cos(-i1 + math.pi + i2)
					s = math.sin(-i1 + math.pi + i2)
					vx = p.vx * c - p.vy * s
					vy = p.vx * s + p.vy * c
					p.vx = vx
					p.vy = vy
					
					print 180 * i1 / math.pi, 180 * i2 / math.pi

					if not p in self.inside:
						self.inside[p] = True
					else:
						self.inside[p] = not self.inside[p]
					if not self.inside[p]:
						p.last_indice = self.indice
				else:
					#print 'coucou'
					c = math.cos(-2 * i1)
					s = math.sin(-2 * i1)
					vx = p.vx * c - p.vy * s
					vy = p.vx * s + p.vy * c
					#p.vx = vx
					#p.vy = vy
				
				return True
			return False
		
		if len(self.points) >= 2:
			for p1, p2 in zip(self.points, self.points[1:] + [self.points[0]]):
				if _collides(p1[0], p1[1], p2[0], p2[1], p.x, p.y, p.old_x, p.old_y):
					break
			
		
	def drawTo(self, window):
		window.Draw(self.shape)

