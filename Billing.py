print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if(size == "S"):
    bill = 15
    if(add_pepperoni == "Y" or add_pepperoni == "y"):
        bill += 2
    if(extra_cheese == "Y" or extra_cheese == "y"):
        bill += 1
    print(f"Your final bill is: ${bill}")

if(size == "M"):
    bill = 20
    if(add_pepperoni == "Y" or add_pepperoni == "y"):
        bill += 3
    if(extra_cheese == "Y" or extra_cheese == "y"):
        bill += 1
    print(f"Your final bill is: ${bill}")

if(size == "L"):
    bill = 25
    if(add_pepperoni == "Y" or add_pepperoni == "y"):
        bill += 4
    if(extra_cheese == "Y" or extra_cheese == "y"):
        bill += 1
    print(f"Your final bill is: ${bill}")