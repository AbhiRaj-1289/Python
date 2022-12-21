y = int(input("Enter Year : "))
if (y % 400 == 0) and (y % 100 == 0):
    print(str(y)+" is a leap year")
elif (y % 4 == 0) and (y % 100 != 0):
    print(str(y)+" is a leap year")
else:
    print(str(y)+" is not a leap year")