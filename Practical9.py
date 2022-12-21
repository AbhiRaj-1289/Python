x = int(input("Enter First Number : "))
y = int(input("Enter Second Number : "))
i = 1
while (i <= x and i <= y):
    if(x % i == 0 and y % i == 0):
        result = i
    i += 1
print("G.C.D Of "+str(x)+" and "+str(y)+" is "+str(result))    