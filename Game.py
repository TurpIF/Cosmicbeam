from PySFML import sf
from Engine import *
import Geometry
import sys
import time

from Receptor import Receptor
from Emitter import Emitter
from Particle import Particle
from Mirror import Mirror
from Circle import Circle
from Field import *
from Medium import Medium

class Game:
	#time_delta = 1.0/40.0
	time_delta = 1.0/10.0
	
	high_perf_mode = True
	
	def __init__(self, window):
		self.window = window
		self.window.SetFramerateLimit(50)
		self.running = False
		#self.speedView = 10.0
		#self.speedView = 500.0
		self.view = self.window.GetDefaultView()
		self.clock = sf.Clock()
		
		self.speedView = 8.0
		self.view_move_speed_x = 0.0
		self.view_move_speed_y = 0.0
		self.view_move_speed_damping = .8
		self.max_mirror_size = 200
		
		#self.max_particles = 700
		#self.max_particles = 20
		self.max_particles = 600
		self.particles_to_receive = 500
		
		
		#INITIALIZING THE TEXT'S FONT
		self.GameOver = sf.Font()
		self.GameOver.LoadFromFile("./fonts/game_over.ttf")
		
		#INITIALIZING THE TEXT
		self.Text = sf.String()
		
		self.sprReceptors = []
		self.sprEmitters = []
		
		self.victory = False
		self.paused = False
		
		self.sprPause = sf.Shape.Rectangle(0, 0, self.window.GetWidth(), self.window.GetHeight(), sf.Color(0, 0, 0, 175))
		
		self.timeBegin = time.time()
		self.timeEnd = time.time()
		self.construct()
	
	def construct(self):
		raise Exception("Not implemented")
	
	def run(self):
		self.running = True
		while self.running:
			self.event()
			self.draw()
	
	def get_offset(self):
		cx, cy = self.view.GetCenter()
		hsx, hsy = self.view.GetHalfSize()
		return (cx - hsx, cy - hsy)
	
	def cmd_move_view(self,sx,sy):
		#TODO : Bloquer la camera pour qu'elle ne depasse pas les limites de l'ecran
		self.view_move_speed_x += sx
		self.view_move_speed_y += sy
	
	def event(self):
		elapsedTime = self.clock.GetElapsedTime()
		self.clock.Reset()
		
		if not self.victory and not self.paused:
			#self.engine.next_frame(elapsedTime)
			self.engine.next_frame(Game.time_delta)
		
		# if elapsedTime != 0:	print 1.0 / elapsedTime
		
		event = sf.Event()
		while self.window.GetEvent(event):
			if event.Type == sf.Event.Closed:
				self.running = False
				sys.exit()
			
			if not self.victory and not self.paused:
				if event.Type == sf.Event.MouseButtonPressed and event.MouseButton.Button == sf.Mouse.Left:
					self.posMouse = (event.MouseButton.X, event.MouseButton.Y)
			
				if self.posMouse and event.Type == sf.Event.MouseButtonReleased and event.MouseButton.Button == sf.Mouse.Left:
					p = (event.MouseButton.X, event.MouseButton.Y)
					if self.posMouse[0] != p[0] or self.posMouse[1] != p[1]:
						print 'Ajout d\'un mirroir : (' + str(self.posMouse[0]) + ' ; ' + str(self.posMouse[1]) + ') -> (' + str(p[0]) + ' ; ' + str(p[1]) + ')';
						#mouse_offset = self.view.GetCenter() - self.view.GetHalfSize()
						ox, oy = self.get_offset()
						x1, y1 = self.posMouse[0]+ox, self.posMouse[1]+oy
						x2, y2 = Geometry.maximize_vector(x1, y1, p[0]+ox, p[1]+oy, self.max_mirror_size)
						self.engine.obstacles += [Mirror(x1, y1, x2, y2)]

					self.posMouse = None
			
			if not self.victory and self.engine.victory() and event.Type == sf.Event.KeyPressed and event.Key.Code == sf.Key.Return:
				self.victory = True
				self.paused = True
				self.timeEnd = time.time()
			
			if event.Type == sf.Event.KeyPressed and event.Key.Code == sf.Key.R:
				self.timeBegin = time.time()
				self.victory = False
				self.paused = False
				self.construct()
			
			if event.Type == sf.Event.KeyPressed and event.Key.Code == sf.Key.N:
				self.running = False
			
			if not self.victory and event.Type == sf.Event.KeyPressed and event.Key.Code == sf.Key.Escape:
				self.paused = not self.paused
		
		self.view_move_speed_x *= self.view_move_speed_damping
		self.view_move_speed_y *= self.view_move_speed_damping
		
		if not self.paused:
			# J'aime les poneys...
			if self.window.GetInput().IsKeyDown(sf.Key.Up):
				#self.view.Move(0, -self.speedView * elapsedTime)
				self.cmd_move_view(0,-self.speedView)
		
			if self.window.GetInput().IsKeyDown(sf.Key.Down):
				#self.view.Move(0, self.speedView * elapsedTime)
				self.cmd_move_view(0,self.speedView)
		
			if self.window.GetInput().IsKeyDown(sf.Key.Left):
				#self.view.Move(-self.speedView * elapsedTime, 0)
				self.cmd_move_view(-self.speedView,0)
		
			if self.window.GetInput().IsKeyDown(sf.Key.Right):
				#self.view.Move(self.speedView * elapsedTime, 0)
				self.cmd_move_view(self.speedView,0)
			
			mx, my = self.window.GetInput().GetMouseX(), self.window.GetInput().GetMouseY()
			if mx < self.window.GetWidth() * 0.2:
				self.cmd_move_view(-self.speedView * (2.0 * (1.0 - 5.0 * (mx * 1.0 / self.window.GetWidth()))), 0)
			if mx > self.window.GetWidth() * 0.8:
				self.cmd_move_view(self.speedView * (2.0 * 5.0 * (mx * 1.0 / self.window.GetWidth() - 0.8)), 0)
			if my < self.window.GetHeight() * 0.2:
				self.cmd_move_view(0, -self.speedView * (2.0 * (1.0 - 5.0 * (my * 1.0 / self.window.GetHeight()))))
			if my > self.window.GetHeight() * 0.8:
				self.cmd_move_view(0, self.speedView * (2.0 * 5.0 * (my * 1.0 / self.window.GetHeight() - 0.8)))
		
		x1, y1 =  self.get_offset()
		x1, y1 = x1 + self.view_move_speed_x , y1 + self.view_move_speed_y
		x2, y2 = x1 + self.window.GetWidth(), y1 + self.window.GetHeight()
		
		xCenter = x1 + self.window.GetWidth()/2.0
		yCenter = y1 + self.window.GetHeight()/2.0
		
		if (x1 < 0):
			xCenter = self.window.GetWidth()/2.0
		if (y1 < 0):
			yCenter = self.window.GetHeight()/2.0
		if (x2 > self.max_width):
			xCenter = self.max_width - self.window.GetWidth()/2.0
		if (y2 > self.max_height):
			yCenter = self.max_height - self.window.GetHeight()/2.0
			
		self.view.SetCenter(xCenter, yCenter)


	
	def draw(self):
		self.window.SetView(self.view)
		self.window.Clear()
		
		for x in range(self.max_width/int(self.sprBackgroundTile.GetSize()[0]) + 1):
			self.sprBackgroundTile.SetPosition(x*self.sprBackgroundTile.GetSize()[0], 0)
			self.window.Draw(self.sprBackgroundTile)
			
	
		for e in self.sprEmitters:
			self.window.Draw(e)
		
		for r in self.sprReceptors:
			self.window.Draw(r)
		
		# for p in self.engine.particles:
			# p.drawTo(self.window)
		
		#if not Game.high_perf_mode:
		for f in self.engine.fields:
			f.drawTo(self.window)
		
		for o in self.engine.obstacles:
			o.drawTo(self.window)
		
		for m in self.engine.medium:
			m.drawTo(self.window)
		
		for p in self.engine.particles:
			p.drawTo(self.window)
		
		if self.paused:
			self.window.Draw(self.sprPause)
		
		if self.posMouse:
			x0, y0 = self.posMouse
			x1, y1 = Geometry.maximize_vector(x0, y0, self.window.GetInput().GetMouseX(), self.window.GetInput().GetMouseY(), self.max_mirror_size)
			if self.posMouse[0] != self.window.GetInput().GetMouseX() or self.posMouse[1] != self.window.GetInput().GetMouseY():
				ox, oy = self.get_offset()
				shape = sf.Shape.Line(x0+ox, y0+oy, x1+ox, y1+oy, 2, sf.Color(200, 42, 42))
				self.window.Draw(shape)
				
		self.Text = sf.String("GENERAL INFOS : " + str(self.engine.dead_particles) + " dead particles  |  " +  str(self.engine.generated_particles) + " generated particles" ,
		self.GameOver, 40)
		self.Text.SetPosition(self.get_offset()[0] + 20, self.get_offset()[1] )
		self.window.Draw(self.Text)
				
		for i in range(len(self.receptors)):
			self.Text = sf.String("RECEPTOR " + str(i+1) + " : " + str(self.receptors[i].point) + "/" + str(self.receptors[i].minimum) + " received particles",
			self.GameOver, 40)
			self.Text.SetPosition(self.get_offset()[0] + 20, self.get_offset()[1] + 30*(i+1))
			self.window.Draw(self.Text)
		
		if not self.victory and self.engine.victory():
			self.Text = sf.String("PRESS ENTER !!!", self.GameOver, 80)
			self.Text.SetPosition(self.window.GetWidth() - 300, self.window.GetHeight() - 100)
			self.window.Draw(self.Text)
		
		if self.paused:
			self.Text = sf.String("R - RECOMMENCER | N - NEXT LEVEL", self.GameOver, 40)
			self.Text.SetPosition(self.window.GetWidth() / 2.0 - 200, self.window.GetHeight() / 2.0 - 30)
			self.window.Draw(self.Text)
		
		if self.victory:
			self.Text = sf.String("PARTICLES COLLECTED : " + str(sum([r.point for r in self.engine.receptors])) + " | TIME ELAPSED : " + str(int(self.timeEnd - self.timeBegin)) + " SECONDS", self.GameOver, 40)
			self.Text.SetPosition(self.window.GetWidth() / 2.0 - 200, self.window.GetHeight() / 2.0)
			self.window.Draw(self.Text)
			
		
		self.window.Display()
