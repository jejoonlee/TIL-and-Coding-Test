import turtle as t
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color from rainbow colors: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
turtle_line = -170

for i in range(len(colors)):
    temp_turtle = Turtle(shape="turtle")
    temp_turtle.color(colors[i])

    turtle_line += 50

    temp_turtle.penup()
    temp_turtle.goto(-220, turtle_line)

    turtles.append(temp_turtle)

print(turtles)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle_race in turtles:
        move_forward = random.randint(0, 10)
        turtle_race.forward(move_forward)

        if turtle_race.xcor() > 230:
            winner = turtle_race.color()
            is_race_on = False
            break

if winner == user_bet:
    print(f"You've won! The {winner} turtle is the winner!")
else:
    print(f"You've lost! The {winner} turtle is the winner!")

screen.exitonclick()