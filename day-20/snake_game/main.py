import turtle
from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

# Set up the game objects
snake = Snake()
food = Food()
screen = Screen()
score = ScoreBoard()

# Configure the screen
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

# Set up the key listeners for snake movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
