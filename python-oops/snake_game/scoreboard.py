from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 20, "normal")

HIGH_SCORE_DATA = open("data.txt")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highScore = int(file.read())
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

    def update_high_score(self):
        with open("data.txt") as file:
            self.highScore = int(file.read())

    def reset_score(self):
        if self.score > self.highScore:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.update_high_score()
        self.score = 0
        self.print_score()

    # def game_over(self):
    #     self.home()
    #     self.write("Game Over", align=ALIGN, font=FONT)
