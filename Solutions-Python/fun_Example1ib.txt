###########################################################################################
### The issue here is that, if ALL the Arguments are Integers,
### AvergeN will perform Integer arithmetic by default.
### 
### So, ((1 + 2 + 4) / 3) is 2
### As Integer division always rounds down to the nearest INTEGER value.
### 
### If just ONE of the Arguments is a float, AvergeN performs Floating Point arithmetic.
###
### So, ((1.0 + 2 + 4) / 3) is 2.333333...
###
### If you want AverageN to ALWAYS use Floating Point arithmetic, you must ensure that it
### never the case that ALL Arguments are INTEGER.
###
### This can be acheive by casting all arguments to float as they are added up.
### If they were floats already ... no harm done.
### All the ints will be massaged into floats and so integer arithmetic will
### never be appropriate.
###
### Alternatively (and more simply), I could just force the Total Variable to be a float
### by initialising it as a float (Total = 0.0)
###
### Only one, or the other, of these amendment is required.
###
### I have made both here. The "Belt and Braces" approach.
###
### Try removing each in turn to prove both are, alone, sufficient solutions.
###
###########################################################################################

def AverageN (*Numbers): # Using a Variable number of Parameters

    Total = 0.0; # Initialise Variable to store the Sum of all Arguments.

    for Number in Numbers: # For each Argument,
        Total += float(Number);   # increment the Total.

    return (Total / len(Numbers)); # Return the Average.

#TEST BED 
#======== 

print str(AverageN(1 , 2, 4));                # 3 Integers 
print str(AverageN(0.1 , 2.95, 7));           # 3 Mix float/Integer
print str(AverageN(1 , 2.6));                 # 2 Numbers 
print str(AverageN(1 , 13.2, 9.2, 4, 6, 10)); # 6 Numbers 
print str(AverageN(2.9999));                  # 1 Number 

