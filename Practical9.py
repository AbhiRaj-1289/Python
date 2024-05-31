#Python code to find GCD of two numbers

x = int(input("Enter First Number : "))
y = int(input("Enter Second Number : "))
i = 1
gcd = 0
while(i <= x and i <= y):
    if(x % i == 0 and y % i == 0):
        gcd = i
    i += 1
print(f"G.C.D. of {x} and {y} is {gcd}")