#!/usr/bin/python

def fib(n):

#
# A function to return the nth Fibonacci Number NOT using recursion
# -----------------------------------------------------------------
#
# PSEUDO-CODE:
# ============
#
# if n is less then 1 then return error
#
# if n is 1 or 2 then by convention, the answer is 1, so return 1
#
# otherwise
#
# Initialise variables to store the current & previous Finonnacci Numbers (F & F-1, say)
# At this point, the first two Numbers of the series are saved, both 1
#
# For Fibonacci Numbers from 3 ... to the number requested, Update the variables F & F-1
#
# return F

    if n < 1:      # fib is not defined for anything less than 1,
        return -1; # so return an Error Code if n < 1.

    if n <= 2:
        return  1; # The first 2 Fibonacci Numbers are 1.

    Current_Value = 1; Last_Value = 1; # Save the current and Previous Series Values.

    for fib_no in range(3, n + 1):     # For all values up to the target value,
        Saved_Value = Current_Value;               # Backup the Current Value. 
        Current_Value = Last_Value + Current_Value;# Compute new Current value.
        Last_Value = Saved_Value;                  # Original Current Value becomes Previous Value

    return Current_Value; # Return Current Value.

# TEST BED:
# =========

for fib_no in range(1, 25):
    print fib(fib_no);

