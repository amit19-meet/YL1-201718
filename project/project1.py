import turtle

# using this class i will create the different circles for the game.
class Ball(turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)
		self.penup()
		self.setpos(x,y)
		self.dx(dx)
		self.dy(dy)
		self.r(r)
		self.shape("circle")
		self.shapesize(r/10)
		self.color(color)

	def move(self,screen_width, screen_height):
                current_x= self.xcor()
                new_x= current_x + self.dx
                current_y= self.ycor()
                new_y= current_y + self.dy
                right_side_ball= new_x + self.r
                left_side_ball= new_x - self.r
                up_side_ball = new_y + self.r
                down_side_ball = new_y - self.r
                self.goto(new_x, new_y)
                if right_side_ball>screen_width/2:
                        self.dx= self.dx*(-1)
                if left_side_ball<screen_width/(-2):
                        self.dx= self.dx*(-1)
                if up_side_ball>screen_height/2:
                        self.dy= self.dy*(-1)
                if down_side_ball<screen_height/(-2):
                        self.dy= self.dy*(-1)

                        
                        
                
                

