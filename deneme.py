


import turtle

written=0

wn=turtle.Screen()
wn.title("Button Counting")
wn.bgcolor("red")
wn.setup(width=800,height=800)

button=turtle.Turtle()
button.penup()
button.color("white")
button.shape("square")
button.shapesize(stretch_wid=5, stretch_len=5)

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 0)
pen.write(" 0 ")

def click(x,y):
    global written
    wn.update()
    written += 1
    x=0
    y=0
    pen.clear()
    pen.write(" {} ".format(written), align="center")

turtle.listen()
button.onclick(click)
turtle.mainloop()