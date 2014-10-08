'''
Created on Jun 4, 2014

@author: terrymac
'''

#!/usr/bin/python 
#Filename: pickling.py
import cPickle as p 
#import pickle as p
shoplistfile= '/Users/terrymac/Downloads//backup/shoplist.data'
#the name of the file where we will store the object
shoplist = ['apple', 'mango', 'carrot']
#Write to the file
f = file(shoplistfile, 'w')
p.dump(shoplist, f) #dump the object to a file 
f.close()
del shoplist #removetheshoplist
#Readback fromthestorage 
f = file(shoplistfile)
storedlist = p.load(f)
print storedlist
        