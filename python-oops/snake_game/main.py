from turtle import Screen
from snakes import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_head.distance(food) < 15:
        food.refresh()
        score.count_score()
        snake.extend_snake()

    if snake.check_wall_collision():
        game_is_on = False
        score.game_over()

    for snk in snake.snakes[:1:-2]:
        if snake.snake_head.distance(snk) < 20:
            game_is_on=False
            score.game_over()


screen.exitonclick()
