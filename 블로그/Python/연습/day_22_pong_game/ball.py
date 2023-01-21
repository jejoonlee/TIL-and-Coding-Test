from turtle import Turtle

MOVE_DISTANCE = 20

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    # x 좌표같은 경우 계속 한 쪽으로 움직인다
    # 하지만 위 아래 벽에 부딛힐 경우, 위로 가던 공은 아래로 향해야 하고
    # 아래고 가던 공은 위로 향해야 해서 -1을 곱해준다
    def bounce(self):
        self.y_move *= -1
        self.ball_speed *= 0.9

    def paddle_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.x_move *= -1
        self.ball_speed = 0.1