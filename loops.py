# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:20:11 2017

@author: Meena
"""
x=float(input("enter x"))
if x==3:
    print("X equals to 3")
elif x==2:
    print("X equals to 2")
else:
    print("X equals to something else")
print("This is outside the if")

#for loop
for somech in "Killer Rabbit":
    print(somech)
1 and 0
1 or 0
100 or 0
100 and 50
50 and 100
100 or 50
50 or 100
1 or 0 or 50
0 or 20 or 1
def myfn(b,c):
    return(b+c)
myfn(5,6)

def hello():
    name=input("enter name:")
    age=input("enter age:")
    if name:
        print("hello" + str(name))
        print("age" + age)
    else:
        print("hello world")
    return
hello()


def intersect(seq1,seq2):
    res=[]
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res
print(intersect('neena','meesha'))

def union(seq1,seq2):
    res=[]
    for x in seq1:
        res.append(x)
    for x in seq2:
        if x not in res:
            res.append(x)
    return res
print(union('neena','meesha'))