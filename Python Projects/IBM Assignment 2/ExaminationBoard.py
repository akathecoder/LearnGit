# Program to tell wheather the student passes or not.

a = int(input())
b = int(input())
c = int(input())

if (a <= b) and (b <= c):
    if (b>50) and (c>50):
        if (a>50):
            print("pass")
        elif (a>40) and (a+b+c > 150):
            print("deliberated")
    else:
        print("fail")
else:
    print("invalid input")


