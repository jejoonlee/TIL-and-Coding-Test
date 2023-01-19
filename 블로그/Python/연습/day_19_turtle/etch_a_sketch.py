# W = Forward
# S = Backwards
# A = Counter-Clockwise
# D = Clockwise
# C = Clear drawing

import turtle as t
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def clockwise():
    tim.right(10)

def counter_clockwise():
    tim.left(10)

def clear():
    tim.reset()

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear)



screen.exitonclick()