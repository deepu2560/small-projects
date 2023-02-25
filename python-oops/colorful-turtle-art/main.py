from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

print("hello world")
def curve(num):
    for i in range(num):
        timmy_the_turtle.left(1)
        timmy_the_turtle.forward(1)


timmy_the_turtle.shape("turtle")

timmy_the_turtle.fillcolor("red")
timmy_the_turtle.begin_fill()
timmy_the_turtle.left(55)
timmy_the_turtle.forward(200)
curve(num=200)
timmy_the_turtle.right(160)
curve(num=200)
timmy_the_turtle.left(5)
timmy_the_turtle.forward(210)
timmy_the_turtle.left(100)
timmy_the_turtle.end_fill()


screen = Screen()
screen.exitonclick()
print("turtle graphic shape made")
