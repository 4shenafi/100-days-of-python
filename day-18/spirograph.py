from turtle import Turtle, Screen
import random


tim = Turtle()
def random_color():
    r = random.randint(0, 1)
    g = random.randint(0, 1)
    b = random.randint(0, 1)
    return (r, g, b)

for i in range(18):
    color = random_color()
    tim.color(color)
    tim.circle(150)
    tim.right(20)

screen = Screen()
screen.exitonclick()