#!/usr/bin/python
# Filename: using_set.py

a=[1,2,4,2,4,5,6,5,7,8,9,0]
b={}
b=b.fromkeys(a)
c=list(b.keys())
print(c)