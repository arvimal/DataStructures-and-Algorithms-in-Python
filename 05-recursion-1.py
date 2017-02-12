#!/usr/bin/env python3

# Recursion
# Example 1

def factorial(n):
    # type: (int) -> int
    """Find the factorial of a number"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print('\nFactorial of {0} is {1}'.format(2, factorial(2)))
print('Factorial of {0} is {1}'.format(3, factorial(3)))
print('Factorial of {0} is {1}'.format(4, factorial(4)))
print('Factorial of {0} is {1}'.format(5, factorial(5)))
print('Factorial of {0} is {1}'.format(6, factorial(6)))
print('Factorial of {0} is {1}'.format(7, factorial(7)))
print('Factorial of {0} is {1}'.format(8, factorial(8)))
print('Factorial of {0} is {1}'.format(9, factorial(9)))
print('Factorial of {0} is {1}'.format(10, factorial(10)))
