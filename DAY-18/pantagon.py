import turtle
import random

# Create a Turtle object
t = turtle.Turtle()

# Set the speed of the turtle
# t.speed(1)
# no_of_times = int(input("how many pantagon do u want :\n"))
# side = 5
# angle = 360 / side
# for _ in range(no_of_times):
#     for _ in range(side):
#         t.forward(50)
#         t.right(angle)
#     side = side + 1
#     angle = 360 / side

t.speed(5)

turtle.colormode(255)


# crete a rgb tuple of color
def color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    rgb = (red, green, blue)
    return rgb


# drawing a pattern by 3 sides to 10 sides ,initially side=3
def draw_patten(side):
    # calculating an angle by dividing number of sides
    angle = 360 / side
    # creating a pattern
    for _ in range(side):
        t.forward(100)
        t.right(angle)


# calling  a function
for x in range(3, 11):
    t.color(color())
    draw_patten(x)
