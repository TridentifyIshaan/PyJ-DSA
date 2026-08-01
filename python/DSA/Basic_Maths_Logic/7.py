'''
> Date Created: 01/08/2026
> Author: Ishaan Rastogi
> Purpose: To print all the factors of a number by better solution.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def factorOf(num, result=[]):
    for i in range(1,num//2):
        if num%i == 0:
            result.append(i)
    result.append(num)
    return result
print(factorOf(120))