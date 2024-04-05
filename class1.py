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

coffee_maker.report()
money_machine.report()


