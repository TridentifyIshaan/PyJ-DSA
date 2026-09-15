'''
> Date Created: 15/08/2026
> Dates of Update: 
> Author: Ishaan Rastogi
> Purpose: To count frequency of numbers of list 2, in list 1.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def count_freq(n=[], m=[]):
    n = [5,3,2,2,1,5,5,7,5,10] # list 1
    m = [10,111,1,9,5,67,2] # list 2
    
    result = []
    for i in m: # i is element in m
        count = 0
        for j in n: # j is element in n
            if j == i: # check is the element of m is in n
                count += 1 # increment frequency count
        result.append(count)
    return result
print(count_freq())