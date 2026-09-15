'''
> Date Created: 15/08/2026
> Dates of Update: 
> Author: Ishaan Rastogi
> Purpose: To count frequency of numbers of list 2, in list 1 using a dictionary (optimal code)
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def count_freq(n=[], m=[]):
    n = [5,3,2,2,1,5,5,7,5,10] # list 1
    m = [10,111,1,9,5,67,2] # list 2
        
    hash_map = {}

    for i in n: # i is element in n
        hash_map[i] = hash_map.get(i, 0) + 1

    result = []
    for i in m: # i is element in m
        result.append(hash_map.get(i, 0))
    return result
print(count_freq())