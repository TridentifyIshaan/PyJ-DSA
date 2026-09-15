'''
> Date Created: 15/09/2026
> Author: Ishaan Rastogi
> Purpose: To print first N natural numbers in opposite order using tail recursion
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Using Tail Recursion as it is faster
def func(i,N):
    if i > N:
        return
    func(i+1,N)
    print(i)
func(1,4)