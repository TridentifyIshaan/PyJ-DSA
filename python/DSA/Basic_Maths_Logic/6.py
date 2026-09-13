'''
> Date Created: 01/08/2026
> Dates of Update: 13/09/2026
> Author: Ishaan Rastogi
> Purpose: To print all the factors of a number.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def factorOf(num, result=[]):
    for i in range(1,num+1):
        if num%i == 0: # if remainder is 0, that number is a factor
            result.append(i) # appending factors
    return result
print(factorOf(20))