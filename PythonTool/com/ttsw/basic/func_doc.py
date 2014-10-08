
#!/usr/bin/python
# Filename: func_doc.py

'''
Created on May 31, 2014

@author: terrymac
'''

def printMax(x,y):
    '''Prints them maximum of two numbers.
    
    The two values must be integers.'''
    x=int(x)
    y=int(y)
    
    if x>y:
        print x,'is maximum'
    else:
        print y,'is maximum'
        
printMax(3,5)
print printMax.__doc__ #doc string 