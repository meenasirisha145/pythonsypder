# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 14:26:34 2017

@author: Meena
"""
import numpy as np
import sklearn
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
a=pd.read_csv("train.csv")
a
a.shape
a.isnull().sum()
x=np.mean(a.Age)
x
a.loc[a.Age.isnull(),"Age"].shape
a.isnull().sum()
