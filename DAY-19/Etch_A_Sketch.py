from turtle import Turtle, Screen

q = Turtle()


# go forward by 100
def forward():
    q.forward(100)


# go backward by 100
def backward():
    q.backward(100)


# changes an angle by 100 degree
def left():
    heading = q.heading() + 100
    q.setheading(heading)


# change turtle angle by 100 degree by right side
def right():
    q.right(100)


# reset the turtle
def clear():
    q.clear()
    q.penup()
    q.home()
    q.pendown()
    # q.reset()


screen = Screen()
screen.listen()
# button listener
screen.onkey(key="f", fun=forward)
screen.onkey(key="b", fun=backward)
screen.onkey(key="l", fun=left)
screen.onkey(key="r", fun=right)
screen.onkey(key="q", fun=clear)

screen.exitonclick()
