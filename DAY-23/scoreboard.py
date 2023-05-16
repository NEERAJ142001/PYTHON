# it finds out the score
# displaying the score
# end the game if turtle crashes with car


from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.display_scoreboard()

    # display score_board
    def display_scoreboard(self):
        self.clear()
        self.write(f"Level :{self.score}", align="left", font=FONT)

    # increasing the level
    def scoreboard_increased(self):
        self.score += 1
        self.display_scoreboard()

    # if turtle crashes with a car then call game over function
    def game_end(self):
        self.goto(-280, 0)
        self.write(f"GAME-OVER,you crossed {self.score - 1} Level ", align="left", font=FONT)
