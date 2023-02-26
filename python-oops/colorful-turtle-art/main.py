import turtle as t
import random

t.colormode(255)
timmy_the_turtle = t.Turtle()
timmy_the_turtle.speed("fast")
timmy_the_turtle.pensize(5)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    color_tuple = (red, green, blue)

    return color_tuple


turn_angle = [0, 90, 180, 270]

for _ in range(200):
    clr = random_color()
    timmy_the_turtle.color(clr)
    timmy_the_turtle.forward(20)
    timmy_the_turtle.left(random.choice(turn_angle))


screen = t.Screen()
screen.exitonclick()
print("turtle graphic shape made")
