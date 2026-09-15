'''
> Date Created: 15/09/2026
> Dates of Update: 
> Author: Ishaan Rastogi
> Purpose: To show tail recursion
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Tail recursion - when recursive call is made at the end of the recursive function statement

def func(count):
    if count == 4:
        return
    count += 1
    func(count) # HERE
    print('Anirudh')
func(0)