x = int(input("Enter First Number : "))
y = int(input("Enter Second Number : "))
i = 1
gcd = 0
while (i <= x and i <= y):
    if(x % i == 0 and y % i == 0):
        gcd = i
    i += 1
print("G.C.D Of "+str(x)+" and "+str(y)+" is "+str(gcd))    