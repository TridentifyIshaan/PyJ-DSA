'''
> Date Created: 31/07/2025
> Author: Ishaan Rastogi
> Purpose: To create a game of Snake, Water, Gun with reduced codelines
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# First setting variables
'''
snake = 1
water = -1
gun = 0
'''

import random
computer = random.randint(-1, 1) # random number between -1 and 1

you = input("Enter your choice: \n1. s for Snake \n2. w for Water \n3. g for Gun \n")

youDict = {"s": 1, "w": -1, "g": 0}
answer = youDict[you]

reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
print(f"You chose: {reverseDict[answer]} and computer chose: {reverseDict[computer]}")

if computer == answer:
    print("Draw! Both chose the same thing")
else:

    # We formed a pattern here by taking difference of user choice and computer choice
    # When difference is -1 or 2, user lose.

    if (computer - answer) == -1 or (computer - answer) == 2:
        print("You lose!")
    else:
        print("You win!")
'''

Terminal - Ctrl + Shift + `
> python "path to the file"

'''