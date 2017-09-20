# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:15:05 2017

@author: Meena
"""
fam=[1.73,1.68,1.52,1.23]
max(fam)
round(1.68)
import numpy as np
h=[1,5,8,9,5]
w=[1,8,5,9,7]
np_h=np.array(h)
np_w=np.array(w)
bmi=np_w/np_h**2
print(bmi)
np.round(bmi,2)
x=bmi[2]
print(x)
np.round(x,2)

np.array([1,"is",True])
np_array=np.array([1,2,3])
np_x=np_array+np_array
print(np_x)
bmi[1]
bmi>5
np_w>5
np_w[np_w>5]
type(np_w)
