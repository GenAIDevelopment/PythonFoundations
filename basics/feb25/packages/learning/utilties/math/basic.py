"""This module consists of reusable functions

List of Functions

* is_prime
* is_factor
"""

def is_prime(number):
    """This function check if the number is prime or not

    Args:
        number (int): number to be checked

    Returns:
        bool: True if prime false otherwise
    """
    result = True
    for index in range(2,number):
        if number % index == 0:
            result = False
            break
    return result

def is_factor(number, index):
    """This function checks if index is factor of number

    Args:
        number (_type_): _description_
        index (_type_): _description_

    Returns:
        _type_: _description_
    """
    return number % index == 0