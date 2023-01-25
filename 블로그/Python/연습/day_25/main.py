from turtle import Turtle, Screen
import pandas

screen = Screen()
name = Turtle()

screen.title("US States Game")
screen.bgpic("blank_states_img.gif")
screen.setup(width=725, height=491)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
count = 0
correct_states = []

while len(correct_states) < 50:
    state_name = screen.textinput(f"{count}/{len(data)} States Correct", "Type name of US state: ")
    state_name = state_name.title()

    if state_name == 'Exit':
        states_to_learn = pandas.DataFrame([state for state in states if state not in correct_states])
        states_to_learn.to_csv("states_to_learn.csv")
        break

    if state_name in states and state_name not in correct_states:
        count += 1
        correct_states.append(state_name)
        x_cord = int(data[data["state"] == state_name].x)
        y_cord = int(data[data["state"] == state_name].y)

        name.penup()
        name.hideturtle()
        name.goto(x_cord, y_cord)
        name.write(state_name, align="center")
