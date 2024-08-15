from turtle import Turtle, Screen
import random

tim = Turtle()
tim.pensize(30)

colors = [
    (1.0, 0.0, 0.0),
    (0.0, 1.0, 0.0),
    (0.0, 0.0, 1.0),
    (1.0, 0.5, 0.0),
    (1.0, 1.0, 0.0),
    (0.5, 0.0, 0.5),
    (1.0, 0.0, 1.0),
    (0.0, 1.0, 1.0),
    (0.5, 0.5, 0.0),
    (0.5, 0.0, 0.0)
]
while True:
    degree = random.choice([0, 90, 180, 360, -90, -180])
    color = random.choice(colors)
    tim.forward(50)
    tim.color(color)
    tim.right(degree)

screen = Screen()
screen.exitonclick()
