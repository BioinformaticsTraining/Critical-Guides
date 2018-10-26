from random import randint; # Import the random integer generator
                            # from the module random. 
Target = randint(1,20);     # Generate the Integer to be matched. 
Guess = randint(1,20);      # Generate the first attempt to match the Target. 

while Guess != Target:      # While the Target is not matched, 
    print "Target (" + str(Target) + ") does not match Guess (" \
    + str(Guess) + "). \tTry again!";
    Guess = randint(1,20);  # Sadly admit failure,and try again. 

print "Hoorah! Target and Guess are both = " + str(Guess);
                            # When a match is acheived, be happy.
