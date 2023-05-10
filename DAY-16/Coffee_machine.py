from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

'''Print a coffee
    check resources are sufficient?
        process coins
        check transaction successful or not
        Make a coffee'''
# creating an objects
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu_get_items = Menu()

flag = True
while flag:
    # get all the items and print it and get user choice
    menu_items = menu_get_items.get_items()
    choice = input(f"Choice one option '{menu_items}off/report :\n")

    # for closing the machine
    if choice == "off":
        break
    # for getting the report of the machine
    elif choice == "report":
        # showing report of water,milk and coffee
        coffee_maker.report()
        # showing report of money
        money_machine.report()

    else:
        # find the drink is present or not
        drink = menu_get_items.find_drink(choice)
        # checking resources are available or not to make a coffee
        # if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        if coffee_maker.is_resource_sufficient(drink):
            # executing the payment part and refunding the extra amount
            if money_machine.make_payment(drink.cost):
                # make a coffee and deduct the resources that are used in making the coffee
                coffee_maker.make_coffee(drink)
