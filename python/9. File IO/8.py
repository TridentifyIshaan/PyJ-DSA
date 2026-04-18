'''
> Date Created: 31/07/2025
> Author: Ishaan Rastogi
> Purpose: The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

import random
def game():
    print("Welcome to the game..")
    score = random.randint(0, 100)
    print(f"Your score is {score}")
    
    # Read Hi-score from a file
    with open(r'Code With Harry\9. File IO\Hi-score.txt', 'r') as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore) # converting string to integer
        else:
            hiscore = 0

    # Write Hi-score to a file
    if score > hiscore:
        # Update the Hi-score
        with open(r'Code With Harry\9. File IO\Hi-score.txt', 'w') as f:
            f.write(str(score))

    return score

game()

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''
