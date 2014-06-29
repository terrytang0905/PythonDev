'''
Created on Jun 4, 2014

@author: terrymac
'''

#!/usr/bin/python
#Filename: list_comprehension.py
listone=[2,3,4]
listtwo= [i*2 for i in listone if i > 2] 
print listtwo
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
listthree=[elem for elem in li if len(elem) > 1]
print listthree