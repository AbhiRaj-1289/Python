#Calculator

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

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))


for symbol in operation:
    print(symbol)
    
operation_symbol = input("Pick any operation from above : ")

calculation_function = operation[operation_symbol]
first_answer = calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick any operation from above : ")
num3 = int(input("Enter next number : "))
calculation_function = operation[operation_symbol]
second_answer = calculation_function(first_answer,num3)
print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

