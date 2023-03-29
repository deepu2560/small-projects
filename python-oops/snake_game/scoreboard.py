from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highScore = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.print_score()

    def count_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}  |  High score: {self.highScore}", align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.highScore:
            self.highScore = self.score
        self.score = 0
        self.print_score()

    # def game_over(self):
    #     self.home()
    #     self.write("Game Over", align=ALIGN, font=FONT)
