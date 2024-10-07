import turtle
import pandas as pd

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name? (Type 'exit' to finish)").title()

    if answer_state == "Exit":
        break

    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        state = data[data.state == answer_state]

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        t.goto(int(state.x), int(state.y))
        t.write(answer_state)

for state in states:
    if state not in guessed_states:
        state_data = data[data.state == state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state)

screen.exitonclick()
