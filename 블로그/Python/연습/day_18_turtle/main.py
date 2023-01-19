import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
tim.pensize(1)
tim.speed("fastest")

t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(10)

screen = Screen()
screen.exitonclick()