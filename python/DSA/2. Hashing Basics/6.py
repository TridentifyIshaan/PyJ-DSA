'''
> Date Created: 15/08/2026
> Dates of Update: 
> Author: Ishaan Rastogi
> Purpose: To perform character hashing
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def char_freq(s='', q=[]):
    s = "azyxyyzaaaa"
    q = ['d', 'a', 'y', 'x']
        
    hash_list = [0] * 26 # ascii values range from 97 to 122
    
    for char in s:
        ascii = ord(char) # to find ascii value of character
        i = ascii - 97 # to index characters from 0 to 26
        hash_list[i] += 1

    result = []
    for char in q:
        ascii = ord(char)
        i = ascii - 97
        result.append(hash_list[i])
    return result
print(char_freq())