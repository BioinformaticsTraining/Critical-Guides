#!/usr/bin/python

def fib(n):

#
# A function to return the nth Fibonacci Number using recursion
# -------------------------------------------------------------
#
# PSEUDO-CODE:
# ============
#
# if n is less then 1 then return error
#
# if n is 1 or 2 then by convention, the answer is 1, so return 1
#
# otherwise return the sum of the previous 2 fibonacci numbers
#

    if n < 1:      # fib is not defined for anything less than 1,
        return -1; # so return an Error Code

    if n <= 2:
        return  1; # The first 2 Fibonacci Numbers are 1
    else:
        return fib(n-1) + fib(n-2)
                   # Otherwise Return the sum of the
                   # previous 2 Fibonacci Numbers
# TEST BED:
# =========

for fib_no in range(1, 25):
    print fib(fib_no);

