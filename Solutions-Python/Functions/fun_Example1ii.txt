###########################################################################################
### Only one change is required to the Function Code.
### Remove the "*" in front of Numbers.
### The Number of Arguments expected is no longer variable.
### Just ONE List (of arbitrary length) is expected.
### 
### The TEST BED Code must be amended to send List Arguments, of course.
###
###########################################################################################

def AverageN (Numbers): # Using a Variable number of Parameters

    Total = 0.0; # Initialise Variable to store the Sum of all Arguments.

    for Number in Numbers: # For each Argument,
        Total += float(Number);   # increment the Total.

    return (Total / len(Numbers)); # Return the Average.

#TEST BED 
#======== 

List_of_Lists = [[1 , 2, 4], [0.1 , 2.95, 7], [1 , 2.6], [1 , 13.2, 9.2, 4, 6, 10], [2.9999]];

for List in List_of_Lists:
    print AverageN(List);
# In turn: 3 Integers, 3 Mix float/Integer, 2 Numbers, 6 Numbers, 1 Number 

