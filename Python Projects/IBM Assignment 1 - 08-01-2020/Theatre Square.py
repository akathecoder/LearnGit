# This Program tells the mininum number of square tiles required

m = int(input())
n = int(input())
a = int(input())

l = m//a
w = n//a
if m%a != 0:
    l += 1
if n%a != 0:
    w += 1

print("You need",l*w,"tiles of",a,"cm to cover a floor of",m,"x",n,"cm2.")
