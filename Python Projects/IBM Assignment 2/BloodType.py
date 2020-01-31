x = input()
y = input()

if (x=="A") or (y=="A"):
    if (x=="B") or (y=="B"):
        print("The combination of ABO alleles "+x+" and "+y+" results in blood type AB.")
    elif (x=="O") or (y=="O"):
        print("The combination of ABO alleles " + x + " and " + y + " results in blood type A.")
    else:
        print("The combination of ABO alleles " + x + " and " + y + " results in blood type A.")

elif (x=="B") or (y=="B"):
    if (x=="B") or (y=="B"):
        print("The combination of ABO alleles " + x + " and " + y + " results in blood type B.")
    else:
        print("The combination of ABO alleles " + x + " and " + y + " results in blood type B.")

else:
    print("The combination of ABO alleles " + x + " and " + y + " results in blood type O.")
