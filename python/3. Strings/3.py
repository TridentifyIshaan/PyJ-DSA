'''
> Date Created: 11/07/2025
> Author: Ishaan Rastogi
> Purpose: To fill in a letter template given below with name and date.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

letter = '''
            Dear <|Name|>,
            You are selected!
            <|Date|>
        '''

name = input("Enter your name: ")
date = input("Enter the date:")
print(letter.replace("<|Name|>", name).replace("<|Date|>", date))