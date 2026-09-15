'''
> Date Created: 15/09/2026
> Dates of Update: 
> Author: Ishaan Rastogi
> Purpose: To show recursion using parameters.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Using Tail Recursion as it is faster
def func(x,N):
    if N == 0:
        return
    func(x,N-1)
    print(x)
func(15,4)