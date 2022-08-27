print("Hello there")
print("Welcome you to tip calculator")
bill = input("What was the total bill ? \n$ ")
total_people = input("How many people to split the bill? \n")
percent_input = input(
    "What percentage tip would you like to give? 10, 12 or 15? \n")

total_bill = float(bill) / int(total_people)

percentage = int(percent_input) / 100

total_percent = float(1) + percentage

to_pay = total_bill * total_percent

print(f"\nEach person should pay: $ {round(to_pay, 2)}")