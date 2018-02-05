import turtle
import time
import random
from ball import Ball
import math

turtle.tracer(0)

RUNNING= True
SLEEP= 0.0099
SCREEN_WIDTH= round(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT= round(turtle.getcanvas().winfo_height()/2)

MY_BALL= Ball(0, 0, 3, 3, 55,"red")

NUMBER_OF_BALLS= 5
MINIMUM_BALL_RADIUS= 5
MAXIMUM_BALL_RADIUS= 70
MINIMUM_BALL_DX= -1
MAXIMUM_BALL_DX= 1
MINIMUM_BALL_DY= -1
MAXIMUM_BALL_DY= 1

BALLS= []


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
    NEW_BALL= Ball(x,y,dx,dy,r,color)
    BALLS.append(NEW_BALL)

def move_all_balls():
    for i in BALLS:
        i.move(SCREEN_WIDTH, SCREEN_HEIGHT)


def collide(ball_a,ball_b):
    if ball_a.r==ball_b.r and ball_a.pos() == ball_b.pos():
        return False
    A= math.sqrt(math.pow((ball_b.xcor()-ball_a.xcor()),2)+ math.pow((ball_a.ycor()-ball_b.ycor()),2))
    if A+10<=ball_a.r+ball_b.r:
        return True
    else:
        return False

def check_all_balls_collision():
    for ball_a in BALLS:
        for ball_b in BALLS:
            if collide(ball_a,ball_b):
                x= random.randint(int(-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS, int(SCREEN_WIDTH) - MAXIMUM_BALL_RADIUS)
                y= random.randint(int(-SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS, int(SCREEN_HEIGHT) - MAXIMUM_BALL_RADIUS)
                dx= random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                while(dx==0):
                    dx= random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                dy= random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
                while(dy==0):
                    dy= random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
                r= random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
                color = (random.random(), random.random(), random.random())
                print(r)
                if ball_a.r>ball_b.r:
                    ball_b.goto(x,y)
                    ball_b.dx = dx
                    ball_b.dy = dy
                    ball_b.color(color)
                    ball_b.r = r
                    ball_b.shapesize(r/10)
                    
                    ball_a.r = ball_a.r+1
                    ball_a.shapesize(ball_a.r/10)
                else:
                    ball_a.goto(x,y)
                    ball_a.dx = dx
                    ball_a.dy = dy
                    ball_a.color(color)
                    ball_a.r = r
                    ball_a.shapesize(r/10)
                    
                    ball_b.r = ball_a.r+1
                    ball_b.shapesize(ball_a.r/10)


def check_myball_collision():
    for ball in BALLS:
        if(collide(MY_BALL, ball)):
            my_radius = MY_BALL.r
            ball_radius = ball.r
            if(my_radius<ball_radius):
                return False
            else:
                x= random.randint(int(-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS, int(SCREEN_WIDTH) - MAXIMUM_BALL_RADIUS)
                y= random.randint(int(-SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS, int(SCREEN_HEIGHT) - MAXIMUM_BALL_RADIUS)
                dx= random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                while(dx==0):
                    dx= random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
                dy= random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
                while(dy==0):
                    dy= random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
                r= random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
                color = (random.random(), random.random(), random.random())

                ball.ht()
                ball.goto(x, y)
                ball.color(color)
                ball.r=r
                ball.shapesize(r/10)
                ball.dx=dx
                ball.dy=dy
                ball.st()

                MY_BALL.r+=1
                MY_BALL.shapesize(MY_BALL.r/10)
    return True

def move_around(event):
    MY_BALL.goto(event.x-SCREEN_WIDTH,SCREEN_HEIGHT-event.y)

turtle.getcanvas().bind("<Motion>", move_around)
turtle.listen()

while RUNNING is True:
    if SCREEN_WIDTH!= turtle.getcanvas().winfo_width()/2:
        SCREEN_WIDTH= turtle.getcanvas().winfo_width()/2
    if SCREEN_HEIGHT!= turtle.getcanvas().winfo_height()/2:
        SCREEN_HEIGHT= turtle.getcanvas().winfo_height()/2
    move_all_balls()
    check_all_balls_collision()
    RUNNING = check_myball_collision()
    time.sleep(SLEEP)
    turtle.update()
    
    
                                                            
        
    
    

    
            
            
            
        

            
        
    
        
        

                    



                    

                

            

                


                
            
        

    
