# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
size = len(names)
choice = random.randint(0, size-1)
person = names[choice]
print(f"{person} is going to buy the meal today!")
