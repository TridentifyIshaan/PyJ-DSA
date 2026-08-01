'''
> Date Created: 01/08/2026
> Author: Ishaan Rastogi
> Purpose: To print all the factors of a number.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def factorOf(num, result=[]):
    for i in range(1,num+1):
        if num%i == 0:
            result.append(i)
    return result
print(factorOf(20))