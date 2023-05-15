from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = .5
        self.y_move = .5
        self.move_speed = 0.1

    # moving ball at random position
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # The bounce_y method is used to reverse the direction of the ball
    # when it hits a vertical boundary.
    # It does this by multiplying the current y_move by -1.
    def bounce_y(self):
        self.y_move = self.y_move * -1

    # The bounce_x method is used to reverse the direction of the ball when it hits a horizontal boundary.
    # It does this by multiplying the current x_move by -1 and reducing the move_speed property by 10%.
    def bounce_x(self):
        self.x_move = self.x_move * -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
