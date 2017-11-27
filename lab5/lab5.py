from turtle import *
colormode(255)
import random
#exercise_1:
#class Square (Turtle):
#	def __init__(self,size):
#		Turtle.__init__(self)
#		self.shape("square")
#		self.shapesize(size)
	
#	def random_color(self):

#		r = random.randint(0,255)
#		g = random.randint(0,255)
#		b = random.randint(0,255)
#		self.color(r,g,b)



#square1 = Square(3)
#square1.random_color()

#exercise_2:
class Hexagon (Turtle):
	def __init__(self,size,color):
		Turtle.__init__(self)
		self.home()
		self.begin_poly()
		self.forward(100)
		self.right(60)
		self.forward(100)
		self.right(60)
		self.forward(100)
		self.right(60)
		self.forward(100)
		self.right(60)
		self.forward(100)
		self.right(60)
		self.forward(100)
		self.end_poly()
		h= self.get_poly()
		self.color(color)
		self.shapesize(size)
		register_shape("Hexagon",h)
		self.shape("circle")
		self.clear()

		
	
		

	
		


hexagon= Hexagon(40, "purple")
mainloop()