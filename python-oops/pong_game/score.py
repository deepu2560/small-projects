from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=0, y=250)
        self.write(f"{self.score_left}   |   {self.score_right}", align="center", font=("arial", 30, "normal"))

    def left_scored(self):
        self.score_left += 1
        self.update_score()

    def right_scored(self):
        self.score_right += 1
        self.update_score()

    def who_won(self, player):
        self.goto(0, 0)
        self.write(f"{player} Won the match", align="center", font=("arial", 30, "normal"))
