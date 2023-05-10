import random
import turtle
from turtle import Turtle, Screen

# creating object of class Turtle
q = Turtle()

# speed function
q.speed("fastest")

# This function is used to return the color mode or set it to 1.0 or 255. (r, g, b) values of color triples have to
# be in range 0 to c mode One of the values 1.0 or 255.
turtle.colormode(255)


# using colorgram class
# def color():
#     all_colors = []
#     extract_colors = colorgram.extract("image.png", 10)
#     for i in extract_colors:
#         red = i.rgb.r
#         green = i.rgb.g
#         blue = i.rgb.b
#         new_color = (red, green, blue)
#         all_colors.append(new_color)
#     return all_colors

# it used to get the rgb values
def color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    rgb = (red, green, blue)
    return rgb


# this function change the direction
def change_direction():
    q.penup()
    q.setheading(90)
    q.forward(30)
    q.setheading(180)
    q.forward(300)
    q.setheading(360)


def painting():
    for i in range(10):
        # does not shows the lines
        q.penup()
        # hide the turtle
        q.hideturtle()
        for j in range(10):
            q.begin_fill()
            q.circle(5)
            q.end_fill()
            q.penup()
            q.forward(30)
            q.pendown()
            q.color(color())
        change_direction()

painting()

# creating an object of Screen class
screen = Screen()

# exitonclick function means tap and exit
screen.exitonclick()
