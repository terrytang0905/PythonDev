'''
Created on Jun 4, 2014

@author: terrymac
'''


#!/usr/bin/python 
#Filename: finally.py
import time
try:
    f = file('/Users/terrymac/Downloads//backup/poem.txt')
    while True: #our usual file-reading idiom
        line= f.readline() 
        if len (line) == 0 :
            break 
        time.sleep(2) 
        print line,
finally: 
    f.close()
print 'Cleaning up...closed the file'