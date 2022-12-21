x = int(input("Enter First Number : "))
y = int(input("Enter Second Number : "))
z = int(input("Enter Third Number : "))
if (x >= y) and (x >= z):
    print("Greatest = ",x)
    if(y > z):
        print("Middle No. = ",y)
        print("Smallest No. = ",z)
    else:
        print("Middle No. = ",z)
        print("Smallest No. ",y)
if(y >= x) and (y >= z):
    print("Greatest = ",y)
    if(x > z):
        print("Middle No. ",x)
        print("Smallest No. ",z)
    else:
        print("Middle No. = ",z)
        print("Smallest No. = ",x)
if(z >= y) and (z >= x):
    print("Greatest = ",z)
    if(x > y):
        print("Middle No. = ",x)
        print("Smallest No. = ",y)
    else:
        print("Middle No. = ",y)
        print("Smallest No. = ",x)