# This Program calculates the Mean and Variance of a sample space of 5.

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())

mean = (n1+n2+n3+n4+n5)/5

var = ((n1-mean)**2)+((n2-mean)**2)+((n3-mean)**2)+((n4-mean)**2)+((n5-mean)**2)
var /= 4

print('%.2f'%mean)
print('%.2f'%var)
