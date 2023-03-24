from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your bet?", prompt="Which turtle will win the race? Enter your color.\n"
                                                              "\n colors:- red, orange, black, green, "
                                                              "blue, purple")
colors = ["red", "orange", "black", "green", "blue", "purple"]
turtles = []

for num in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[num].speed("slow")
    turtles[num].color(colors[num])
    turtles[num].penup()
    turtles[num].goto(x=-230, y=(150-(num*50)))

Game_is_on = False

if user_choice:
    Game_is_on = True
else:
    print("You didn't selected any turtle. Play again and select a turtle to bet.")

while Game_is_on:
    for num in range(6):
        position = int(round(turtles[num].xcor(), 0))
        if position > 230:
            Game_is_on = False
            if user_choice == colors[num]:
                print(f"You won the bet. {colors[num]} won the match")
            else:
                print(f"You Lose the bet. {colors[num]} won the match")
            break
        turtles[num].forward(randint(a=2, b=10))

# screen.exitonclick()
