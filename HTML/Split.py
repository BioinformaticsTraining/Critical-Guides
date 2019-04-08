#!/usr/bin/python3

ifh = open("Python_Bits.html",'r')
ofh = open ("x.html",'w')

for Line in ifh:
  if ("###CUT000###" == Line.rstrip()): break
  else: ofh.write(Line)

for Line in ifh:
  if ("###MOD000###" == Line.rstrip()): break

for Line in ifh:
  if ("###MOD000###" == Line.rstrip()): break
  else: ofh.write(Line)

for Line in ifh:
  if ("###CUT000###" == Line.rstrip()): break

for Line in ifh:
  ofh.write(Line)

ifh.close()
ofh.close()
