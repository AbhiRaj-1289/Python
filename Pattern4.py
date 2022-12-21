x = int(input("Enter No. Of Rows : "))
k = 0
for i in range(1,x+1):
    for j in range(1,(x-i)+1):
        print(end=" ")
    while k != (2*i-1):
        print("*",end="")
        k += 1
    k = 0
    print("\r")