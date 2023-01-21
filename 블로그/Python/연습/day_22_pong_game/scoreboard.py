from turtle import Turtle

EACH_SCORE = [(250, 200), (-250, 200)]

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.setposition(250, 200)
        self.write(self.r_score, font=('Arial', 48, 'normal'))
        self.setposition(-250, 200)
        self.write(self.l_score, font=('Arial', 48, 'normal'))
    

    def r_score_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def l_score_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()
