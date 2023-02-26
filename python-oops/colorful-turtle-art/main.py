import turtle as t
import random

t.colormode(255)

timmy_the_turtle = t.Turtle()
timmy_the_turtle.speed("fastest")

for _ in range(100):
    timmy_the_turtle.circle(100)
    timmy_the_turtle.setheading(timmy_the_turtle.heading()+10)

screen = t.Screen()
screen.exitonclick()
print("turtle graphic shape made")
