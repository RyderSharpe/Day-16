# https://docs.python.org/3/library/turtle.html

# Attributes: have things -> is_holding_plate = true
# Methods: things can do -> def take_order(table, order):

# Class: The waiter
# Object: waiters names
# object = class() -> car = CarBlueprint()

# import turtle
# timmy = turtle.Turtle()
# *or can write as shown below
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)

# methods
timmy.shape("turtle")
timmy.color("cyan", "magenta")
timmy.forward(100)
# object.attribute -> car.speed
my_screen = Screen()
print(my_screen.canvheight)
# object.method -> car.stop()
my_screen.exitonclick()
