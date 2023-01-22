from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(-290, 260)
        self.level = 1
        self.write(f"Level : {self.level}", False, font = FONT)

    def score_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level : {self.level}", False, font = FONT)
    
    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", False, align="center",font = FONT)
