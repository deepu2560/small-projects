logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)


def add(n1, n2):
    return n1 + n2


def multiple(n1, n2):
    return n1 * n2


def substract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


operations = {"-": substract, "+": add, "/": divide, "*": multiple}


def program():
    num1 = float(input("what's the first number?: "))
    for symbol in operations:
        print(symbol)

    end_calculation = False

    while not end_calculation:
        operation_symbol = input("Pick an operation: ")
        if operation_symbol not in operations:
            print(f"Wrong input. Your last result was {num1}")
            return None
        num2 = float(input("what's the next number?: "))
        calculatin_function = operations[operation_symbol]
        answer = calculatin_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        final = input(
            f"Type 'y' to continue calculation with {answer} or type 'n' to restart calculation: "
        )

        if final == "y":
            num1 = answer
        elif final == "n":
            program()
        else:
            print(f"Your final result was {answer}")
            end_calculation = True
            return None


program()