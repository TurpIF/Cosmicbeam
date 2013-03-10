import Game
from PySFML import sf
from Engine import *
import Geometry

from Receptor import Receptor
from Emitter import Emitter
from Particle import Particle
from Mirror import Mirror
from Circle import Circle
from Field import *
from Medium import Medium

class Level5(Game.Game):
	def construct(self):
		self.max_width = 1600
		self.max_height = 900
		
		#LOADING BACKGROUND
		img = sf.Image()
		img.LoadFromFile("./img/background_repeated.png")
		self.sprBackgroundTile = sf.Sprite(img)
		
		#LOADING AND PLACING EMITTER
		img = sf.Image()
		img.LoadFromFile("./img/emitter.png")
		self.sprEmitters += [sf.Sprite(img)]
		self.sprEmitters[-1].SetPosition(0, 400)
		
		self.emitters = []
		self.emitters += [Emitter(self.sprEmitters[0].GetPosition()[0] + self.sprEmitters[0].GetSize()[0] - 5, self.sprEmitters[0].GetPosition()[1] + self.sprEmitters[0].GetSize()[1] / 2.0, 100, 10, sf.Color(0, 0, 300), 30)]
		
		#LOADING AND PLACING RECEPTOR
		img = sf.Image()
		img.LoadFromFile("./img/receptor.png")
		self.sprReceptors += [sf.Sprite(img)]
		self.sprReceptors[-1].SetPosition(self.max_width - self.sprEmitters[0].GetSize()[0], 250)
		
		self.receptors = []
		self.receptors += [Receptor(self.sprReceptors[0], 10)]
		
		#ON
		self.posMouse = None
		self.engine = Engine(self.max_width, self.max_height, self.receptors, self.emitters)
		
		#NIVEAU:
		self.engine.fields += [AntiBlackHoleField(1500, 100, 400000)]
		self.engine.fields += [AntiBlackHoleField(1100, 320, 400000)]
		self.engine.fields += [AntiBlackHoleField(900, 600, 400000)]
		self.engine.fields += [BlackHoleField(500, 50, 400000)]

		# self.engine.medium += [Medium([(200, 200), (500, 200), (500, 600), (200, 600)], 10.7337)]
		
		#self.engine.obstacles += [Circle(900, 300, 2)]
		#self.engine.obstacles += [Circle(400, 500, 1)]
		#self.engine.obstacles += [Circle(600, 50, 4)]
		#self.engine.obstacles += [Circle(800, 600, 3)]
		
		self.engine.obstacles += [Mirror(50, 375, 600, 375)]
		self.engine.obstacles += [Mirror(50, 475, 650, 475)]
		self.engine.obstacles += [Mirror(600, 375, 600, 75)]
		self.engine.obstacles += [Mirror(650, 475, 650, 125, True)]
		
