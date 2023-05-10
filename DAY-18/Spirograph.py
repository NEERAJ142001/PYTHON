import random
import turtle
from turtle import Turtle, Screen

# create an object of class Turtle
q = Turtle()
# setting speed
q.speed(30)
# set the color shade to 255
turtle.colormode(255)
# # width of circle
# q.pensize(2)


# create a rgb value and store in tuple
def color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    rgb = (red, green, blue)
    return rgb


def draw_a_circle():
    # 38 circle
    for _ in range(72):
        # rotate 360 times with a radius of 100 and full circle=360
        q.circle(90, 360)

        # # move towards right
        # q.right(10)

        # calculating the angle and store in heading
        heading = q.heading()
        # add subtract,add,multiply,divide th change the angle
        q.setheading(heading - 5)
        q.color(color())


draw_a_circle()

# creating an object of Screen class
screen = Screen()

# exitonclick function means tap and exit
screen.exitonclick()
