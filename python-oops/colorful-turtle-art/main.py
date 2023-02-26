from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.speed("fast")
timmy_the_turtle.pensize(5)

colors = ["black", "teal", "slate gray", "aquamarine", "cornflower blue", "royal blue",
          "blue", "navy", "midnight blue", "deep sky blue", "dodger blue", "steel blue", "cyan", "medium turquoise",
          "green", "dark green", "green yellow", "orange", "peru", "goldenrod", "brown", "orange red", "red",
          "deep pink", "purple", "magenta", "dark violet", "indigo", "lavender", "dark slate blue", "yellow"]

turn_angle = [0, 90, 180, 270]

for _ in range(200):
    clr = float(f"0.{random.randint(0, 255)}"), float(f"0.{random.randint(0, 255)}"), float(f"0.{random.randint(0, 255)}")
    timmy_the_turtle.color(clr)
    timmy_the_turtle.forward(20)
    timmy_the_turtle.left(random.choice(turn_angle))


screen = Screen()
screen.exitonclick()
print("turtle graphic shape made")
