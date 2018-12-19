# Tables taken from EMBOSS Source code who took it from
# " Bill Pearson's include files"

AA_Codes = "GAVLISTDENQKHRFYWCMP"

Helix_LODs = (
    ( -5,-10,-15,-20,-30,-40,-50,-60,-86,-60,-50,-40,-30,-20,-15,-10, -5), # G
    (  5, 10, 15, 20, 30, 40, 50, 60, 65, 60, 50, 40, 30, 20, 15, 10,  5), # A
    (  0,  0,  0,  0,  0,  0,  0,  5, 10, 14, 10,  5,  0,  0,  0,  0,  0), # V
    (  0,  5, 10, 15, 20, 25, 28, 30, 32, 30, 28, 25, 20, 15, 10,  5,  0), # L
    (  5, 10, 15, 20, 25, 20, 15, 10,  6,  0,-10,-15,-20,-25,-20,-10, -5), # I
    (  0, -5,-10,-15,-20,-25,-30,-35,-39,-35,-30,-25,-20,-15,-10, -5,  0), # S
    (  0,  0,  0, -5,-10,-15,-20,-25,-26,-25,-20,-15,-10, -5,  0,  0,  0), # T
    (  0, -5,-10,-15,-20,-15,-10,  0,  5, 10, 15, 20, 20, 20, 15, 10,  5), # D
    (  0,  0,  0,  0, 10, 20, 60, 70, 78, 78, 78, 78, 78, 70, 60, 40, 20), # E
    (  0,  0,  0,  0,-10,-20,-30,-40,-51,-40,-30,-20,-10,  0,  0,  0,  0), # N
    (  0,  0,  0,  0,  5, 10, 20, 20, 10,-10,-20,-20,-10, -5,  0,  0,  0), # Q
    ( 20, 40, 50, 55, 60, 60, 50, 30, 23, 10,  5,  0,  0,  0,  0,  0,  0), # K
    ( 10, 20, 30, 40, 50, 50, 50, 30, 12,-20,-10,  0,  0,  0,  0,  0,  0), # H
    (  0,  0,  0,  0,  0,  0,  0,  0, -9,-15,-20,-30,-40,-50,-50,-30,-10), # R
    (  0,  0,  0,  0,  0,  5, 10, 15, 16, 15, 10,  5,  0,  0,  0,  0,  0), # F
    ( -5,-10,-15,-20,-25,-30,-35,-40,-45,-40,-35,-30,-25,-20,-15,-10, -5), # Y
    (-10,-20,-40,-50,-50,-10,  0, 10, 12, 10,  0,-10,-50,-50,-40,-20,-10), # W
    (  0,  0,  0,  0,  0,  0, -5,-10,-13,-10, -5,  0,  0,  0,  0,  0,  0), # C
    ( 10, 20, 25, 30, 35, 40, 45, 50, 53, 50, 45, 40, 35, 30, 25, 20, 10), # M
    (-10,-20,-40,-60,-80,-100,-120,-140,-77,-60,-30,-20,-10, 0, 0, 0,  0)) # P

Sheet_LODs = (
    ( 10, 20, 30, 40, 40, 20,  0,-20,-42,-20,  0, 20, 40, 40, 30, 20,-10),
    (  0,  0,  0,  0, -5,-10,-15,-20,-23,-20,-15,-10, -5,  0,  0,  0,  0),
    (  0,  0,-10,-20,  0, 20, 40, 60, 68, 60, 40, 20,  0,-20,-10,  0,  0),
    (  0,  0,  0,  0,  0,  5, 10, 20, 23, 20, 10,  5,  0,  0,  0,  0,  0),
    (  0,-10,-20,-10,  0, 20, 40, 60, 67, 60, 40, 20,  0,-10,-20,-10,  0),
    (  0, 10, 20, 10,  0, -5,-10,-15,-17,-15,-10, -5,  0, 10, 20, 10,  0),
    (  5, 10, 15, 20, 15, 15, 10, 10, 13, 10, 10, 15, 15, 20, 15, 10,  5),
    (  0,  5, 10, 15, 20,  0,-20,-30,-44,-30,-20,  0,  0,  0,  0,  0,  0),
    (-10,-15,-20,-25,-30,-35,-40,-45,-50,-55,-60,-60,-50,-40,-30,-20,-10),
    ( 10, 30, 50, 30, 20,  0,-15,-30,-41,-30,-15,  0, 20, 50, 30, 50, 10),
    (  0,  0,  0,  0,  0, -5,-10,  0, 12, 20, 30, 40, 50, 50, 40, 30, 15),
    ( -5,-10,-15,-20,-30,-40,-50,-40,-33,-20,-10,  0, 10, 10,  0,  0,  0),
    (-10,-20,-40,-20,-10,  0,-10,-20,-25,-35,-30,-25,-20,-15,-10, -5,  0),
    (  0,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0),
    (  0,  0,  0,  0,  0,  5, 10, 20, 26, 10,-10,-30,-60,-65,-60,-40,-20),
    (  0,  5, 10, 15, 20, 25, 30, 35, 40, 35, 30, 25, 20, 15, 10,  5,  0),
    (  0,  0,  0,  0,  0,-10,-10,-10,-10,-10,-10,-15,-20,-25,-30,-20,-10),
    (  0,  0,  0,  0,  0, 10, 20, 30, 44, 30, 20, 10,  0,  0,  0,  0,  0),
    (-10,-20,-30,-40,-40,-30,  0, 10, 23, 10,  0,-30,-40,-40,-30,-20,-10),
    ( 10, 20, 30, 30, 20, 10,  0,-10,-18,-20,-10, 10, 30, 40, 30, 20, 10))

Turn_LODs = (
    (  0,  0,  0,  0, 10, 30, 55, 55, 57, 40,  0,  0,  0,  0,  0,  0,  0),
    (  0,  0,  0,-10,-20,-30,-40,-50,-50,-40,-30,-20,-10,  0,  0,  0,  0),
    (  0,  0,  0,  0,-10,-20,-30,-40,-60,-40,-30,-20,-10,  0,  0,  0,  0),
    (  0,  0,  0,-10,-20,-30,-40,-50,-56,-20,-10,  0,  0,  0,  0,  0,  0),
    (  0,  0,  0,  0,  0,-10,-20,-30,-46,-40,-10,  0,  0, 20, 30, 20, 10),
    (  0,-10,-20,-20, 10, 15, 20, 25, 26, 25, 20, 15, 10,  0,  0,  0,  0),
    (  0, 10, 20, 20, 20, 15, 18,  5,  3,  5, 10, 15, 20, 20, 20, 10,  0),
    (  0,  0,  0,  0,  0,  0,  5, 10, 31, 10,  5,  0,  0,  0,  0,  0,  0),
    (  0, -5,-10,-15,-20,-30,-40,-45,-47,-20,  0, 10,  5,  0,  0,  0,  0),
    (  0,  0,  0, 10, 20, 30, 35, 40, 42, 40, 35, 30, 20, 10,  5,  0,  0),
    ( 10, 20, 30, 25, 20, 15, 10,  5,  4, 20, 30, 40, 50, 60, 50, 40, 20),
    (-10,-20,-30,-40,-25,-10,  0, 10, 10, 10,  0,-20,-30,-20,-10, -5,  0),
    (  0,  0,  0,  0,  0,  0,  0,  0, -3,  0, 10, 20, 30, 20, 10,  0,  0),
    (  0,  0,  0,  0,  0,  0,  0, 10, 21, 30, 40, 30, 20, 10,  0,  0,  0),
    (  0,  0,  0,  0,  0, -5,-10,-15,-18,-15,  0, 15, 30, 25, 20, 10,  0),
    (  0,  0,  0,  5, 15, 15, 20, 25, 29, 25, 20, 15, 15,  5,  0,  0,  0),
    (  0,  0,  0, 10, 20, 30, 40, 80, 36,-30, 30, 40, 50, 60, 70, 40, 20),
    ( 20, 40, 50, 60, 60, 55, 50, 45, 44, 40, 35, 30, 25, 20, 15, 10,  5),
    ( -5,-15,-20,-25,-30,-35,-40,-45,-48,-45,-40,-35,-30,-25,-20,-15, -5),
    ( 10, 20, 30, 40, 50, 70, 10,-90, 36, 90, 10,  0,  0,  0,  0,  0,  0))

Coil_LODs = (
    (  0,  0,  0,  0, 10, 30, 40, 45, 49, 45, 40, 30, 10,  0,  0,  0,  0),
    (  0,  0,  0,  0, -5,-10,-20,-25,-25,-25,-20,-15,-10, -5,  0,  0,  0),
    (  0,  0,  0,  0,-10,-20,-25,-30,-35,-30,-25,-20,-10,  0,  0,  0,  0),
    (  0,  0,  0,-10,-20,-30,-40,-30,-20,-20,-10,  0,  0,  0,  0,  0,  0),
    (  0,  0,  0,  0,  0,-10,-20,-30,-33,-30,-10,  0, 10, 20, 30, 20,  0),
    (  0,-10,-20,-20, 10, 15, 20, 25, 50, 25, 20, 15, 10,  0,  0,  0,  0),
    (  0, 10, 20, 30, 20, 15, 10, 15, 17, 15, 10, 15, 20, 30, 20, 10,  0),
    (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
    (  0,  0, 10, 20, 40, 20,  0,-10,-44,-40,-20,-10,  0,  0,  0,  0,  0),
    (  0,  0,  0, 10, 20, 30, 35, 40, 46, 40, 35, 30, 20, 10,  0,  0,  0),
    ( 10, 20, 30, 25, 20, 15, 10,  0, -5, 20, 30, 40, 50, 60, 50, 40, 20),
    (-10,-20,-30,-40,-25,-20,-10, -8, -8,  0,  0,-20,-30,-20,-10, -5,  0),
    (  0,  0,  0,  0,  0,  0,  0, 10, 16, 15, 10, 10, 10, 10,  5,  0,  0),
    (  0,  0,  0,  0,  0,  0,  0,  0,-12,  0, 20, 30, 20, 10,  0,  0,  0),
    (  0,  0,  0,  0,  0, -5,-10,-20,-41,-20,  0, 15, 30, 25, 20, 10,  0),
    (  0,  0,  0,  0,  0,  0,  0,  0, -6,  0,  0,  0,  0,  0,  0,  0,  0),
    (  0,  0,  0, 10, 20, 30, 40, 20, 12, 20, 30, 40, 50, 60, 70, 40, 20),
    (  0,  0,  0,  0,  0,  0,-10,-30,-47,-30,-10,  0,  0,  0,  0,  0,  0),
    (  0, -5,-10,-15,-20,-25,-30,-40,-41,-40,-30,-25,-20,-15,-10, -5,  0),
    (  0,  0, 10, 20, 30, 40, 50, 55, 58, 50, 10,  0,  0,  0,  0,  0,  0))

###################################################################
# Test Procedures & Data
###################################################################

Structure_Table = (Helix_LODs, Sheet_LODs, Turn_LODs, Coil_LODs)
Structure_Code  = ('H','E','T','C')
#Structure_Code  = ('H',' ',' ',' ')

# Display Scoring Matrices.

def Print_LOD_Table(LOD_Table=Helix_LODs, Table_Title="Mystery Table"):
	
  print ("\n",Table_Title)
  for i in range(19):
    for j in range (16):
      print ("%4d" % LOD_Table[i][j],end='')
    print()

# Test Bed

'''

Print_LOD_Table(Helix_LODs,"Helix")
Print_LOD_Table(Sheet_LODs,"Sheet")
Print_LOD_Table(Coil_LODs,"Coil")
Print_LOD_Table(Turn_LODs,"Turn")
Print_LOD_Table(LOD_Table=Helix_LODs)
Print_LOD_Table(Table_Title="Default ... Helix")
Print_LOD_Table()

'''

# Test Sequence

Test_Sequence = "MQNSHSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRY\
YETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSV\
SSINRVLRNLASEKQQMGADGMYDKLRMLNGQTGSWGTRPGWYPGTSVPGQPTQDGCQQQ\
EGGGENTNSISSNGEDSDEAQMRLQLKRKLQRNRTSFTQEQIEALEKEFERTHYPDVFAR\
ERLAAKIDLPEARIQVWFSNRRAKWRREEKLRNQRRQASNTPSHIPISSSFSTSVYQPIP\
QPTTPVSSFTSGSMLGRTDTALTNTYSALPPMPSFTMANNLPMQPPVPSQTSSYSCMLPT\
SPSVNGRSYDTYTPPHMQTHMNSQPMGTSGTTSTGLISPGVSVPVQVPGSEPDMSQYWPR\
LQ"

A_Sequence  = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEKQQMGADGMYDKLRMLN"
#A_Sequence  = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

Mix_Sequence= "GAVLISTDENQKHRFYWCMPGAVLISTDENQKHRFYWCMPGAVLISTDENQKHRFYWCMP"
#A_Sequence  = "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEKQQMGADGMYDKLRMLN"
#A_Sequence  = "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
# Procedure to Calculate LOD Count for single Window

def Window_Score(LOD_Table, Protein, Window_Middle):

  LOD_Count = 0
  
  Last_aa      = len(Protein)
  Window_End = max(-1, Window_Middle - 9)
  Window_Start   = min(Last_aa - 1, Window_Middle + 8)
#  Window_Start = min(Last_aa - 1, Window_Middle + 7)
#  Window_End   = max(-1, Window_Middle - 10)
  print(range(Window_Start, Window_End,-1),",,,,,,",list(range(Window_Start, Window_End,-1)))
#  for aa in range(Window_Start, Window_End):
  for aa in range(Window_Start, Window_End, -1):

#   	print (aa,
# 	  Protein[aa],
#    LOD_Table[AA_Codes.find(Protein[aa])],
#    LOD_Table[AA_Codes.find(Protein[aa])] [Window_End - aa )

		  print (LOD_Table[AA_Codes.find(Protein[aa])] [Window_End - aa], end=' ')
		  
		  LOD_Count += LOD_Table[AA_Codes.find(Protein[aa])] [Window_End - aa]

  print ("xxx ",LOD_Count)

  return LOD_Count
  	 
# Test Bed

'''
print ("\n\nHelix")
for aa in range(0,421):
  print(Window_Score(Helix_LODs, Test_Sequence, aa), end=' ')
  
print ("\n\nSheet")
for aa in range(0,421):
  print(Window_Score(Sheet_LODs, Test_Sequence, aa), end=' ')
  
print ("\n\nTurn")
for aa in range(0,421):
  print(Window_Score(Turn_LODs, Test_Sequence, aa), end=' ')
  
print ("\n\nCoil")
for aa in range(0,421):
  print(Window_Score(Coil_LODs, Test_Sequence, aa), end=' ')

print ("\n\nHelix")
for aa in range(50,51):
  print(Window_Score(Helix_LODs, Test_Sequence, aa), end=' ')
print ("\n\nSheet")
for aa in range(50,51):
  print(Window_Score(Sheet_LODs, Test_Sequence, aa), end=' ')
print ("\n\nTurn")
for aa in range(50,51):
  print(Window_Score(Turn_LODs, Test_Sequence, aa), end=' ')
print ("\n\nCoil")
for aa in range(50,51):
  print(Window_Score(Coil_LODs, Test_Sequence, aa), end=' ')

print(Test_Sequence[49], Window_Score(Helix_LODs, Test_Sequence, 49), end=' ')
print(Test_Sequence[49], Window_Score(Sheet_LODs, Test_Sequence, 49), end=' ')
print(Test_Sequence[49], Window_Score(Turn_LODs,  Test_Sequence, 49), end=' ')
print(Test_Sequence[49], Window_Score(Coil_LODs,  Test_Sequence, 49), end=' ')
print()
'''
# Procedure to Predict the Secondary Structure
# of a Protein using (roughly) The original GOR
# method.

def GORI(Protein, First_Window = 0, Last_Window = -1):

  if Last_Window == -1:
    Last_Window = len(Protein)
  
  Prediction = ""

  for aa in range(First_Window, Last_Window):
    print ("===========",aa)
    Prediction_Code  = ' '
    Prediction_Score = -99999

    for Table in range(0,4):
		    Table_Score = Window_Score(Structure_Table[Table], Protein, aa)
		    if Table_Score >= Prediction_Score:
		      Prediction_Score = Table_Score
		      Prediction_Code  = Structure_Code[Table]

    print(Prediction_Score, Table_Score, "***")

    Prediction += Prediction_Code

  return Prediction

# Test Bed

'''

print (GORI(Test_Sequence,20,21))
print (GORI(Test_Sequence))
print (GORI(Test_Sequence,False))

'''

def Display_Prediction(Protein, Prediction, Trim = True, Line_Length = 50):	

	 Protein_Length = len(Protein)
	 Prediction_Pad = "........"
	 
	 if Trim:
	 	 Display_Prediction = Prediction_Pad + Prediction[8:-7] + Prediction_Pad
	 else:
	 	 Display_Prediction = Prediction
	 	 
	 Line_Start = 0
	 
	 while Line_Start < Protein_Length:
	 	 Line_End = min(Line_Start + Line_Length, Protein_Length)
	 	 print(Protein[Line_Start: Line_End], Line_End)
	 	 print(Display_Prediction[Line_Start: Line_End], end='\n\n')
	 	 Line_Start += Line_Length
	 	 
	 return Display_Prediction

# Test Bed

#'''                      
Structure_Prediction = Display_Prediction(A_Sequence, GORI(A_Sequence), False)
'''
Structure_Prediction = Display_Prediction(Test_Sequence, GORI(Test_Sequence), False)
Structure_Prediction = Display_Prediction(Test_Sequence, GORI(Test_Sequence),  60)
Structure_Prediction = Display_Prediction(Test_Sequence, GORI(Test_Sequence), 100)
print (Structure_Prediction)

'''

##########################################################################
##########################################################################
# Main
##########################################################################
##########################################################################


##########################################################################