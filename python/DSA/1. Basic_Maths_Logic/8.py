'''
> Date Created: 01/08/2026
> Author: Ishaan Rastogi
> Purpose: To print all the factors of a number by optimal solution.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

from math import sqrt
def factorOf(num, result=[]):
    # range is square rooted because factors always come in pairs, so they repeat
    for i in range(1,int(sqrt(num))+1): 
        if num%i == 0:
            result.append(i) # appending factors coming in range of square root
            # checking if the pair is not same (so that factors are not repeated)
            if num//i != i:
                # appending the factors that don't come in range of square root
                result.append(num//i)
    result.sort() # sorting the factors - optional
    return result
print(factorOf(120))