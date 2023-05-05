import os
import art

# printing the logo
print(art.logo)
# creating a dictionary
bid_dictionary = {}
flag = True
highest_bid_value = 0
winner = ""


# this function calculates the highest bidder
def highest_bidder(all_bids):
    global highest_bid_value
    global winner

    for keys in all_bids:
        temp = all_bids[keys]
        if temp > highest_bid_value:
            highest_bid_value = temp
            winner = keys
    print(f"The winner is '{winner}',with the highest bid of{highest_bid_value}")


# it continue until flag become false
while flag:
    name = input("Enter the bidder name?\n")
    bid_price = int(input("what's your bid price?\n"))
    bid_dictionary[name] = bid_price

    next = input("Do you have more bids remaining: yes/no \n")
    if next == "yes" or next == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    elif next == "no" or next == "n":
        highest_bidder(bid_dictionary)
        print("Thanks for your bidding")
        break
