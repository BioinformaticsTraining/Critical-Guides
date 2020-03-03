#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as pl

#import random
np.random.seed()
Y=N=x=y=0
counts=1000000000
for i in range(0,counts,1):
  #np.random.seed()
  x=np.random.uniform(0,1)
  y=np.random.uniform(0,1)
  if (np.sqrt((x**2) + (y**2))) <= 1:
    Y+=1
  else:
    N+=1
  print(x,y,N,Y,(x**2) + (y**2))
print("Pie is ", (Y/counts)*4)
