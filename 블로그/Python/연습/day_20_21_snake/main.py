from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# update를 하지 않으면 아무것도 안 한다
screen.tracer(0)

# 뱀을 가지오 오기
snake = Snake()
food = Food()
scoreboard = ScoreBoard()


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

    if snake.head.distance(food) < 10:
        scoreboard.score_point()
        food.refresh()
        snake.extend()

    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        scoreboard.reset()
        snake.reset()

    for body in snake.body[1:]:
        if snake.head.position() == body.position():
            scoreboard.reset()
            snake.reset()

screen.exitonclick()