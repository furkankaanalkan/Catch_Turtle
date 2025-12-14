import turtle
import random
import time


screen = turtle.Screen()
myturtle = turtle.Turtle()
myturtle.shape("turtle")
myturtle.shapesize(4)
myturtle.color("green")
myturtle.left(90)

screen.bgcolor("light blue")
screen.title("Catch Turtle Game")
screen.screensize(400,400)

myturtle.speed(3)

written = 0



pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 320)
pen.write(" Score: 0 ", align="center", font=("Arial", 24, "normal"))

def click(x,y):
    global written
    screen.update()
    written += 1
    x=0
    y=0
    pen.clear()
    pen.write(" Score :{} ".format(written),align="center")
myturtle.onclick(click)
turtle.listen()

while True:
    myturtle.penup()
    myturtle.hideturtle()
    myturtle.teleport(random.randint(-320,320),random.randint(-300,300))
    myturtle.showturtle()
    screen.delay(400)

timing(8)
