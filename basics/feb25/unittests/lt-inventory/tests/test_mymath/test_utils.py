from mymath.utils import is_prime, factorial
import pytest

def test_is_prime_basic():
    """This test case will validate basic prime functionality
    """
    assert is_prime(7) == True
    assert is_prime(9) == False

def test_is_prime_border():
    """This test case will validate boundary conditions
    """
    assert is_prime(1) == False
    assert is_prime(0) == False


def test_is_prime_invalid():
    """This testcase will validate invalid cases
    """
    with pytest.raises(ValueError):
        is_prime("hello")
    with pytest.raises(ValueError):
        is_prime(7.5)


def test_factorial_basic():
    assert factorial(5) == 120, "Value Comparision failed"
    assert factorial(0) == 1, "Value Comparision failed"


def test_factorial_invalid():
    with pytest.raises(ValueError):
        factorial(-1)
    
    with pytest.raises(ValueError):
        factorial("1")

