choice = input("Do you want to accelerate or decelerate: ").lower()

initial_speed = 10
final_speed = initial_speed

def accelerate(speed):
    while True:
        case = input("Enter 'stop' to stop accelerating or press Enter to continue: ").lower()
        if case == "stop":
            print(f"Your final speed = {speed}")
            break
        else:
            speed += 15
            print("Your speed =", speed)
    return speed

def decelerate(speed):
    while True:
        case = input("Enter 'stop' to stop decelerating or press Enter to continue: ").lower()
        if case == "stop":
            print(f"Your final speed = {final_speed}KM/Hr")
            break
        else:
            if speed <= 0:
                print("Further deceleration not possible")
                break
            speed -= 10
            print(f"Your speed = {speed} KM/Hr")
    return speed

if choice == "accelerate":
    final_speed = accelerate(final_speed)
    choice = input("Do you want to decelerate now? (yes/no): ").lower()
    if choice == "yes":
        final_speed = decelerate(final_speed)
    else:
        print(f"Your final speed = {final_speed} KM/Hr")
elif choice == "decelerate":
    final_speed = decelerate(final_speed)

else:
    print("Invalid choice")
