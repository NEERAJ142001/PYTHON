from turtle import Turtle, Screen

q = Turtle()


def move_forwards():
    q.forward(100)


def move_left():
    q.left(90)
    q.forward(100)


def move_right():
    q.right(90)
    q.forward(100)


# creating an object of Screen class
screen = Screen()
# Set focus on TurtleScreen (in order to collect key-events). Dummy arguments are provided in order to be able to
# pass listen() to the onclick method

screen.listen()

# on key function it works when we click the key
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="l", fun=move_left)
screen.onkey(key="r", fun=move_right)

# exitonclick function means tap and exit
screen.exitonclick()
