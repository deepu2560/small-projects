from turtle import Turtle, Screen

timmy_the_turtle = Turtle()


def turn_left():
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(100)


timmy_the_turtle.forward(100)
turn_left()
turn_left()
turn_left()

screen = Screen()
screen.exitonclick()

print("turtle graphic shape made")
