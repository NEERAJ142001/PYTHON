# making a tip calculator
print("Welcome to the tip calculator!")
# getting the bill amount
bill_amount = float(input("What was the total bill? \n"))

# asking user to enter the tip
tip = int(input("How much tip would you like to give? 10, 12, or 15? \n"))

# in how many person they want to split the bill
number_of_person = int(input("How many people to split the bill? \n"))

# change into percentage
tip_as_percent = tip / 100

# calculating tip amount
total_tip_amount = bill_amount * tip_as_percent

# total bill
total_bill = bill_amount + total_tip_amount

# split the bill
bill_per_person = total_bill / number_of_person

# round off total bill amount upto 2 places
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: {final_amount} rupees \n")