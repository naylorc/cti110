import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

t.pensize(4)
t.pencolor("red")
t.shape("arrow")

t.circle(100,-180)
t.penup()
t.setposition(0,0)
t.right(180)
t.forward(100)
t.left(90)
t.pendown()
t.forward(200)
t.right(152)
t.forward(220)
t.left(152)
t.forward(200)

