def is_prime(number: int) -> bool:
    """This method checks if the number is prime or not

    Args:
        number (int): number

    Returns:
        bool: True if Prime false other wise

    Raises:
       ValueError: if the number is not of integer type
    """
    if not isinstance(number, int):
        raise ValueError(f"{number} is not a valid integer")
    result = True
    if number <= 1:
        result = False
    for index in range(2,number):
        if number % index == 0:
            result = False
            break
    return result


def factorial(number: int) -> int:
    """_summary_

    Args:
        number (int): _description_

    Returns:
        int: _description_
    
    Raises:
      ValueError: For all invalid entries
    """
    if not isinstance(number, int):
        raise ValueError(f"{number} is not valid integer, So factorial cannot be calcuated")
    if number < 0:
        raise ValueError(f"{number} is not negative integer, So factorial cannot be calcuated")

    result = 1
    for index in range(1,number+1):
        result = result * index
    return result