def is_even(number: int) -> bool:
    """_summary_

    Args:
        number (int): _description_

    Returns:
        bool: _description_
    """
    if isinstance(number, int):
        return number%2 == 0
    raise ValueError(f"{number} is not integer")