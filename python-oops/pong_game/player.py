from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shape("square")
        self.shapesize(stretch_len=3)

    def move_up(self):
        if self.ycor() < 210:
            self.forward(10)

    def move_down(self):
        if self.ycor() > -210:
            self.backward(10)
