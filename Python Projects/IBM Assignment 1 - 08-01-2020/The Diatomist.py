# This Program tells the total area covered by small circles in a large circle.

import math
r = float(input())
R = float(input())

n = int((0.83*(R**2)/(r**2))-1.9)

smallArea = (math.pi*r*r)*n
largerArea = math.pi*R*R
percentage = (smallArea*100)/largerArea

print(n,"smaller circles cover",'%.2f'%percentage+"%","of the larger circle")
