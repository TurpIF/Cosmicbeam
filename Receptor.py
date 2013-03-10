class Receptor:
	def __init__(self, sprReceptor, minimum):
		self.width, self.height = sprReceptor.GetSize()
		self.x, self.y = sprReceptor.GetPosition()
		self.point = 0
		self.minimum = minimum

