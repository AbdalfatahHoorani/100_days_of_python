from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

options = menu.get_items()

on = True
while on:
    user_input = input(f"please choose an option. {options} \n")
    if menu.find_drink(user_input):
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    elif user_input.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input.lower() == "off":
        on = False




