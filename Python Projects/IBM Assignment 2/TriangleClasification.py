import math
import numpy as np


x1 = float(input("x1 : "))
y1 = float(input("y1 : "))
x2 = float(input("x2 : "))
y2 = float(input("y2 : "))
x3 = float(input("x3 : "))
y3 = float(input("y3 : "))

"""
x1 = float(-5.018651714882998)
y1 = float(5.273815977515895)
x2 = float(-4.1327268984230505)
y2 = float(5.7376448463677665)
x3 = float(-4.596555767274922)
y3 = float(6.623569662827715)
"""

a = (((x1-x2)**2) + ((y1-y2)**2))**0.5
b = (((x2-x3)**2) + ((y2-y3)**2))**0.5
c = (((x3-x1)**2) + ((y3-y1)**2))**0.5

a = round(a , 5)
b = round(b , 5)
c = round(c , 5)

if a == b == c:
    print("This triangle is Equilateral and ")
elif a == b or b == c or a == c:
    print("This triangle is Isosceles and ")
else:
    print("This triangle is Scalene and ")

alpha = ((a**2) + (b**2) - (c**2))/(2*a*b)
beta = ((b**2) + (c**2) - (a**2))/(2*b*c)
gamma = ((c**2) + (a**2) - (b**2))/(2*c*a)

alpha = math.acos(alpha)
beta = math.acos(beta)
gamma = math.acos(gamma)

alpha = round(np.rad2deg(alpha) , 2)
beta = round(np.rad2deg(beta) , 2)
gamma = round(np.rad2deg(gamma) , 2)

if alpha > 90 or beta > 90 or gamma > 90:
    print("Obtuse Triangle.")
elif alpha == 90 or beta == 90 or gamma == 90:
    print("Right Angle Triangle.")
else:
    print("Acute Triangle.")