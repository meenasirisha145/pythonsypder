# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 20:04:15 2017

@author: Meena
"""

def missing_char(s,n):
    if n in range(0,len(s)):
        s1 = s[:n] + s[n+1:]
        print(s1)

missing_char('meena',2)



        
        