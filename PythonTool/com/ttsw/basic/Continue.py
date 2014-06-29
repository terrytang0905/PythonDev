#!/usr/bin/python
# Filename: continue.py

'''
Created on May 30, 2014

@author: terrymac
'''

while True:
    s=raw_input('Enter something:')
    if s=='quit':
        break
    if len(s)<3:
        continue
    print 'Input is of sufficient length'