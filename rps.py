import random

options = ["rock", "paper", "scissors"]

def func(choice):
    cpuChoice = random.choice(options)
    print("Cpu chose:", cpuChoice)


    #2 for draw, 1 for lost, 0 for win
    if choice == 0:
        if cpuChoice == options[choice]:
            return 2
        elif cpuChoice == options[1]:
            return 1
        elif cpuChoice == options[2]:
            return 0

    if choice == 1:
        if cpuChoice == options[choice]:
            return 2
        elif cpuChoice == options[2]:
            return 1
        elif cpuChoice == options[0]:
            return 0

    if choice == 2:
        if cpuChoice == options[choice]:
            return 2
        elif cpuChoice == options[0]:
            return 1
        elif cpuChoice == options[1]:
            return 0

while (True):
    print("1.rock 2.paper 3.scissors")
    x = int(input("What is your Choice: "))
    print("\nYou chose:", options[x - 1])
    result = func(x - 1)
    
    if result == 0:
        print("You won!\n")
    elif result == 1:
        print("You lost!\n")
    elif result == 2:
        print("Draw!\n")

    
        


