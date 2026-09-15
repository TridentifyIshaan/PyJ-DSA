'''
> Date Created: 15/09/2026
> Dates of Update: 
> Author: Ishaan Rastogi
> Purpose: To find factorial of a number
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def fact(N):
    if N == 0 or N == 1:
        return 1
    return N * fact(N-1)
print(fact(5))