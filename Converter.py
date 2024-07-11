#Python code to convert various measurnments.

print("Press '1' to convert units of lengths.")
print("Press '2' to convert units of temperature.")
print("Press '3' to convert units of liquid.")

choice = int(input("Enter Your choice : "))

if choice == 1:
    print("Select your Conversion Type : ")
    print("Press 1 to convert cm to inch.")
    print("Press 2 to convert inch to cm.")
    print("Press 3 to convert cm to feet.")
    print("Press 4 to convert feet to cm.")
    print("Press 5 to convert inch to feet.")
    print("Press 6 to convert feet to inch.")

    input_value = int(input("Enter your choice : "))

    if input_value == 1:
        cm = float(input("Enter value in cm : "))
        inch = cm * 0.393701
        round(inch,3)
        print("The value in inch is : ", inch)

    elif input_value == 2:
        inch = float(input("Enter value in inch : "))
        cm = inch * 2.54
        print("The value in cm is : ", cm)
    
    elif input_value == 3:
        cm = float(input("Enter value in cm : "))
        feet = cm * 0.0328084
        round(feet,3)
        print("The value in feet is : ", feet)
    
    elif input_value == 4:
        feet = float(input("Enter value in feet : "))
        cm = feet * 30.48
        print("The value in cm is : ", cm)
    
    elif input_value == 5:
        inch = float(input("Enter value in inch : "))
        feet = inch * 0.0833333
        round(feet,3)
        print("The value in feet is : ", feet)
    
    elif input_value == 6:
        feet = float(input("Enter value in feet : "))
        inch = feet * 12
        print("The value in inch is : ", inch)
    else:
        print("Invalid Input")

elif choice == 2:
    print("Select your Conversion Type : ")
    print("Press 1 to convert Fahrenheit to Celsius.")
    print("Press 2 to convert Celsius to Fahrenheit.")

    input_choice = int(input("Enter Your Choice : "))

    if input_choice == 1:
        fahrenheit = float(input("Enter value in Fahrenheit : "))
        celsius = (fahrenheit - 32) * 5 / 9
        print("The value in Celsius is : ", celsius)
    
    elif input_choice == 2:
        celsius = float(input("Enter value in Celsius : "))
        fahrenheit = celsius * 9 / 5 + 32
        print("The value of Fahrenheit is : ", fahrenheit)
    else:
        print("Invalid Input")

elif choice == 3:
    print("Select your Conversion Type : ")
    print("Press 1 to convert Milliliters to Litres.")
    print("Press 2 to convert Litres to Milliliters.")
    print("Press 3 to convert Litres to Gallons.")
    print("Press 4 to convert Gallons to Litres.")

    input_number = int(input("Enter Your Choice : "))

    if input_number == 1:
        ml = float(input("Enter value in Milliliters : "))
        litres = ml / 1000
        print("The value in Litres is : ", litres)
    
    elif input_number == 2:
        litres = float(input("Enter value in Litres : "))
        ml = litres * 1000
        print("The value in Millilitres is : ", ml)
    
    elif input_number == 3:
        litres = float(input("Enter value in Litres : "))
        gallons = litres * 0.264172
        round(gallons,2)
        print("The value in Gallons is : ", gallons)
    
    elif input_number == 4:
        gallons = float(input("Enter value in Gallons : "))
        litres = (gallons / 0.264172)
        round(litres,2)
        print("The value in Litres is : ", litres)
    else:
        print("Invalid Input")

else:
    print("Invalid Input")