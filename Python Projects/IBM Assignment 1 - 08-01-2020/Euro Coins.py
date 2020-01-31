# This Program tells the total number of coins and total money in Euro.

p1 = int(input())
p2 = int(input())
p5 = int(input())
p10 = int(input())
p20 = int(input())
p50 = int(input())
r1 = int(input())
r2 = int(input())

total_coins = p1+p2+p5+p10+p20+p50+r1+r2

amt = p1+(p2*2)+(p5*5)+(p10*10)+(p20*20)+(p50*50)
amt = amt/100
amt += r1+(r2*2)

print(total_coins)
print(amt)
