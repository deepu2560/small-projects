from turtle import Screen
from player import Player
from ball import Ball
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

player_one = Player()
player_one.goto(x=-280, y=0)

player_two = Player()
player_two.goto(x=280, y=0)

screen.listen()
screen.onkey(player_two.move_up, "Up")
screen.onkey(player_two.move_down, "Down")
screen.onkey(player_one.move_up, "w")
screen.onkey(player_one.move_down, "s")

ball = Ball()

game_is_on = True

while game_is_on:
    ball.move()
    screen.update()
    time.sleep(0.1)

    if ball.ycor() > 210 or ball.ycor() < -210:
        ball.bounce(angle=90)

    if ball.distance(player_one) < 30 or ball.distance(player_two) < 30:
        ball.bounce(angle=90)

    if ball.xcor() > 280 or ball.xcor() < -280:
        game_is_on = False

screen.exitonclick()
