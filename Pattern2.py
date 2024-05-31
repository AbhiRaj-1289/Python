#Python code to print Pyramid pattern

x = int(input("Enter No. Of Rows : "))
k = x-1
for i in range(0,x):
    for j in range(0,k):
        print(end=" ")
    k = k-1
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")