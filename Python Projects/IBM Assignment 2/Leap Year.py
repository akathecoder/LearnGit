# Program to tell whether a year is Leap Year or not.

year = int(input("Enter Year : "))
if (year > 0) and (year < 10000):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 == 0):
        print(year, "is a Leap Year.")
    else:
        print(year, "is not a Leap Year.")
else:
    print("Please Enter an appropriate value.")