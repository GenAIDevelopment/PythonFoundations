"""A one-line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:

  foo = ClassFoo()
  bar = foo.function_bar()
"""

import math

def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers"""
    return a + b


def sub(a: int | float, b: int | float) -> int | float:
    """Subtract two numbers"""
    return a - b


def mul(a: int | float, b: int | float) -> int | float:
    """Multiply two numbers"""
    return a * b


def div(a: int | float, b: int | float) -> float:
    """Divide two numbers (true division)"""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def floordiv(a: int | float, b: int | float) -> int | float:
    """Floor division of two numbers"""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a // b


def mod(a: int | float, b: int | float) -> int | float:
    """Modulus of two numbers"""
    if b == 0:
        raise ValueError("Modulo by zero is not allowed.")
    return a % b


def power(a: int | float, b: int | float) -> int | float:
    """Raise a to the power of b"""
    return a ** b


def square(a: int | float) -> int | float:
    """Return the square of a number"""
    return a * a


def cube(a: int | float) -> int | float:
    """Return the cube of a number"""
    return a * a * a


def sqrt(a: int | float) -> float:
    """Return the square root of a number"""
    if a < 0:
        raise ValueError("Square root of negative number is not defined.")
    return a ** 0.5


def abs_val(a: int | float) -> int | float:
    """Return the absolute value of a number"""
    return abs(a)


def mean(a: int | float, b: int | float) -> float:
    """Return the arithmetic mean of two numbers"""
    return (a + b) / 2


# -------------------------------
# Additional 20 functions
# -------------------------------

def factorial(n: int) -> int:
    """Return factorial of a number"""
    if n < 0:
        raise ValueError("Factorial of negative number not defined.")
    return math.factorial(n)


def gcd(a: int, b: int) -> int:
    """Return greatest common divisor"""
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    """Return least common multiple"""
    return abs(a * b) // math.gcd(a, b) if a and b else 0


def is_even(n: int) -> bool:
    """Check if a number is even"""
    return n % 2 == 0


def is_odd(n: int) -> bool:
    """Check if a number is odd"""
    return n % 2 != 0


def percent(a: int | float, b: int | float) -> float:
    """Return percentage (a is what percent of b)"""
    if b == 0:
        raise ValueError("Cannot calculate percentage with denominator 0.")
    return (a / b) * 100


def average(numbers: list[int | float]) -> float:
    """Return the average of a list of numbers"""
    if not numbers:
        raise ValueError("Empty list provided.")
    return sum(numbers) / len(numbers)


def variance(numbers: list[int | float]) -> float:
    """Return variance of a list of numbers"""
    m = average(numbers)
    return sum((x - m) ** 2 for x in numbers) / len(numbers)


def stddev(numbers: list[int | float]) -> float:
    """Return standard deviation of a list of numbers"""
    return math.sqrt(variance(numbers))


def harmonic_mean(numbers: list[int | float]) -> float:
    """Return harmonic mean of a list of numbers"""
    if not numbers or 0 in numbers:
        raise ValueError("Harmonic mean not defined for empty list or zero values.")
    return len(numbers) / sum(1 / x for x in numbers)


def geometric_mean(numbers: list[int | float]) -> float:
    """Return geometric mean of a list of numbers"""
    if not numbers:
        raise ValueError("Empty list provided.")
    product = 1
    for x in numbers:
        product *= x
    return product ** (1 / len(numbers))


def log(a: int | float, base: int | float = math.e) -> float:
    """Return logarithm of a number with given base"""
    if a <= 0:
        raise ValueError("Logarithm only defined for positive numbers.")
    return math.log(a, base)


def exp(a: int | float) -> float:
    """Return exponential of a number (e^a)"""
    return math.exp(a)


def deg_to_rad(deg: float) -> float:
    """Convert degrees to radians"""
    return math.radians(deg)


def rad_to_deg(rad: float) -> float:
    """Convert radians to degrees"""
    return math.degrees(rad)


def sin_deg(deg: float) -> float:
    """Return sine of angle in degrees"""
    return math.sin(math.radians(deg))


def cos_deg(deg: float) -> float:
    """Return cosine of angle in degrees"""
    return math.cos(math.radians(deg))


def tan_deg(deg: float) -> float:
    """Return tangent of angle in degrees"""
    return math.tan(math.radians(deg))


def nCr(n: int, r: int) -> int:
    """Return n choose r (combinations)"""
    if r > n or n < 0 or r < 0:
        raise ValueError("Invalid values for nCr.")
    return math.comb(n, r)


def nPr(n: int, r: int) -> int:
    """Return n permute r (permutations)"""
    if r > n or n < 0 or r < 0:
        raise ValueError("Invalid values for nPr.")
    return math.perm(n, r)
