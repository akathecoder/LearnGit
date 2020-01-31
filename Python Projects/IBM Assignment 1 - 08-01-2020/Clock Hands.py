# This Program finds the minimum angle between the Hour Hand and the minute hand.

hh = int(input())
mm = int(input())
h = hh
if hh>=12:
    hh -= 12

#Hours Hand from 12
hhDegree = (hh*30) + (mm*0.5)

#Minutes Hand from 12
mmDegree = mm*6

Degree = min(abs(hhDegree-mmDegree),360-abs(hhDegree-mmDegree))
print("At ",'%02d'%h,":",'%02d'%mm," both hands form an angle of ",str(Degree),chr(176),".",sep="")
