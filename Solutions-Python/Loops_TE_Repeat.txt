from random import randint; # Import the random integer generator
                            # from the module random. 
Target = randint(1,20);     # Generate the Integer to be matched. 

while True:                 # While ... 
    Guess = randint(1,20);
    if Guess == Target:
        break;
    else:                   # Sadly admit failure,and try again. 
        print "Target (" + str(Target) + ") does not match Guess (" \
        + str(Guess) + "). \tTry again!";

print "Hoorah! Target and Guess are both = " + str(Guess);
                            # When a match is acheived, be happy.
