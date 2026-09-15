'''
> Date Created: 15/09/2026
> Author: Ishaan Rastogi
> Purpose: To show head recursion
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Head recursion - when recursive call is made before the recursive function statement

def func(count):
    if count == 4:
        return
    print('Anirudh')
    count += 1
    func(count) # HERE
func(0)