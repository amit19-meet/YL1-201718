import turtle
import time
import random
from ball.py import Ball
import math

turtle.tracer(delay=0)

RUNNING= True
SLEEP= 0.0077
SCREEN_WIDTH= turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT= turtle.getcanvas().winfo_height()/2

MY_BALL= Ball(x=0, y=0, dx= 3, dy= 3, r= 20, color= "purple")

NUMBER_OF_BALLS= 5
MINIMUM_BALL_RADIUS= 10
MAXIMUM_BALL_RADIUS= 100
MINIMUM_BALL_DX= -5
MAXIMUM_BALL_DX= 5
MINIMUM_BALL_DY= -5
MAXIMUM_BALL_DY= 5

for i in range(NUMBER_OF_BALLS):
    x= random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
    y= random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
    dx= random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
        while(dx==0):
            dx= random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
    dy= random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
        while(dy==0):
            dy= random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
    r= random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
    color= (random.random(), random.random(), random.random())

BALLS= []

NEW_BALL= Ball(x,y,dx,dy,r,color)
BALLS.append(NEW_BALL)

for i in BALLS:
    i.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collide(ball_a,ball_b):
    if ball_a==ball_b:
        return False
    A= math.sqrt(math.pow((ball_b.xcor()-ball_a.xcor()+ 

    



    
    






