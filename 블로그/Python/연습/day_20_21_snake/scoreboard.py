from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")

        file = open("score.txt")
        last_high_score = file.read()

        self.high_score = int(last_high_score)
        self.score = -1
        self.penup()
        self.setposition(0, 280)
        self.hideturtle()
        self.update_scoreboard()
        self.score_point()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", False, align="center", font=('Arial', 12, 'normal'))

    def score_point(self):
        self.score += 1
        self.update_scoreboard()

    # 최고 점수 추가하기
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            
            with open("score.txt", mode="w") as file:
                file.write(str(self.high_score))
        
        self.score = 0
        self.update_scoreboard()





    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write("GAME OVER", True, align="center", font=('Arial', 24, 'normal'))