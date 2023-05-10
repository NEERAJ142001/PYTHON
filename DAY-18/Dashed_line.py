from turtle import Turtle, Screen

# creating an object of class Turtle
t = Turtle()

# speed to run
t.speed(1)

# changing the shape
t.shape("circle")

# changing the color
t.color("red")

# making a dotted square
for _ in range(4):
    for _ in range(10):
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
    t.right(90)


# creating an object of Screen class
screen = Screen()

# exitonclick function means tap and exit
screen.exitonclick()