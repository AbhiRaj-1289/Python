import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors "))
if choice >= 3 or choice < 0:
    print("You entered an invalid input! You lose!")
else:
    print("You choose = ",choice)
    print(images[choice])
    computer_choice = random.randint(0,2)

    print("Computer choose = ",computer_choice)
    print(images[computer_choice])
    if choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice > choice:
        print("You lose")
    elif choice == 2 and computer_choice == 0:
        print("You lose")
    elif choice > computer_choice:
        print("You win")
