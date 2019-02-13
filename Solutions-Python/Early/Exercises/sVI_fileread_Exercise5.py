# Open a file for writing

fh=open("File_of_Lines",'w')

# Fill "File_of_Lines" full of lines with one command

fh.write("abcdef\nghijkl\nmnop\nqrst\nuvwxyz01\n234\n56789\nand so say ALL of us")

# Close "File_of_Lines" for writing

fh.close()

# Open "File_of_Lines" for reading

fh=open("File_of_Lines",'r')

# Read each line of "File_of_Lines" in turn

for Line in fh:
  Line=Line.rstrip('\n')         # remove the trailing '\n' read from the file by write
  print(Line)                    # print the line as read
  print(Line.upper())            # print the uppercase version of the current line
  Line_Case_Swap=Line.swapcase() # make a case swapped version of the current line
  print(Line_Case_Swap)          # print the case swapped version of the current line
  print(Line_Case_Swap[::-1])    # print the case swapped version of the current line backwards

# Print nauseous line of self congratulation!

print("I am so clever to acheive this awesome task ... and now I need but to sit back and listen")
print("to the sound of the Frontiers of Science rumbling in confused retreat in the face of unequalled powers!")
