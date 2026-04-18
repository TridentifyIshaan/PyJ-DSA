'''
> Date Created: 14/08/2025
> Author: Ishaan Rastogi
> Purpose: Write a Class 'Train' which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

from random import randint

class Train:

    def __init__(self, trainNo, starting, destination, seats=1000):
        self.trainNo = trainNo
        self.starting = starting
        self.destination = destination
        self.seats = seats

    def book(self):
        print(f"Ticket booked for Train No: {self.trainNo} from {self.starting} to {self.destination}")

    def status(self):
        print(f"Train No: {self.trainNo} is running on time with {self.seats} seats available.")

    def fare(self):
        print(f"Ticket fare for Train No: {self.trainNo} from {self.starting} to {self.destination} is {randint(1000, 5000)} INR.")

T1 = Train(12399, "Delhi", "Mumbai")
T1.book()
T1.status()
T1.fare()

T2 = Train(12400, "Delhi", "Kolkata")
T2.book()
T2.status()
T2.fare()

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''