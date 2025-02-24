"""
This is a sample program to learn debugging
"""

def is_factor(number, index):
    """This number checks if the index is a factor of number

    Args:
        number (int): number
        index (int): index

    Returns:
        bool: True if factor, false otherwise
    """
    return number % index == 0


def is_prime(number):
    """This function checks if the number is prime

    Args:
        number (int): number

    Returns:
        bool: True if prime, false otherwise
    """
    for index in range(2, number):
        if is_factor(number, index):
            return False
    return True

def main():
    """This is the main function
    """
    for number in range(1, 20):
        if is_prime(number):
            print(f"{number} is prime")
        else:
            print(f"{number} is not prime")

if __name__ == "__main__":
    print("Running the program")
    main()
    print("Program terminated")

