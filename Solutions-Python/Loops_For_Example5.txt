import urllib; # import the code to access remote files. 

File_URL = 'http://www.uniprot.org/uniprot/P12931.fasta';
Sequence_file = urllib.urlopen(File_URL); # Open remote file for reading. 

while True:   # Repeat ... 
   Line = Sequence_file.readline(); # Read the next line using readline. 
   if not Line: break; # If at the end of the, stop reading/printing. 
   print Line,          # print this Line and go round for more. 

Sequence_file.close(); # Close file tidily. 
