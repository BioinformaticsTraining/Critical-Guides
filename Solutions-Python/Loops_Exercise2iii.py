######################################################
### Open the file ... one last exasperating time!
###
### Initialise a count for the Hydrophobics.
###
### Keep reading the file one line at a time until it is empty
###    print any lines that begin with ">"
###    for lines that do not begin with ">"
###        for each amino acid in the line
###        if it is Hydrophobic, add one to the Hydropobic Count
###
### Announce the count of Hydrophobics
###
### Close the file.
###
### Data Structures:
### ================
###
### I see a test to determine whether a given amino acid 
### is hydrophobic ... is not the way to do that to ask if said
### amino acid exists in a list of hydrophobic amino acids?
###
### I reckon I need a list of Hydrophic Amino Acids.
### Even a tuple, as it would be naturally immutable.
#######################################################

# A tuple of Hydrophobic Amino Acids.

Hydrophobics = ('A', 'I', 'L', 'M', 'F', 'V', 'P', 'G');

# Open sequences.fasta making the "File Handle" Sequence_File.
Sequence_File = open("sequences.fasta");

Hydrophobic_Count = 0;         # Initialise Count of Hydrophobics.

for Line in Sequence_File:   # So for each Line in turn,
    if Line[0] == ">":       # If the first character is  ">"
        print Line;          # print it.
    else:                    # Otherwise it is a sequence line, so
        for aa in Line:      # for each amino acid in the line,
            if aa in Hydrophobics:      # if it is a Hydrophobic,
                Hydrophobic_Count += 1; # add 1 to the count.
# Display the Hydrophobic Count.
print "There were " + str(Hydrophobic_Count) + " Hydrophobics.";

Sequence_File.close();       # Tidily close the file.

