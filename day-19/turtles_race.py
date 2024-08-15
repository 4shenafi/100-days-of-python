from turtle import Turtle, Screen
import random


is_race_on = False
colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "black"]
racers = []
screen = Screen()
screen.setup(width=500, height=500)
usr_choice = screen.textinput("Turtles Race Game", "Which color of turtle will win o you think?")
y_position = [-140, -100, -60, -20, 20, 60, 100, 140]
all_players = []
for i in range(len(colors)):
    player = Turtle(shape="turtle")
    player.color(colors[i])
    player.penup()
    player.goto(x=-230, y=y_position[i])
    all_players.append(player)

if usr_choice:
    is_race_on = True

while is_race_on:
    for player in all_players:
        if player.xcor() > 230:
            is_race_on =False
            wining_player = player.pencolor()
            if wining_player == usr_choice:
                print("You Won!")
            else:
                print(f'You Lose! Winner is {wining_player}')
        rand_dist = random.randint(0, 10)
        player.forward(rand_dist)

screen.exitonclick()
