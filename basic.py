# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:58:52 2017

@author: Meena
"""

a=15
print(a)
fam=[1.73,1.68,1.52,1.23]
print(fam)
print(fam+fam)
print(fam*3)
max(fam)
fam=["liz",1.73,"reena",1.54,"anu",1.65,"ram",1.28]
print(fam)
fam1=[["liz",1.73],["ram",1.65]]
print(fam1)
print(fam[3])
print(fam[-1])
print(fam[3:5])
print(fam[:4])
print(fam[4:])
fam[0:2]=["lisa",1.74]
print(fam)
fam2=fam+["gp",1.9]
print(fam2)
del(fam2[2:4])
print(fam2)
x=[1,2,3]
y=x
y[1]=6
print(y)
print(x)
y=list(x)
y[1]=4
print(x)
print(y)

z=[[1,5,6,8,6],[5,4,8,6,9]]
print(z[0][3])

import numpy as np
list=[1,5,10,15,20]

print(list)
list.insert(3,12)
print(list)
sum(list)
len(list)
np.sum(list)
np.mean(list)
np.average(list)
from numpy import array
array([1,2,3])
