from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# update를 하지 않으면 아무것도 안 한다
screen.tracer(0)

# 뱀을 가지오 오기
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:

    # 뱀이 움직일 때마다, 몸 전체가 움직이게 된다
    screen.update()
    time.sleep(0.1)

    # 뱀 움직이기
    snake.move()


screen.exitonclick()