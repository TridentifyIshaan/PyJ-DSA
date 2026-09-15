'''
> Date Created: 15/09/2026
> Dates of Update: 
> Author: Ishaan Rastogi
> Purpose: To find sum of first N natural numbers
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Using Tail Recursion as it is faster
def func(sum, i, N):
    if i > N:
        print(sum)
        return
    func(sum+i, i+1, N) # Adding that element and incrementing the counter
func(0, 1, 10)