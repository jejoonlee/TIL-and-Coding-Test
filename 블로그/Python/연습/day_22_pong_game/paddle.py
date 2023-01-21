from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, s_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.starting_position(s_position)

    def starting_position(self, s_position):
        self.penup()
        self.setposition(s_position)

    def up(self):
        new_ycor = self.ycor() + MOVE_DISTANCE
        
        if new_ycor <= 255:
            self.goto(self.xcor(), new_ycor)


    def down(self):
        new_ycor = self.ycor() - MOVE_DISTANCE

        if new_ycor >= -250:
            self.goto(self.xcor(), new_ycor)