def is_even(number: int) -> bool:
    """_summary_

    Args:
        number (int): _description_

    Returns:
        bool: _description_
    """
    raise_error_if_not_int(number)
    return number%2 == 0

def raise_error_if_not_int(number):
    if not isinstance(number, int):
        raise ValueError(f"{number} is not integer")

def is_prime(number: int) -> bool:
    raise_error_if_not_int(number)
    result = True
    if number < 1:
        result = False
    for index in range(2,number):
        if number % index == 0:
            result = False
            break
    return result
# come up with unit tests




