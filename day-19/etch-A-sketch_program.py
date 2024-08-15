from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward(): 
    tim.backward(10)


def move_clockwise():
    tim.right(5)


def move_counter_clockwise():
    tim.left(5)


def clear_screen():
    screen.reset()


screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(move_clockwise, "Right")
screen.onkey(move_counter_clockwise, "Left")
screen.onkey(clear_screen, "c")
screen.listen()
screen.exitonclick()
