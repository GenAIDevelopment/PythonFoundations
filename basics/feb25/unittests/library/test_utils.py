from utils import is_even,is_prime
import pytest

def test_is_even_basic():
    assert(is_even(4) == True)
    assert(is_even(3) == False)
    assert(is_even(0) == True)

def test_is_even_advanced():
    # test negative numbers
    assert(is_even(-4) == True)
    assert(is_even(-3) == False)

def test_is_even_negative():
    with pytest.raises(ValueError):
        is_even(4.0)

    with pytest.raises(ValueError):
        is_even("4")


def test_is_prime_positive():
    assert(is_prime(7) == True)
    assert(is_prime(9) == False)

def test_is_prime_negative():
    assert(is_prime(0) == False)
    assert(is_prime(-8) == False)

def test_is_prime_invalid_values():
    with pytest.raises(ValueError):
        is_prime("hello")
    with pytest.raises(ValueError):
        is_prime(7.0)
    
