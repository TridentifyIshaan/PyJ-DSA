'''
> Date Created: 31/07/2025
> Author: Ishaan Rastogi
> Purpose: To create a function to convert temperature from Fahrenheit to Celcius.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

f = int(input("Enter the temperature in Fahrenheit: "))  # User input for temperature in Fahrenheit
def fahrenheit_to_celcius(f):
    c = (f - 32) * 5 / 9  # Convert Fahrenheit to Celcius
    return c

c = fahrenheit_to_celcius(f)
print(f"The temperature in Celsius is: {round(c, 2)}") # Round the result to 2 decimal places

'''

Terminal - Ctrl + Shift + `
> python "path to the file"

'''