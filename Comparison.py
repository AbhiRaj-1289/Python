x = int(input("Enter First Number : "))
y = int(input("Enter Second Number : "))
z = int(input("Enter Third Number : "))
if (x > y) and (x > z):
    print("Gretaest =", x)
elif y > z:
    print("Greatest =", y)
else:
    print("Greatest =", z)