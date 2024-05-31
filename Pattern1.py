#python code to print right triangle pattern

x = int(input("Enter No. Of Rows : "))
for i in range(0,x):
    for j in range(0,i+1):
        print("*",end= "")
    print("\r")