'''
> Date Created: 15/08/2026
> Dates of Update: 
> Author: Ishaan Rastogi
> Purpose: To count frequency of a number in a list.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def count_freq(num, key=1):
    freq_map = {} # initialized an empty dictionary, to store frequency of each number
    
    # Appending the frequency one by one as we parse through the array
    for i in range(0,len(num)):
        if num[i] in freq_map:
            freq_map[num[i]] += 1
        else:
            freq_map[num[i]] = 1 # introducing frequency of a new number to be incremented later on
    
    #Returning the frequency of the key
    return freq_map[key]
print(count_freq([0,2,1,0,1,0,5,1]))