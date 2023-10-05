#Calculator
from CalcArt import logo

#Add
def add(n1,n2):
    return n1 + n2

#Subtract
def sub(n1,n2):
    return n1 - n2

#Multiply
def multiply(n1,n2):
    return n1 * n2

#divide
def div(n1,n2):
    return n1 / n2

#Operation Dictionary
operation = {
             "+": add,
             "-": sub,
             "*": multiply, 
             "/": div
             }
print(logo)

def calculator():
    num1 = float(input("Enter first number : "))
    for symbol in operation:
        print(symbol)
    if_continue = True

    while if_continue:
        operation_symbol = input("Pick any operation : ")
        num2 = float(input("Enter next  number : "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            if_continue = False
            calculator()

calculator()