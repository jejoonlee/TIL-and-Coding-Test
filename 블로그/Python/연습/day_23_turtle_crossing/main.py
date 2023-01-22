import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

avator = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(avator.move ,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.car_move()

    # 거북이가 도착 지점에 도착하면, 다시 시작 지점으로 돌아온다
    # 그리고 레벨이 올라간다
    if avator.ycor() > 280:
        car.level_up()
        avator.new_level()
        scoreboard.score_up()

    # 차에 부딛히면, 게임을 중단 시킨다
    for vehicle in car.all_cars:
        if avator.distance(vehicle) <= 20:
            game_is_on = False
            scoreboard.game_over()
            break

screen.exitonclick()