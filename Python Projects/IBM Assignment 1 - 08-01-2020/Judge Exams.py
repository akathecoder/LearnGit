# This Program tells the number of the undiscovered errors using probability.

a = int(input())
b = int(input())
c = int(input())
unDisrd = (a-c)*(b-c)/c
print("There are",'%.2f'%unDisrd,"undiscovered errors.")
