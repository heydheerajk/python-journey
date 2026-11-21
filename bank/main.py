
import os
import bank

def look(a="=", b=40):
    print(a * b)


class BankInfo:

    def __init__(self):
        self.name()
        self.description()
        self.tagline()

    def name(self):
        look()
        print("WELCOME TO THE SOFTECH BANK")
        look()

    def tagline(self):
        print("24*7 Banking Facility")
        print("Fully Digital Services")

    def description(self):
        print("WELCOME TO INDIA'S FIRST DIGITAL BANK")
        


bank = BankInfo()
