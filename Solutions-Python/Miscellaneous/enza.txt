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
### read the first line of the file (has to be a Sequence Start)
### REPEAT ... know at this point a ">" line has been read.
###     Set Output file to reflect whether cancer or not
###     Output Header Line.
###     REPEAT ... 
###         read a line
###         if EOF break;
###         if new header line break;
###         Output what must be sequence line
###     if EOF break

# Make the Cancer Acc code list.
acc_file=open ("accs");            # Open the Acc code file.
acc_list = [];                     # Make an empty list.
for Line in acc_file:              # Read in the Acc codes,
    acc_list.append(Line.strip()); # Stick each one in the list.
acc_file.close();                  # Close the Acc code file.

seq_infile = open ("SwissProt-Human.fasta"); # Open the Input File for reading.
seq_cancer = open("Cancer.fasta", "w");      # Open an Output file for the Cancer Seqeunces.
seq_other  = open("/dev/null","w")           # Open a NULL file for the Other Sequences.

Line = seq_infile.readline();        # Read First Line of Sequence File.
while True:                          # Repeat ... loop always has header line at the top.
    if (Line.split("|")[1]) in acc_list:  # if cancer,
        Outfile = seq_cancer;             # point output to Cancer File
    else:                                 # if not cancer,
        Outfile = seq_other;              # point output to Other File (NULL)

    Outfile.write(Line);                  # Write header line to output.

    while True:                           # Repeat ... has to be header to start
        Line = seq_infile.readline();     # Get next Line.
        if Line.strip() == "":            # If EOF,
            break;                        # break from inner loop.
        if Line[0] == ">":                # If New Sequence,
            break;                        # break from inner loop.
        Outfile.write(Line);              # If Sequence Line, write to output.

    if Line.strip() == "":                # If EOF,
        break;                            # break from outer loop.

seq_infile.close(); # Close the Input File for reading.
seq_cancer.close(); # Close an Output file for the Cancer Seqeunces.
seq_other.close();  # Close a NULL file for the Other Sequences.

