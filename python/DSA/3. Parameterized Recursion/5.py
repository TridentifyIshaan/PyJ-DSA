'''
> Date Created: 15/09/2026
> Dates of Update: 
> Author: Ishaan Rastogi
> Purpose: To print first N natural numbers using head recursion
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Head Recursion
def func(i,N):
    if i > N:
        return
    print(i)
    func(i+1,N)
func(1,4)