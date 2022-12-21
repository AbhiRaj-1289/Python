x = int(input("Enter a Number : "))
sum = 0
temp = x
while temp > 0:
    digit = temp %10
    sum += digit ** 3
    temp //= 10
if x == sum:
    print("Given Number Is An Armstrong Number")
else:
    print("Given Number Is Not An Armstrong Number")