from turtle import Turtle

# initial position of player or 0,-280
STARTING_POSITION = (0, -260)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("navy blue")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    # creating the function for a key
    def turtle_up(self):
        # new_y = self.ycor() + 20
        # self.goto(self.xcor(), new_y)
        self.forward(MOVE_DISTANCE)

    # if player crossed the 280 on yaxis then return true else false
    def reached_destination(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    # set thr turtle at the initial position(0,-280)
    def go_to_start(self):
        self.goto(STARTING_POSITION)

