import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

# creating square
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

#creating dashed line
# for i in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()

#drawing dfferent shapes in one
colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan"]
c = 0
timmy.pensize(20)
for shape in [4, 5, 6, 7, 8, 9, 10]:
    degree = 360 / shape
    timmy.color(colors[c])
    c += 1
    for i in range(shape):
        timmy.forward(100)
        timmy.right(degree)

screen = Screen()
screen.exitonclick()
