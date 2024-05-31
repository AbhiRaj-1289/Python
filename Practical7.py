#Python code to print Fabonacci series upto n terms

n = int(input("Enter number of terms : "))
n1 = 0
n2 = 1
count = 0
print("Fabonacci series of "+str(n)+" terms : ")
while count < n:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1