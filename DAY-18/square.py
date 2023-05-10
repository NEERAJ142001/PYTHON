from turtle import Turtle, Screen

# creating an object of class Turtle
t = Turtle()

# speed to run
t.speed(1)

# changing the shape
t.shape("circle")

# changing the color
t.color("red")

# making a square
for _ in range(4):
    t.forward(100)
    t.right(90)

# creating an object of Screen class
screen = Screen()

# exitonclick function means tap and exit
screen.exitonclick()
