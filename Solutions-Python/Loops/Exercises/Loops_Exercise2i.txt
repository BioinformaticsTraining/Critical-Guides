######################################################
### Open the jolly old file
###
### Keep reading the file one line at a time until it is empty
###    print each line as it passes by
###
### Close the file.
#######################################################

# Open sequences.fasta making the "File Handle" Sequence_File.
Sequence_File = open("sequences.fasta");

# File Handles can be treated as Lists of the Lines of the file,
for Line in Sequence_File:   # So for each Line in turn,
    print Line;              # Print out the Line.

Sequence_File.close();       # Tidily close the file.

