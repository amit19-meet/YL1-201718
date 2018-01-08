import turtle

# using this class i will create the different circles for the game.
class Circle(Turtle):
	def __init__(self, size, color):
		Turtle.__init__(self)
		self.color=color
		self.size=size

player= Circle(30, "red")
