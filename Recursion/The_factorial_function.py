#The factorial of a positive integer n, denoted n!, is defined as the product of the integers from 1 to n
#If n = 0, then n! is defined as 1 by convention.

"""
    |1     if n = 0
n!  <
    |n(n - 1)(n - 2)...(3)(2)(1) if n >= 1
"""

#For example: 5! = 5 * 4 * 3 * 2 * 1 = 120

#A RECURSIVE IMPLEMENTATION OF THE FACTORIAL FUNCTION

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)#This is the recursive call
    
#This function does not use any loops. Repetition is provided by
#repeated recursive invocations of the function.

"""
we to see how the function works.

factorial(4) return 4 * 6 = 24
factorial(3) return 3 * 2 = 6
factorial(2) return 2 * 1 = 2
factorial(1) return 1 * 1 = 1
factorial(0) return 1


"""

