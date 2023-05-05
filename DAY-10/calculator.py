import calculator_art
print(calculator_art.logo)
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    return a / b


def modulus(a, b):
    return a % b


# creating a dictionary
calculator = {"+": addition, "-": subtraction, "*": multiply, "/": division, "%": modulus}

flag = True


def calci():
    # taking input from user
    number1 = float(input("Enter the first number \n"))

    # printing operators on the screen
    for keys in calculator:
        print(keys)

    while flag:
        # taking operator and next number

        operator_symbol = input("pick an operator \n")
        number2 = float(input("Enter the number \n"))

        calculation_symbol = calculator[operator_symbol]

        # call the function
        result = calculation_symbol(number1, number2)
        # printing the output in a format
        print(f"{number1} {operator_symbol} {number2} = {result} \n")

        # asking user to continue or not
        choice = input(f"type 'y' to continue with {result} \n"
                       f"or type 'n' to exit \n"
                       f"or start a new calculation type 's'\n")
        # for continue with the same calculation
        if choice == "y":
            number1 = result

        # for creating a new calculation
        elif choice == 's':
            calci()

        # exit point
        else:
            break


calci()
