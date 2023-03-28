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
player_one.goto(x=-350, y=0)

player_two = Player()
player_two.goto(x=350, y=0)

ball = Ball()

screen.listen()
screen.onkey(player_two.move_up, "Up")
screen.onkey(player_two.move_down, "Down")
screen.onkey(player_one.move_up, "w")
screen.onkey(player_one.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    if ball.distance(player_two) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(player_one) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 370 or ball.xcor() < -370:
        game_is_on = False

screen.exitonclick()
