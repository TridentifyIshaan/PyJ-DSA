'''
> Date Created: 15/09/2026
> Author: Ishaan Rastogi
> Purpose: To print first N natural numbers in opposite order using head recursion
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Using Head Recursion
def func(N):
    if N == 0:
        return
    print(N)
    func(N-1)
func(4)