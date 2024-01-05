lcm = 0 
i = 1
j = 2
gcd = 0
x = int(input("Enter First Number : "))
y = int(input("Enter Second Number : "))


while(i <= x and i <= y):
    if(x % i == 0 and y % i == 0):
        gcd = i
    i += 1
  
if(gcd == x or gcd == y):
    if(x > y):
        print(x)
    else:
        print(y)

if(gcd >= 1):
    lcm = (x*y)/gcd
    print(f"L.C.M of {x} and {y} is {lcm}") 