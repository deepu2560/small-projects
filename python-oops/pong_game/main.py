from turtle import Screen
from player import Player

screen = Screen()
screen.setup(width=600, height=500)
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

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
