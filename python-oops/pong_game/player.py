from turtle import Turtle


class Player(Turtle):
    def __init__(self, position, clr):
        super().__init__()
        self.penup()
        self.color(clr)
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)

    def move_up(self):
        if self.ycor() < 270:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -270:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
