#Python code to print factorial of a number

fact = 1
n = int(input("Enter a number :"))
for i in range(1,n+1):
    fact = fact * i
print("Factorial of the given number = ")
print(fact)