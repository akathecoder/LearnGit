# This Program converts Arabic numeral into Roman Numerals.

n = int(input())
if n>0:
    roman = ""
    while n>0:
        if n>=1000:
            roman +="M"
            n-=1000
        elif n>=900:
            roman +="CM"
            n-=900
        elif n>=500:
            roman +="D"
            n-=500
        elif n>=400:
            roman +="CD"
            n-=400
        elif n>=100:
            roman +="C"
            n-=100
        elif n>=90:
            roman +="XC"
            n-=90
        elif n>=50:
            roman +="L"
            n-=50
        elif n>=40:
            roman +="XL"
            n-=40
        elif n>=10:
            roman +="X"
            n-=10
        elif n>=9:
            roman +="IX"
            n-=9
        elif n>=5:
            roman +="V"
            n-=5
        elif n>=4:
            roman +="IV"
            n-=4
        elif n>=1:
            roman +="I"
            n-=1
        else:
            break
    print(roman)
else:
    print("Please enter a Postive Numeral only. Try Again.")
