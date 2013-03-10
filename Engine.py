#from Geometry import *

class Obstacle:
	def __init__(self):
		pass
	
	def collides(self,p):
		raise Exception("Not implemented")
	
	def drawTo(self, window):
		raise Exception("Not implemented")

class Engine:
	def __init__(self, width = 2000, height = 2000, receptors = [], emitters = []):
		
		#self.max_particles = 700
		self.max_particles = 20
		self.generated_particles = 0
		self.dead_particles = 0
		self.computed_frames = 0
		self.received_particles = 0
		self.particles = set()
		self.obstacles = []
		self.fields = []
		self.medium = []
		
		self.width = width
		self.height = height
	
		self.receptors = receptors
		self.emitters = emitters
	
	def victory(self):
		return len([0 for r in self.receptors if r.point >= r.minimum]) == len(self.receptors)
	
	def next_frame(self, dt):
		self.computed_frames += 1
		
		for e in self.emitters:
			e.add_particle(self)
		
		lsRemove = set()
		for p in self.particles:
			"""
			p.old_x = p.x
			p.old_y = p.y
			if p.leader is None:
				for f in self.fields:
					f.apply(p, dt);
				p.x += p.vx * dt
				p.y += p.vy * dt
			else:
				p.x = 
			"""
			
			p.old_x = p.x
			p.old_y = p.y
			for f in self.fields:
				f.apply(p, dt);
			p.x += p.vx * dt
			p.y += p.vy * dt
			
			for p in self.particles:
				if p.engine is not None:
					alive = True
					for s in self.receptors:
						if (p.x >= (self.width - s.width / 2.0) and p.y >= s.y and p.y <= (s.y + s.height) ):
							s.point += 1
							self.received_particles += 1
							self.rem_part(p)
							alive = False
							break
			
					if alive and p.x < 0 or p.y < 0 or p.x > self.width or p.y > self.height:
						#print "Removing part: ",p.x, p.y
						p.kill()
						alive = False
				
					if alive:
						for m in self.medium:
							m.apply(p, dt)
							m.collides(p)
			
					if alive:
						for o in self.obstacles:
							if o.collides(p):
								pass #print "lol"
				
					if not alive:
						lsRemove.add(p)
				else:
					lsRemove.add(p)
		
		self.particles = self.particles - lsRemove
	
	def add_part(self,p):
		self.particles.add(p)
		p.engine = self
		self.generated_particles += 1
		#print "added part!",self
	
	def rem_part(self, p):
		#self.particles.remove(p)
		p.engine = None

def main():
	print "Initializing engine..."
	e = Engine()
	print "Ending game..."

if __name__ == '__main__':
	main()


