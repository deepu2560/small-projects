PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as all_names:
    names = all_names.readlines()

    with open("./Input/Letters/starting_letter.txt") as letter_format:
        letter = letter_format.read()

        for name in names:
            name = name.strip()
            final_letter = letter.replace(PLACEHOLDER, name)
            with open(f"./Output/ReadyToSend/invite_letter_for_{name}.txt", mode="w") as invite_letter:
                invite_letter.write(final_letter)
