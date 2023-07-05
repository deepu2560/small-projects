import pandas
import turtle

us_states_data = pandas.read_csv("./us-states-game-start/50_states.csv")

us_state_name_list = us_states_data["state"].to_list()

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("US State Game")
img = "./us-states-game-start/blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

chances = 0
is_game_on = True
while is_game_on:
    user_answer = screen.textinput(title="Guess the state name?",
                                   prompt=f"What's another state's name?\nchance: {chances}/50")
    if user_answer in us_state_name_list:
        correct_answer = us_states_data[us_states_data["state"] == user_answer]
        write_correct_answer = turtle.Turtle()
        write_correct_answer.hideturtle()
        write_correct_answer.penup()
        write_correct_answer.goto(x=int(correct_answer["x"].to_list()[0]), y=int(correct_answer["y"].to_list()[0]))
        write_correct_answer.write(correct_answer["state"].to_list()[0], align="center", font=("Arial", 8, "normal"))

    chances += 1

    if chances >= 50:
        is_game_on = False
