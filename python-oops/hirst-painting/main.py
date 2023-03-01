import colorgram
import turtle as t

colors = colorgram.extract("image.jpg", 30)
print(len(colors))

draw = t.Turtle()
t.colormode(255)

count = -1

for num in range(0, 5):
    draw.penup()
    draw.goto(-50.00, float(50*num))
    for _ in range(6):
        count += 1
        rgb = colors[count].rgb
        clr = (rgb.r, rgb.g, rgb.b)
        draw.pendown()
        draw.dot(20, clr)
        draw.penup()
        draw.forward(50)

screen = t.Screen()
screen.exitonclick()
