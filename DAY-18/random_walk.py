import turtle
from turtle import Turtle, Screen
import random

# creating an object of Turtle class
q = Turtle()

# set the colormode to 255
turtle.colormode(255)


# making a list of colors by color function
def color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    rgb = (red, green, blue)
    return rgb


# making a list of directions
directions = [0, 90, 180, 270]

# setting a speed
q.speed(30)

# increase the width size
q.pensize(13)

# loop upto 200
for i in range(200):
    # forward by 40
    q.forward(40)
    # changing the direction of turtle
    q.setheading(random.choice(directions))
    # changing the color everytime
    q.color(color())

# creating an object of Screen class
screen = Screen()

# exitonclick function means tap and exit
screen.exitonclick()
