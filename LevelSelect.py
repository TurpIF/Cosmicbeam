from PySFML import sf
import sys

import Level1
import Level2
import Level3
import Level4
import Level5

class LevelSelect:
	def __init__(self, window):
		self.window = window
		self.running = False
		
		img = sf.Image()
		img.LoadFromFile("./img/background.png")
		self.sprBackground = sf.Sprite(img)
		self.sprBackground.SetCenter(-(self.window.GetWidth() - self.sprBackground.GetSize()[0]) / 2.0, 0)
		
		self.cursor = 0
		self.levels = [Level1.Level1, Level2.Level2, Level3.Level3, Level4.Level4, Level5.Level5]
		
		#INITIALIZING THE TEXT'S FONT
		self.GameOver = sf.Font()
		self.GameOver.LoadFromFile("./fonts/game_over.ttf")
		
		#INITIALIZING THE TEXT
		self.Text = sf.String()
	
	def run(self):
		self.running = True
		while self.running:
			self.event()
			self.draw()
	
	def event(self):
		event = sf.Event()
		while self.window.GetEvent(event):
			if event.Type == sf.Event.Closed:
				sys.exit
			
			if event.Type == sf.Event.KeyPressed:
				if event.Key.Code == sf.Key.Up:		self.goUp()
				if event.Key.Code == sf.Key.Down:	self.goDown()
				if event.Key.Code == sf.Key.Return:	self.goIn()
				if event.Key.Code == sf.Key.Escape:	self.running = False
	
	def draw(self):
		self.window.Clear()
		self.window.Draw(self.sprBackground)
		
		for i in xrange(len(self.levels)):
			self.Text = sf.String("Level " + str(i + 1) + "", self.GameOver, 80)
			self.Text.SetPosition(250, 200 + 70 * i)
			if self.cursor == i:
				self.Text.SetColor(sf.Color(231, 58, 134))
			self.window.Draw(self.Text)
		
		self.window.Display()
	
	def goUp(self):
		self.cursor -= 1
		if self.cursor < 0:
			self.cursor = len(self.levels) - 1
	
	def goDown(self):
		self.cursor += 1
		if self.cursor >= len(self.levels):
			self.cursor = 0
	
	def goIn(self):
		for n in xrange(self.cursor, len(self.levels)):
			g = self.levels[n](self.window)
			g.run()

