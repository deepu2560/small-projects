rock = "🪨"

paper = "📄"

scissors = "✂️"

#Write your code below this line 👇

import random

lists = [rock, paper, scissors]

user_choice = int(
    input(
        "Your turn. Choose 0 for rock, 1 for paper and 2 for scissors. What's your choice? \n"
    ))

if(user_choice>2 or user_choice<0):
    print("Your chose invalid number try again...")
else:
    computer_choice = random.randint(0, len(lists) - 1)

    print(f"You choose: {lists[user_choice]} \n")

    print(f"Computer choose: {lists[computer_choice]} \n")

    if (user_choice == 0 and computer_choice == 1):
        print("You lose this Match. Try again...")
    elif (user_choice == 1 and computer_choice == 2):
        print("You lose this Match. Try again...")
    elif (user_choice == 2 and computer_choice == 0):
        print("You lose this Match. Try again...")
    elif (user_choice == computer_choice):
        print("Match draw. Let's play another one...")
    else:
        print("You won this Match. Yeppie...")
