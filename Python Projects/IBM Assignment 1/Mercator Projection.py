# This Program converts the mercator projection coordinates into (x,y) on a rectangle of 360x180 with (0,0) at center.

import math
lamda = float(input())
lamdaNaut = float(input())
omega = float(input())

x = (lamda-lamdaNaut+(180%360))-180
y = 15*(math.log((1+math.sin(math.radians(omega)))/(1-math.sin(math.radians(omega)))))

print("x:",x)
print("y:",y)
