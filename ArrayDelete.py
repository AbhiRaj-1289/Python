size = int(input("Enter Size of list: "))
ar = []

for i in range(size):
    element = input(f"Enter element {i + 1}: ")
    ar.append(element)

for element in ar:
    print(element)
