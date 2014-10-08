
#!/usr/bin/python
# Filename: str_methods.py

'''
Created on Jun 1, 2014

@author: terrymac
'''

name='Swaroop'

if name.startswith('Swa'):
    print 'Yes,the string starts with "Swa"'
    
if 'a' in name:
    print 'Yes,it contains the string "a"'
    
if name.find("war")!=-1:
    print 'Yes,it contains the string "war"'

delimiter='_*_'
mylist=['Brazil','Russia','India','China']
"Connect mylist items with delimiter"
print delimiter.join(mylist)