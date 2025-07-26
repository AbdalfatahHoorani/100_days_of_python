MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

#TODO: asking for user's drink of choice
def drink():
    active = True
    while active:
        drink_of_choice = input("What would you like to drink? (espresso/latte/cappuccino): ")
        if drink_of_choice.lower() == "espresso":
            transactionChecker(drink_of_choice)
        elif drink_of_choice.lower() == "latte":
            transactionChecker(drink_of_choice)
        elif drink_of_choice.lower() == "cappuccino":
            transactionChecker(drink_of_choice)
        elif drink_of_choice.lower() == "report":
            report()
        # TODO: make a secret keyword "off" and keep it hidden when someone types it we kill the program
        elif drink_of_choice == "off":
            return print("the machine has turned off")
        else:
            print("that drink isn't on the menu :(")



#TODO: when "report" is entered by the user print information as shown the PDF
def report():
    # remove the print later?
    print(f"""
Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: {resources['money']}$""")


#TODO: check if there is enough resources for the drink the user wants
def resourceChecker(water: int, coffee: int, milk = 0):
    if water <= resources['water'] and coffee <= resources['coffee'] and milk <= resources['milk']:
        resources['water'] -= water
        resources['coffee'] -= coffee
        resources['milk'] -= milk
        return True
    elif water > resources['water']:
        print("Sorry there isn't enough water!")
        return False
    elif coffee > resources['coffee']:
        print("sorry there isn't enough coffee!")
        return False
    elif milk > resources['milk']:
        print("sorry there isn't enough milk!")
        return False

#TODO: process the coins that were given by the user calculate it and give the change back if there is any
def coinProcesser(drink_type):
    print(f"Please insert coins {MENU[drink_type]['cost']}")
    quarter = int(input("please insert quarters")) * 0.25
    dime = int(input("please insert dimes")) * 0.1
    nickle = int(input("please insert nickles")) * 0.05
    pennies = int(input("please insert pennies")) * 0.01
    total = quarter + dime + nickle + pennies
    if total == MENU[drink_type]['cost']:
        resources['money'] += MENU[drink_type]['cost']
        return True
    elif total > MENU[drink_type]['cost']:
        change = total - MENU[drink_type]['cost']
        print(f"Thank you for paying, here is your change{change:.2f}$.")
        resources['money'] += MENU[drink_type]['cost']
        return True
    else:
        print(f"Not enough money provided, here is your money {total}$.")
        return False


#TODO: check transaction successful? if we have enough resources and user has enough money then yes
def transactionChecker(drink_type):
    if resourceChecker(MENU[drink_type]['ingredients']['water'], MENU['espresso']['ingredients']['coffee']):
        if coinProcesser(drink_type):
            print(f"Transaction successful! here is your {drink_type}")
drink()
