from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.fillcolor("black")
        self.print_score()

    def count_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", move=True, align="center", font=("Arial", 20, "normal"))
