# import colorgram

# colors = colorgram.extract('SpotPainting04.jpg', 30)

# color_rgb = []

# for color in colors:
#     color_rgb.append((color.rgb.r, color.rgb.g, color.rgb.b))


rgb_color = [(230, 215, 101), (234, 246, 242), (154, 80, 38), (244, 231, 236), (207, 159, 105), (181, 175, 18), (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105), (13, 37, 97), (72, 43, 23), (50, 121, 23), (187, 133, 150), (94, 192, 47), (106, 32, 54), (195, 94, 75), (25, 97, 25), (100, 120, 169), (180, 206, 170), (250, 169, 173), (24, 53, 110), (251, 171, 163), (149, 191, 244), (104, 60, 18), (81, 30, 46), (132, 79, 90), (18, 75, 105)]

# 한 줄에 10개의 점들 / 10 줄 총 100개의 점들
# 점들의 간격은 50 / 점 사이즈는 20

import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.shape("turtle")
tim.pensize(1)
tim.speed("fastest")

t.colormode(255)

tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim_xcor = tim.xcor()

for _ in range(10):

    for _ in range(10):
        tim.dot(20, random.choice(rgb_color))
        tim.penup()
        tim.forward(50)

    back_to_start = (tim_xcor, tim.ycor() + 50)

    tim.goto(back_to_start)

screen = Screen()
screen.exitonclick()