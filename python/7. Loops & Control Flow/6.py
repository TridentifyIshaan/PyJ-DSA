'''
> Date Created: 20/07/2025
> Author: Ishaan Rastogi
> Purpose: To check whether a number is prime or not
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Prime numbers are numbers greater than 1 that have no divisors other than 1 and themselves.

n = int(input("Enter a number to check if it is prime: "))

for i in range(2, n):
    if (n % i) == 0:
        print(f"{n} is not a prime number.")
        break
else:
    print(f"{n} is a prime number.")