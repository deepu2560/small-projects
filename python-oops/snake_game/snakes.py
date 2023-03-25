from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.snake_head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(position)
            self.snakes.append(tim)

    def move(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            x_cord = self.snakes[snake_num - 1].xcor()
            y_cord = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(x_cord, y_cord)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        pointing = int(round(self.snake_head.heading(), 0))
        if pointing != 270:
            self.snake_head.setheading(90)

    def left(self):
        pointing = int(round(self.snake_head.heading(), 0))
        if pointing != 0:
            self.snake_head.setheading(180)

    def down(self):
        pointing = int(round(self.snake_head.heading(), 0))
        if pointing != 90:
            self.snake_head.setheading(270)

    def right(self):
        pointing = int(round(self.snake_head.heading(), 0))
        if pointing != 180:
            self.snake_head.setheading(0)