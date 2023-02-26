from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.speed(2)
timmy_the_turtle.pensize(5)

colors = ["black", "teal", "slate gray", "aquamarine", "cornflower blue", "royal blue",
          "blue", "navy", "midnight blue", "deep sky blue", "dodger blue", "steel blue", "cyan", "medium turquoise",
          "green", "dark green", "green yellow", "orange", "peru", "goldenrod", "brown", "orange red", "red",
          "deep pink", "purple", "magenta", "dark violet", "indigo", "lavender", "dark slate blue", "yellow"]

for _ in range(100):
    timmy_the_turtle.color(random.choice(colors))
    timmy_the_turtle.forward(20)
    turn = random.randint(1, 2)
    if turn == 1:
        timmy_the_turtle.left(90)
    else:
        timmy_the_turtle.right(90)


screen = Screen()
screen.exitonclick()
print("turtle graphic shape made")
