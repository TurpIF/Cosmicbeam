from PySFML import sf

from LevelSelect import LevelSelect
from Level1 import Level1
from Level2 import Level2
from Level3 import Level3
from Level4 import Level4
from Level5 import Level5

class Menu:
	def __init__(self, window):
		self.window = window
		self.running = False
		self.cursor = 0
		self.sprCursor = []
		
		self.levels = [Level1, Level2, Level3, Level4, Level5]
		
		img = sf.Image()
		img.LoadFromFile("img/background.png")
		self.sprBackground = sf.Sprite(img)
		
		x = -(self.window.GetWidth() - self.sprBackground.GetSize()[0]) / 2.0
		y = 0
		self.sprBackground.SetCenter(x, y)
		
		img = sf.Image()
		img.LoadFromFile("./img/logo.png")
		self.sprLogo = sf.Sprite(img)
		x = -(self.window.GetWidth() - self.sprLogo.GetSize()[0]) / 2.0
		y = -30
		self.sprLogo.SetCenter(x, y)
		
		img1, img2 = sf.Image(), sf.Image()
		img1.LoadFromFile("./img/new_game.png")
		img2.LoadFromFile("./img/new_game_on.png")
		self.sprCursor += [(sf.Sprite(img1), sf.Sprite(img2))]
				
		x = -(self.window.GetWidth() - self.sprCursor[-1][0].GetSize()[0]) / 2.0
		self.sprCursor[-1][0].SetCenter(x, 0)
		self.sprCursor[-1][0].SetY(250)
		self.sprCursor[-1][1].SetCenter(x, -250)
		
		img1, img2 = sf.Image(), sf.Image()
		img1.LoadFromFile("./img/selection_niveau.png")
		img2.LoadFromFile("./img/selection_niveau_on.png")
		self.sprCursor += [(sf.Sprite(img1), sf.Sprite(img2))]
		
		x = -(self.window.GetWidth() - self.sprCursor[-1][0].GetSize()[0]) / 2.0
		self.sprCursor[-1][0].SetCenter(x, 0)
		self.sprCursor[-1][0].SetY(self.sprCursor[-2][0].GetPosition()[1] + self.sprCursor[-2][0].GetSubRect().Bottom + 30)
		self.sprCursor[-1][1].SetCenter(x, -self.sprCursor[-1][0].GetPosition()[1])
		
		self.music = sf.Music()
		self.music.OpenFromFile("./music.ogg")
		self.music.Play()
	
	def run(self):
		self.running = True
		while self.running:
			self.event()
			self.draw()
	
	def event(self):
		event = sf.Event()
		while self.window.GetEvent(event):
			if event.Type == sf.Event.Closed:
				self.running = False
			
			if event.Type == sf.Event.KeyPressed:
				if event.Key.Code == sf.Key.Up:		self.goUp()
				if event.Key.Code == sf.Key.Down:	self.goDown()
				if event.Key.Code == sf.Key.Return:	self.goIn()
	
	def draw(self):
		self.window.Clear()
		self.window.Draw(self.sprBackground)
		self.window.Draw(self.sprLogo)
		
		for i, p in enumerate(self.sprCursor):
			self.window.Draw(p[0])
			if i == self.cursor:
				self.window.Draw(p[1])
		
		self.window.Display()
	
	def goUp(self):
		self.cursor -= 1
		if self.cursor < 0:
			self.cursor = len(self.sprCursor) - 1
	
	def goDown(self):
		self.cursor += 1
		if self.cursor >= len(self.sprCursor):
			self.cursor = 0
	
	def goIn(self):
		if self.cursor == 0:
			for l in self.levels:
				g = l(self.window)
				g.run()
		
		if self.cursor == 1:
			l = LevelSelect(self.window)
			l.run()

