from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.angle = self.heading()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def move(self):
        self.setheading(self.angle)
        self.forward(10)

    def bounce(self, angle):
        self.angle += angle
