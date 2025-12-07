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

"""
import time
import sys
from plyer import notifi
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f"{mins:02d}:{secs:02d}"

        sys.stdout.write("\r" + timer + "   ")
        sys.stdout.flush()

        time.sleep(1)
        t -= 1

    print("\nZamanlayıcı sona erdi")

    notification.notify(
        title="Time manager",
        message="TİME İS OUT !!!",
        timeout=1
    )
t = int(input("zamanı giriniz: "))
countdown(t)2
"""