import turtle
import random
import time
screen = turtle.Screen()
Lturtle = turtle.Turtle()
Lturtle.shape("turtle")
Lturtle.shapesize(2)
Lturtle.color("green")
Lturtle.left(90)


Lturtle.write("Merhaba Dünya!")



screen.bgcolor("light blue")
screen.title("Catch Turtle Game")


Lturtle.speed(3)

screen.screensize(350,350)

while True:
    Lturtle.penup()
    Lturtle.goto(random.randint(-320,320),random.randint(-300,300))
    Lturtle.hideturtle()
    Lturtle.showturtle()


screen.listen()





screen.mainloop()