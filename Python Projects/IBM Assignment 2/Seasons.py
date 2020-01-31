# Program to tell which season it is on a particular date and month in a year.

date = int(input())
month = input()
flag = 0
if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    if date > 31 or date < 1:
        print("Invalid Input")
        flag = 1
elif month == "April" or month == "June" or month == "September" or month == "November":
    if date > 30 or date < 1:
        print("Invalid Input")
        flag = 1
elif month == "February":
    if date > 28 or date < 1:
        print("Invalid Input")
        flag = 1
else:
    print("Invalid Input")

if flag == 0:
    if (month == "April" or month == "May") or (month == "March" and date >=21) or (month == "June" and date <=20):
        print("Its Spring.")
    elif (month == "July" or month == "August") or (month == "June" and date >=21) or (month == "September" and date <=22):
        print("Its Summer")
    elif (month == "October" or month == "November") or (month == "September" and date >=23) or (month == "December" and date <=20):
        print("Its Autumn")
    elif (month == "January" or month == "February") or (month == "December" and date >=21) or (month == "March" and date <=20):
        print("Its Winter")
