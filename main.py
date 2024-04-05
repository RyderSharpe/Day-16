from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def welcome():
    print('''\033[33m
             )))
            (((
          +-----+
          |     |] - WELCOME TO THE COFFEE MACHINE!
          `-----' 
          \033[m
        ''')
# money_machine = MoneyMachine


coffee_maker = CoffeeMaker() # Create an instance of the CoffeeMaker class
menu = Menu()
menu_items = menu.get_items()


is_on = True
while is_on:
    welcome()
    print(f"\033[1mMenu: {menu_items}\033[0m")
    print('''\x1B[3mPS: Type "report" at any moment to check our resources available. 
    Type "off" to log out from the machine\x1B[0m.\n''')

    user_input = input("What would you like? \n").lower()
    if user_input == "report":
        coffee_maker.report()
    elif user_input in menu_items.split('/'):
        coffee_maker.is_resource_sufficient(menu.find_drink(user_input))

        # drink = menu.find_drink(user_input)
        # print(f"Here is your  {drink.name}")

    break
