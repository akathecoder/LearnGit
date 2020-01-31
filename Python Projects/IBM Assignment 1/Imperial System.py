# This Program converts Length in Imperial syste to Metric System.

metre = float(input())
inch = 39.45 * metre
foot = inch//12
inch = int(round(inch%12))
yard = int(foot//3)
foot = int(foot%3)
print(yard,foot,inch,sep="\n")
