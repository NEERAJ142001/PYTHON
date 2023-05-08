from necessay_data import MENU, resources

'''     Print a coffee
        check resources are sufficient?
        process coins
        check transaction successful or not
        Make a coffee'''
flag = True
profit = 0


# check the resources are available to make a product or not--(drinks[ingredients])
def is_sufficient_resources(order_ingredients):
    for i in order_ingredients:
        # checking the ingredients r available
        if order_ingredients[i] >= resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


# getting the coins from user and fetch the total amount that he has paid
def process_coins():
    print("Please insert coins.")
    total = int(input("how many 1 coins?: ")) * 1
    total = total + int(input("how many 2 coins?: ")) * 2
    total = total + int(input("how many 5 coins?: ")) * 5
    total = total + int(input("how many 10 coins?: ")) * 10

    return total


def is_transaction_having_enough_money_tobe_successful(money_received, drink_cost):
    # drink_cost=drink["cost"]
    # if money received is greater than drink-cost  then refund it
    if money_received >= drink_cost:
        change = money_received - drink_cost

        print(f"Here is your {change} in return.")
        global profit
        profit = profit + drink_cost
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# making the coffee means we are using the resources soo subtract the resources
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] = resources[item] - order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while flag:
    # take an input from the user what they want
    choice = input("What would you like? (espresso/latte/cappuccino):")

    # to turn off the machine
    if choice == "off":
        break

    # printing the report of machine
    elif choice == "report":
        print(f"water :{resources['water']} ml")
        print(f"Milk :{resources['milk']} ml")
        print(f"Coffee :{resources['coffee']} g")
        print(f"Money :₹ {profit}")

    else:
        # user entered a coffee name (espresso/latte/cappuccino)
        drink = MENU[choice]

        # is_sufficient_resources check the availability of resources and get the payment
        if is_sufficient_resources(drink["ingredients"]):
            payment = process_coins()
            # then check payment in successful or not then make a coffee
            if is_transaction_having_enough_money_tobe_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
