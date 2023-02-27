import colorgram
import turtle as t

colors = colorgram.extract("image.jpg", 35)
print(len(colors))

draw = t.Turtle()
t.colormode(255)

count = -1

# for num in range(1, 6):
#     draw.penup()
#     for _ in range(7):
#         print(count)
#         count += 1
#         rgb = colors[count].rgb
#         clr = (rgb.r, rgb.g, rgb.b)
#         draw.pendown()
#         draw.dot(20, clr)
#         draw.forward(50)
#         draw.penup()
#     draw.penup()
#     draw.home()
#     draw.left(90)
#     draw.forward(10*num)
#     draw.right(90)

screen = t.Screen()
screen.exitonclick()