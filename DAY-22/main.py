from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# making a screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# creating an object for left and right paddle
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# object of ball class
ball = Ball()
# object of scoreboard class
scoreboard = Scoreboard()

# making an onkey listener
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    # turing on animations
    screen.update()
    # ball.move setting the ball at random positions
    ball.move()

    # Detect collision with wall means on y-axis if ball reached greater than 280 or lesser than -280
    # than it has to bounce back again
    if ball.ycor() > 280 or ball.ycor() < -280:

        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or\
            ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect Right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect Left paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
