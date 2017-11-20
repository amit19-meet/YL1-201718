from turtle import Turtle, colormode
colormode(255)
import random
class Square (Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)
	
	def random_color(self):

		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(r,g,b)



square1 = Square(10)
square1.random_color()
