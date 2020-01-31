person1 = input()
person2 = input()
num = int(input())

if num == 1:
    if person1 == "white":
        person1 = "black"
    else:
        person1 = "white"

elif num == 2:
    if person2 == "white":
        person2 = "black"
    else:
        person2 = "white"

print(person1+"\n"+person2)