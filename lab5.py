from turtle import Turtle #colormode
import turtle
#colormode(255)
#import random
#class Square (Turtle):
	#def __init__(self,size):
		#Turtle.__init__(self)
		#self.shape("square")
		#self.shapesize(size)
	
	#def random_color(self):

		#r = random.randint(0,255)
		#g = random.randint(0,255)
		#b = random.randint(0,255)
		#self.color(r,g,b)



#square1 = Square(10)
#square1.random_color()

class Hexagon (Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.home()
		self.begin_poly()
		self.forward(100)
		self.right(45)
		self.forward(100)
		self.right(45)
		self.forward(100)
		self.right(45)
		self.forward(100)
		self.right(45)
		self.forward(100)
		self.right(45)
		self.forward(100)
		self.end_poly()
		h= self.get_poly()
		register_shape("Hexagon",h)
		self.shape("Hexagon")
		self.shapesize(size)


hexagon= Hexagon(h, 30)

turtle.mainloop()