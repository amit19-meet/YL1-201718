from turtle import *
import random
import math

class Ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)

ball1= Ball(25,"pink",3)
ball2= Ball(36, "blue",3)



def check_collisions(ball1,ball2):
	a= math.sqrt(math.pow((ball1.xcor()-ball2.xcor(),2)+math.pow(ball1.ycor()-ball2.ycor(),2)))

	if a<=ball1.shapesize()[0]+ball2.shapesize()[0]:
		ball1.color("red")
		ball2.color("green")

check_collisions(ball1,ball2)

	


mainloop()






