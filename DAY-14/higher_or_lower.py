import random
from game_data import data
import art

# Display art logo of game higher and lower
print(art.logo)

# printing the detail in the board in specific format

# # getting name from list-dictionary
# user_name1=user_1["name"]
# user_name2=user_2["name"]
#
# # getting description
# user_description1=user_1["description"]
# user_description2=user_2["description"]
#
# # getting country name
# user_country1=user_1["country"]
# user_country2=user_2["country"]
#
# print(f"Compare A : {user_name1} is a {user_description1} of {user_country1}")
# print(art.logo)
# print(f"Compare B : {user_name2} is a {user_description2} of {user_country2}")

# function that data and return the data in specific print format

# getting data for user1 and user2
user_1 = random.choice(data)
user_2 = random.choice(data)

# if we get same detail of user1 and user2 then change the value of user2 again
if user_2 == user_1:
    user_2 = random.choice(data)
score = 0
flag = True
while flag:

    user_1 = random.choice(data)
    user_2 = random.choice(data)

    # if we get same detail of user1 and user2 then change the value of user2 again
    if user_2 == user_1:
        user_2 = random.choice(data)

    def print_format(user):
        user_name = user["name"]
        user_description = user["description"]
        user_country = user["country"]
        return f" {user_name} is a {user_description} of {user_country}"


    # getting followers
    def followers(user):
        user_followers = user["follower_count"]
        return user_followers


    def check(guess):
        score = 0
        if followers(user_1) > followers(user_2):
            if guess == "a":

                return True
            else:
                return False

        elif followers(user_2) > followers(user_1):
            if guess == "b":

                return True
            else:
                return False


    # printing the data
    print(f"Compare A {print_format(user_1)}")
    print(art.vs)
    print(f"Against B {print_format(user_2)}")

    # asking user who has more followers
    user_guess = (input("Guess who has more followers?  type 'A' or 'B' :\n")).lower()
    answer = check(user_guess)

    if answer:
        score = score + 1
        print(f"You are right and your score is {score}\n")
        continue
    else:
        print(f"Sorry u lost and score is {score}")
        print("Have a great Day")
        break
