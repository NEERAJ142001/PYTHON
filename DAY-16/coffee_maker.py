class CoffeeMaker:
    """Models the machine that makes the coffee"""
    # it has three functions=>report,is_resource_sufficient,make_coffee
    def __init__(self):
        self.resources = {
            "water": 1000,
            "milk": 1000,
            "coffee": 1000,
        }

    def report(self):
        # Prints a report of all resources like water, milk and coffee.
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        # Returns True when order can be made and means resources are available or not.
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        # makes the coffee and deduct the resources
        for item in order.ingredients:
            self.resources[item] =self.resources[item]- order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
