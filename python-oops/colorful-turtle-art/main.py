from turtle import Turtle, Screen

timmy_the_turtle = Turtle()


for _ in range(4):
    for _ in range(5):
        timmy_the_turtle.pendown()
        timmy_the_turtle.forward(20)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(20)
    timmy_the_turtle.left(90)

print("turtle graphic shape made")
