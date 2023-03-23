import turtle as trtl

myturtle = trtl.Turtle()


def move_forward():
    myturtle.forward(100)


scrn = trtl.Screen()
scrn.listen()
scrn.onkey(move_forward, "w")
scrn.exitonclick()

