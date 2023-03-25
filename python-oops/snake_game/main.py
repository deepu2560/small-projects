from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_positions = [(0, 0), (-20, 0), (-40, 0)]
snakes = []

for position in snake_positions:
    tim = Turtle("square")
    tim.color("white")
    tim.penup()
    tim.goto(position)
    snakes.append(tim)

game_is_on = True
while game_is_on:
    screen.update()
    for snake_num in range(len(snakes)-1, 0, -1):
        x_cord = snakes[snake_num-1].xcor()
        y_cord = snakes[snake_num-1].ycor()
        snakes[snake_num].goto(x_cord, y_cord)
    snakes[0].forward(1)

screen.exitonclick()
