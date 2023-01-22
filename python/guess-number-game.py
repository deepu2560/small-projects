#Number Guessing Game:

import pyfiglet
import random

logo = pyfiglet.figlet_format("NUMBER GUESSING GAME")

print(logo)

print("Welcome to number guessing game")

mode = input("What type of mode you want to choose? 'easy' or 'hard'?\n")

correctNumber = random.randint(0, 101)


def gameStart(selectMode):
    totalGuess = 10
    if selectMode == "hard":
        totalGuess = 5
    gameOver = False

    while totalGuess > 0 and not gameOver:
        print(f"You have total {totalGuess} guesses remaining.")
        guess = int(input("Guess a number: "))

        if guess == correctNumber:
            print("You guessed correct number. You won.")
            gameOver = True
        elif guess > correctNumber:
            print("Your guess is higher than number.")
            totalGuess -= 1
        elif guess < correctNumber:
            print("Your guess is lower than number.")
            totalGuess -= 1

        if totalGuess == 0:
            print("Your have 0 guesses remaining. You lost.")
            print("Correct Number was", correctNumber)


if mode == "easy" or mode == "hard":
    gameStart(selectMode=mode)
else:
    print("You typed an invalid choice.")
