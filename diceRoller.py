from random import randint
while True:
    roll = []
    user_input = input(f"How many dice would you like to roll? ")

    if user_input == "exit":
        print("Thank you for playing")
        break
    else: 
        for i in range(int(user_input)):
            roll.append(randint(1,6))
        print(*roll,sep=", ")