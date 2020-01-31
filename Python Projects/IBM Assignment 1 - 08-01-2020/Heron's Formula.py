# This Program tells the area of a triangle using Heron's Formula.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

a = ((x1-x2)**2 + (y1-y2)**2)**0.5
b = ((x2-x3)**2 + (y2-y3)**2)**0.5
c = ((x3-x1)**2 + (y3-y1)**2)**0.5
s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5
print('%.2f'%area)
