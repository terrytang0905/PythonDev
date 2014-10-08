#!/usr/bin/python
# Filename: reference.py

'''
Created on Jun 1, 2014

@author: terrymac
'''

print 'Simple Assignment'
shoplist=['apple','mango','carrot','banana']
mylist=shoplist

del shoplist[0]

print 'shoplist is',shoplist
print 'mylist is',mylist

print 'Copy by making a full slice'
mylist=shoplist[:] #make a copy by doing a full slice
del mylist[0]

print 'shoplist is',shoplist
print 'mylist is',mylist