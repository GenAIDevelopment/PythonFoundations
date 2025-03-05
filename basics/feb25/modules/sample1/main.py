"""This module explains import of functions from other modules
"""
from utils import is_prime

number = int(input("Enter the number of your choice "))
if is_prime(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
