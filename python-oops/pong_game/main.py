from turtle import Screen
from player import Player
from ball import Ball
from score import Score
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

player_one = Player(position=(-350, 0), clr="red")
player_two = Player(position=(350, 0), clr="blue")

ball = Ball()
score = Score()

screen.listen()
screen.onkey(player_two.move_up, "Up")
screen.onkey(player_two.move_down, "Down")
screen.onkey(player_one.move_up, "w")
screen.onkey(player_one.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    if ball.distance(player_two) < 60 and ball.xcor() > 320 or ball.distance(player_one) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 340:
        score.left_scored()
        ball.reset_ball()
    elif ball.xcor() < -340:
        score.right_scored()
        ball.reset_ball()

    if score.score_left >= 10:
        score.who_won(player="Red")
        game_is_on = False
    elif score.score_right >= 10:
        score.who_won(player="Blue")
        game_is_on = False

screen.exitonclick()
