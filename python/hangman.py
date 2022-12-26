import random

#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

user_guess = input("Make a Guess \n")

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
isContain = False

for x in chosen_word:
    if (x == user_guess):
        isContain = True

print(isContain)
