from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# TODO: print report
# TODO: check resources sufficient
# TODO: process coin
# TODO: Check transaction successful
# TODO: make coffee

# object = Class()
# object.attribute =
# object.method(..,..)

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

start = True
while start:
    options = menu.get_items()
    order_ask = input(f"What would you like? ({options}) ")
    if order_ask == "off":
        start = False
    elif order_ask == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order_info = menu.find_drink(order_ask)
        if coffee_maker.is_resource_sufficient(order_info):
            order_cost = order_info.cost
            if money_machine.make_payment(order_cost):
                coffee_maker.make_coffee(order_info)
