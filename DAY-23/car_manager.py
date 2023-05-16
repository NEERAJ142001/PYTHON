# it creates the car
# move the car with a specific speed
# increased by level 1 everytime if it reaches destination
import random
from turtle import Turtle

# color of obstacle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:

    def __init__(self):
        self.car_list = []
        self.create_car()
        self.speed = STARTING_MOVE_DISTANCE

    # creating a car
    def create_car(self):
        random_chance = random.randint(1, 10)
        if random_chance == 1 or random_chance == 5:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choices(COLORS))
            y_position = random.randint(-250, 250)
            new_car.goto(280, y_position)
            self.car_list.append(new_car)

    # move the car from right side to left
    def move_car(self):
        for move in self.car_list:
            move.setheading(180)

            move.forward(self.speed)

    # after reaching  the destination then level up
    def level_up(self):
        self.speed = self.speed + MOVE_INCREMENT
