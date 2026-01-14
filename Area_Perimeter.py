print("Enter 1 to find Perimeter.")
print("Enter 2 to find Area.")

choice = int(input("Enter Your Choice: "))

if choice == 1:
    print("Press 1 to find Perimeter of Rectangle.")
    print("Press 2 to find Perimeter of Square.")
    print("Press 3 to find Perimeter of Triangle.")
    print("Press 4 to find Perimeter of Circle.")

    choose = int(input("Enter Your Choice: "))

    if choose == 1:
        length = int(input("Enter Length Of Rectangle: "))
        breadth = int(input("Enter Breadth Of Rectangle: "))
        perimeter = 2 * (length + breadth)
        print("Perimeter Of Rectangle Is:", perimeter)
    elif choose == 2:
        side = int(input("Enter Side Of Square: "))
        perimeter = side * 4
        print("Perimeter of Square:", perimeter)
    elif choose == 3:
            side1 = int(input("Enter The First Side of Triangle: "))
            side2 = int(input("Enter The Second Side of Triangle: "))
            side3 = int(input("Enter The Third Side of Triangle: "))
            perimeter = side1 + side2 + side3
            print("Perimeter of Triangle is:", perimeter," unit")
    elif choose == 4:
        radius = int(input("Enter The Radius Of Circle: "))
        perimeter = 2 * 3.14 * radius
        print("Perimeter of Circle is:", perimeter," unit")
    else:
        print("Invalid Input")

elif choice == 2:
    print("Press 1 to find Area Of Rectangle.")
    print("Press 2 to find Area Of Square.")
    print("Press 3 to find Area Of Circle.")
    
    choose = int(input("Enter Your Choice: "))

    if choose == 1:
        length = int(input("Enter Length of Rectangle: "))
        breadth = int(input("Enter Breadth of Rectangle: "))
        area = length * breadth
        print("Area of Rectangle is:", area,"sq. units")
    elif choose == 2:
        side = int(input("Enter Side of Square: "))
        area = side * side
        print("Area of Square is:", area,"sq. units")
    elif choose == 3:
        radius = int(input("Enter The Radius Of Circle: "))
        area = 3.14 * radius * radius
        print("Area of Circle is:", area,"sq. units")
    else:
        print("Invalid Input")

else:
    print("Invalid Input")
