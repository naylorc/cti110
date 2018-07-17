import turtle
win = turtle.Screen()
t = turtle.Turtle()


t.pensize(2)
t.pencolor("green")
t.shape("turtle")

answer="y"

while answer=="y":
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    answer=input("Would you like to run again? Y or N ")
win.mainloop()
