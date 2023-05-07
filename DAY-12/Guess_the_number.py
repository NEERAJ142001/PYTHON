import random
import art

# game statement
print(art.logo)
print("Welcome to the NUMBER GUESSING GAME")
print("I'm thinking between a number between 1 and 100 \n")

# choosing a level "hard and easy"
level = input("choose a difficulty level,type 'easy' and 'hard' :\n ")

# creating a list number
numbers = []

# adding 0 to 100 number in list
for i in range(101):
    numbers.append(i)

# getting a random number from random package and choice function
computer_number = random.choice(numbers)


# METHOD 1 SHORT METHOD BY MAKING A CALCULATOR FUNCTION
#
# calculator common function for hard and easy level
def calculator(x, computer_number):
    print(f"You have {x} attempt left to guess a number")

    # loop from 0 to 4 =5 because u have 5 lives
    for i in range(x):

        # taking input from the user again
        user_choice_again = int(input("Guess your number : \n"))

        if x == 1:
            print("You lost the game, better luck next time")
            print(f"the correct answer is {computer_number}")
            break

        # comparing
        elif user_choice_again > computer_number:
            print("TOO HIGH")
            x = x - 1
            print(f"You have {x} attempt left to guess a number \n")

        # comparing
        elif user_choice_again < computer_number:
            print("TOO LOW")
            x = x - 1
            print(f"You have {x} attempt left to guess a number \n")

        # comparing
        elif user_choice_again == computer_number:
            print(f" YOU WIN!, the answer was the :'{computer_number}' \n")
            break


# # METHOD 2 LONG ONE
# # 1 hard level function

# def hard_level():
#     x = 5
#     print(f"You have {x} attempt left to guess a number")

#     # loop from 0 to 4 =5 because u have 5 lives
#     for i in range(5):
#         # taking input from the user again
#         user_choice_again = int(input("Guess your number \n"))

#         if x == 1:
#             print("You lost the game, better luck next time")
#             print(f"The correct answer is :'{computer_number}' \n")
#             break

#         # comparing
#         elif user_choice_again > computer_number:
#             print("too high")
#             x = x - 1
#             print(f"You have {x} attempt left to guess a number \n")
#
#         # comparing
#         elif user_choice_again < computer_number:
#             print("too low")
#             x = x - 1
#             print(f"You have {x} attempt left to guess a number \n")
#
#         # comparing
#         elif user_choice_again == computer_number:
#             print(f" You win!, the answer was the {computer_number} \n")
#             break
#
#
# # 2 easy level function
# def easy_level():
#     x = 10
#     print(f"You have {x} attempt left to guess a number")

#     # loop from 0 to 9 =10 because u have 10 lives
#     for i in range(10):
#         # taking input from the user again
#         user_choice_again = int(input("Guess your number \n"))

#         if x == 1:
#             print("You lost the game, better luck next time")
#             print(f"The answer is the :'{computer_number}' \n")
#             break

#         # comparing
#         elif user_choice_again > computer_number:
#             print("too high")
#             x = x - 1
#             print(f"You have {x} attempt left to guess a number \n")
#
#         # comparing
#         elif user_choice_again < computer_number:
#             print("too low")
#             x = x - 1
#             print(f"You have {x} attempt left to guess a number \n")
#
#         # comparing
#         elif user_choice_again == computer_number:
#             print(f" You win!, the answer was the {computer_number} \n")
#             break
#
#
# flag = True
# while flag:
#     if level == "hard":
#         hard_level()
#         break
#     else:
#         easy_level()
#         break

flag = True
while flag:
    if level == "hard":
        calculator(5, computer_number)
        break

    elif level == "easy":
        calculator(10, computer_number)
        break
