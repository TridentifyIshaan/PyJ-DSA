'''
> Date Created: 15/08/2026
> Dates of Update: 
> Author: Ishaan Rastogi
> Purpose: To perform character hashing using get method (optimal code)
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def char_freq(s='', q=[]):
    s = "azyxyyzaaaa"
    q = ['d', 'a', 'y', 'x']
        
    hash_map ={}
    for char in s:
        hash_map[char] = hash_map.get(char,0) + 1

    result = []
    for char in q:
        result.append(hash_map.get(char,0))
    return result
print(char_freq())