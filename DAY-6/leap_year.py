year = int(input("Enter a year \n"))


def leap_year(x):
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                print("Leap year")
            else:
                print("Not a Leap year")
        else:
            print("Leap year")
    else:
        print("Not a Leap year")


leap_year(year)
