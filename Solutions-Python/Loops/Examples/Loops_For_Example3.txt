Sequence_file = open("homeobox_human.fasta"); # Open the target file for reading 

Sequence_Count = 0; # Initialise the Annotation Line Counter variable 
AA_Count = 0;       # Initialise the Amino Acid Counter variable 

for Line in Sequence_file:   # For each Line of Sequence_file 
    if Line[0] == ">":       # If this is an Annotation Line, 
        print Line;          # Print the Line, 
        Sequence_Count += 1; # Increment the Sequence Counter. 
        continue;            # move to the top of the Loop for the next Line 
    AA_Count += len(Line);   # Increment the Sequence Counter. 

Sequence_file.close(); # Close the file of sequences 

# Print the Sequence & Amino Acid Counts 
print "There are " + str(Sequence_Count) + " Protein Sequences in the file"
print "There are " + str(AA_Count) + " Amino Acid Codes in the file"
