######################################################
### Open the file ... again!
###
### Keep reading the file one line at a time until it is empty
###    ignore any lines that do not begin with ">"
###    print all the lines you have not ignored
###
### Close the file.
#######################################################

# Open sequences.fasta making the "File Handle" Sequence_File.
Sequence_File = open("sequences.fasta");

for Line in Sequence_File:   # So for each Line in turn,
    if Line[0] != ">":       # If the first character is not ">"
        continue;            # ignore it.
    print Line;              # Print out the Line.

Sequence_File.close();       # Tidily close the file.

# This just feels horrid??? Such a struggle to use continue
# Hope you see how continue works from this , but just
# have to write it again more naturally!


