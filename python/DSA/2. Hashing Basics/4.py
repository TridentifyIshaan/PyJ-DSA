'''
> Date Created: 15/09/2026
> Dates of Update: 
> Author: Ishaan Rastogi
> Purpose: To count frequency of numbers of list 2, in list 1 using a hash list (better time complexity)
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def count_freq(n=[], m=[]):
    n = [5,3,2,2,1,5,5,7,5,10] # list 1
    m = [10,111,1,9,5,67,2] # list 2
        
    hash_list = [0] * (len(n)+1)

    for i in n: # i is element in n
        hash_list[i] += 1

    result = []
    for i in m: # i is element in m
        if i < 1 or i > len(n):
            result.append(0)
        else:
            result.append(hash_list[i])
    return result
print(count_freq())