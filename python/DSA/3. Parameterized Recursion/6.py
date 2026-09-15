'''
> Date Created: 15/09/2026
> Author: Ishaan Rastogi
> Purpose: To print first N natural numbers using tail recursion
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Using Tail Recursion as it is faster
def func(N):
    if N == 0:
        return
    func(N-1)
    print(N)
func(4)