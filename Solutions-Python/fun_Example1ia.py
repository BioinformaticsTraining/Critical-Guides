###########################################################################################
### Average3 is renamed to AverageN.
###
### A Variable Number of Parameters is allowed, indicated by the "*" prefix
### for the NumbersParameter.
### 
### The variable *Numbers is used as a List to construct a For Loop to sum all Arguments.
###
### Note that the built in Function "len" works on Lists (and tuples),
### returning the Number of List elements.
### 
### return the Sum of all the Arguments, divided by the Number of Arguments ... also known
### as "The Average".
### 
###########################################################################################

def AverageN (*Numbers): # Using a Variable number of Parameters

    Total = 0; # Initialise Variable to store the Sum of all Arguments.

    for Number in Numbers: # For each Argument,
        Total += Number;   # increment the Total.

    return (Total / len(Numbers)); # Return the Average.

#TEST BED 
#======== 

print str(AverageN(1 , 2, 4));                # 3 Integers 
print str(AverageN(0.1 , 2.95, 7));           # 3 Mix float/Integer
print str(AverageN(1 , 2.6));                 # 2 Numbers 
print str(AverageN(1 , 13.2, 9.2, 4, 6, 10)); # 6 Numbers 
print str(AverageN(2.9999));                  # 1 Number 

