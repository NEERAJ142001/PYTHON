import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# making a screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Making of objects of classes
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

# Making a key to goes upward direction
screen.listen()
screen.onkey(player.turtle_up, "Up")

game_is_on = True
# loop to start thr game
while game_is_on:
    # delay of 0.1 sec
    time.sleep(0.1)
    screen.update()

    # creating a car
    car_manager.create_car()

    # start moving the car
    car_manager.move_car()

    # checking that turtle is hitting the car
    for cars in car_manager.car_list:
        # if turtle hit any of the car then we have to stop the game and display the result
        if cars.distance(player) < 25:
            game_is_on = False
            scoreboard.game_end()

    # if player reached the end then
    # start the game again
    # increased the level
    # update the scoreboard
    if player.reached_destination():
        
        car_manager.level_up()
        player.go_to_start()
        scoreboard.scoreboard_increased()

screen.exitonclick()
