# calling a factorial and is prime
from utilties.math.basic import is_prime
from utilties.math.advanced import factorial

if __name__ == '__main__':
    number = int(input("Enter the number "))
    print(is_prime(number))
    print(factorial(number))