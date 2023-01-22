from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        y_cor = self.ycor() + MOVE_DISTANCE 
        self.goto(0, y_cor)

    def new_level(self):
        self.goto(STARTING_POSITION)