#Python code to Find factors of a given number

n = int(input("Enter a number :"))
print("The Factors of "+str(n)+" are : ")
for i in range(1,n+1):
    if (n % i == 0):
        print(i)