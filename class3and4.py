from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO - Step 1: Print Report
# create objects stored inside variables
# object naming is lower case and uses _. Can be named anything
# class has uppercase
# object = class
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


# TODO - Step 2: Check Resources Sufficient?
# TODO - Step 3: Process coins
# TODO - Step 4: Check if transaction is successful?

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What do would you like? {options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        #drink = menu.find_drink(self, order_name)
        drink = menu.find_drink(choice) # takes "order_name" as the input.
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)

