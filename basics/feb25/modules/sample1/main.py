"""This module explains import of functions from other modules
"""
import utils

number = int(input("Enter the number of your choice "))
if utils.is_prime(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
