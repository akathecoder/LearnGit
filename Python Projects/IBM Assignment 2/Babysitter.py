# Program to print the total a Babysitter will get for his/her work.

h1=int(input("Enter Hour1: "))
m1=int(input("Enter Minute1: "))
h2=int(input("Enter Hour2: "))
m2=int(input("Enter Minute1: "))
if h2==0:
    h2=24
t1,t2=0,0
if h1>=18 and h2<=21 and m2<=30:
    t1 += ((60-m1)+m2)+((h2-h1-1)*60)
elif h1>=21 and h2<=24 and m1>=30:
    t2 += (60-m1)+((h2-h1-1)*60)
elif h1>=18 and h2>21:
    t1 += ((60-m1)+30)+((21-h1-1)*60)
    t2 += (m2+30) + ((h2-21-1)*60)
#print(t1,t2)
print("Wage: ",(2*t1 + 4*t2)/60)