from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = -1
        self.penup()
        self.hideturtle()
        self.score_point()


    def score_point(self):
        self.score += 1
        self.clear()
        self.setposition(0, 280)
        self.write(f"Score : {self.score}", True, align="center", font=('Arial', 12, 'normal'))

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", True, align="center", font=('Arial', 24, 'normal'))