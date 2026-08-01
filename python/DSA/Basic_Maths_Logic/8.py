'''
> Date Created: 01/08/2026
> Author: Ishaan Rastogi
> Purpose: To print all the factors of a number by optimal solution.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

from math import sqrt
def factorOf(num, result=[]):
    for i in range(1,int(sqrt(num))+1):
        if num%i == 0:
            result.append(i)
            if num//i != i:
                result.append(num//i)
    result.sort()
    return result
print(factorOf(120))