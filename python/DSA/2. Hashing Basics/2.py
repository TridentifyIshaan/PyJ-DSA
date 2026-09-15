'''
> Date Created: 15/09/2026
> Dates of Update: 
> Author: Ishaan Rastogi
> Purpose: To count frequency of a number in a list using get function.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def count_freq(num, key=1):
    hash_map = {} # initialized an empty dictionary, to store frequency of each number
    
    # Appending the frequency one by one as we parse through the array
    for i in range(0,len(num)):
        # If the number is already present in the hashmap, we increment its frequency
        # If the number is not present in the hashmap, we add it to the hashmap with a frequency of 1
        hash_map[num[i]] = hash_map.get(num[i], 0) + 1
        
    #Returning the frequency of the key
    return hash_map[key]
print(count_freq([0,2,1,0,1,0,5,1]))