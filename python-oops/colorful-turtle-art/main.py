import turtle as t
import random

t.colormode(255)

timmy_the_turtle = t.Turtle()
timmy_the_turtle.speed("fastest")

for _ in range(200):
    timmy_the_turtle.circle(50)
    timmy_the_turtle.right(10)
    timmy_the_turtle.forward(10)

screen = t.Screen()
screen.exitonclick()
print("turtle graphic shape made")
