from PySFML import sf
import sys
from Menu import Menu

m = Menu(sf.RenderWindow(sf.VideoMode(1280, 720), "CosmicBeam"))
#m = Menu(sf.RenderWindow(sf.VideoMode(800, 600), "PySFML test"))
m.run()
sys.exit()
