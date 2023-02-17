from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_make = CoffeeMaker()
money = MoneyMachine()

machine_on = True

while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(coffee_make.report())
        print(money.report())
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        if coffee_make.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_make.make_coffee(drink)

