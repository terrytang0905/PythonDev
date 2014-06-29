#!/usr/bin/python
# Filename: using_sys.py

'''
Created on May 31, 2014

@author: terrymac
'''

import sys
#from sys import argv

print 'The command line arguments are:'
for i in sys.argv:
    print i
    
print dir(sys)
 
print '\n\n The PYTHON PATH is',sys.path, '\n'