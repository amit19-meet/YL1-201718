#turtle.register_shape("shape_name", ((50,0), (50,50), (0,50), (0,0)))
import turtle
turtle.addshape("heart.gif")
turtle.shape("heart.gif")
turtle.getshapes()
turtle.home()
#turtle.forward(100)
#turtle.right(30)
#turtle.forward(70)
#turtle.right(110)
#turtle.forward(40)

for i in range(360):
	turtle.color("Red")
	turtle.forward(100)
	turtle.left(144)
	turtle.color("Green")
	turtle.forward(100)
	turtle.left(144)
	turtle.color("Purple")
	turtle.forward(100)
	turtle.left(144)
	turtle.color("Yellow")
	turtle.forward(100)
	turtle.left(144)
	turtle.color("Blue")
	turtle.forward(100)
	turtle.right(1)



turtle.mainloop()