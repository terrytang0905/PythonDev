#!/usr/bin/python
# Filename: func_local.py

'''
Created on May 31, 2014

@author: terrymac
'''

def func(x):
    print 'x is',x
    x=2
    print 'Changed local x to',x #just work in function
    
x=50
func(x)
print 'x is still',x