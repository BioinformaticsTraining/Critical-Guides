#!/usr/bin/python

def fib(n):

#
# A function to print out the first n Fibonacci Numbers
# -----------------------------------------------------
#
# On Failure return FALSE
# If sucessful, returns TRUE
#
# PSEUDO-CODE:
# ============
#
# if n is less than 1 then return error
#
# Initialise variables to store the current & previous Finonnacci Numbers (F & F-1, say)
# At this point, the first two Numbers of the series are saved, both 1 by convention
#
# For Fibonacci Numbers from 1 ... to the number requested,
#
#     if current_term is less than 3 then by convention, the answer is 1
#         so print 1 and continue to investigate next term
#
#     if current_term is 3 or more
#         Update the variables F & F-1 and then print F
#
# return Success
# 

    if n < 1:         # fib is not defined for anything less than 1,
        return False; # so return an Error Code if n < 1.

    Current_Value = 1; Last_Value = 1; # Initialise variable to hold the last 2 terms
                                       # These are needed to caculate term 3 and beyond
                                       # The first 2 term are both 1 by convention

    for fib_no in range(1, n + 1):     # Compute and [rint all terms from 1 to n

        if fib_no < 3:                 # The first 2 term are both 1 by convention
            print 1; continue;         # Print them and move on to the next term

        Saved_Value = Current_Value;               # Backup the Current Value. 
        Current_Value = Last_Value + Current_Value;# Compute new Current value.
        Last_Value = Saved_Value;                  # Original Current Value becomes Previous Value

        print Current_Value; # print Current Value.

    return True;

# TEST BED:
# =========

fib(24);

