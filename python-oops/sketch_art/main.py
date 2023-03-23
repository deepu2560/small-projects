import turtle as trtl

myturtle = trtl.Turtle()


def move_forward():
    myturtle.forward(10)


def move_backend():
    myturtle.backward(10)


def move_left():
    new_head = myturtle.heading() + 10
    myturtle.setheading(new_head)


def move_right():
    new_head = myturtle.heading() - 10
    myturtle.setheading(new_head)


def reset():
    myturtle.penup()
    myturtle.clear()
    myturtle.home()
    myturtle.pendown()


scrn = trtl.Screen()
scrn.listen()
scrn.onkey(move_forward, "w")
scrn.onkey(move_backend, "s")
scrn.onkey(move_left, "a")
scrn.onkey(move_right, "d")
scrn.onkey(reset, "e")
scrn.exitonclick()

