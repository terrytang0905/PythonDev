
#!/usr/bin/python
# Filename: using_name.py

'''
Created on Jun 1, 2014

@author: terrymac
'''
import helloWorld

# _name_ is build-in varible for python, the top-level code is an if block.  __name__ is a built-in variable which evaluate to the name of the current module.
if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another module'