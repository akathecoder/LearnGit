# Program to find the weekly pension based on sex and age.

sex = input()
age = int(input())

if sex == "man":
    if age > 70:
        print("70")
    elif age > 65:
        print("50")
    else:
        print("not pensionable")

elif sex == "woman":
    if age > 65:
        print("70")
    elif age > 60:
        print("45")
    else:
        print("not pensionable")

else:
    print("Wrong Input.")
