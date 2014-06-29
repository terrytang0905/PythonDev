'''
Created on Jun 3, 2014

@author: terrymac
'''

#!/usr/bin/python 
#Filename: class_init.py
class Person:
    test=1
    def __init__(self, name):
        self.name= name 
    def sayHi(self) :
        print 'Hello , my name is ' , self.name
p= Person('Swaroop') 
print Person.test
p.sayHi()
# T h i s s h o r t ex am p l e can al s o b e w r i t t en as Person ('Swaroop').sayHi()
        