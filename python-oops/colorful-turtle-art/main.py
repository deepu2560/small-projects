from turtle import Turtle, Screen

timmy_the_turtle = Turtle()


for num in range(3, 10):
    for _ in range(num):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(360/num)


print("turtle graphic shape made")
