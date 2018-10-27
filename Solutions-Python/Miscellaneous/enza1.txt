#########################################################
### Pseudo-Code
### 
### NO DATA CHECKING! ... Assuming perfect FASTA Format.
###
### Make a list of acc codes 
###     Open the file with the cancer acc codes for reading
###     Make an empty list
###     Populate list with file contents
###     Close file
###
### Open Seq File for input.
### Open Cancer Sequence File for Output.
### Open Non-Cancer File for Output (could be NULL file).
###
### Trick this time is only to ever read a line in one place,
### then it can be used to control loop
###########################################################
### 
### REPEAT reading a file until there are no more
###     if we have a header
###         Set Output file to reflect whether cancer or not
###
### Output the line whatever it is! 
### 
##############################################################

# Make the Cancer Acc code list.
acc_file=open ("accs");            # Open the Acc code file.
acc_list = [];                     # Make an empty list.
for Line in acc_file:              # Read in the Acc codes,
    acc_list.append(Line.strip()); # Stick each one in the list.
acc_file.close();                  # Close the Acc code file.

seq_infile = open ("SwissProt-Human.fasta"); # Open the Input File for reading.
seq_cancer = open("Cancer.fasta", "w");      # Open an Output file for the Cancer Seqeunces.
seq_other  = open("/dev/null","w")           # Open a NULL file for the Other Sequences.

for Line in seq_infile:
    if Line[0] == ">":                        # if a new header,
        if (Line.split("|")[1]) in acc_list:  # if cancer,
            Outfile = seq_cancer;             # point output to Cancer File
        else:                                 # if not cancer,
            Outfile = seq_other;              # point output to Other File (NULL)

    Outfile.write(Line);                      # Write line, whatever it is.

seq_infile.close(); # Close the Input File for reading.
seq_cancer.close(); # Close an Output file for the Cancer Seqeunces.
seq_other.close();  # Close a NULL file for the Other Sequences.

