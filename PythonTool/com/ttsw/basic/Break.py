
#!/usr/bin/python
# Filename: break.py

'''
Created on May 30, 2014

@author: terrymac
'''

while True:
    s=raw_input('Enter something:')
    if s=='quit':
        break
    print 'Length of the string is',len(s)
print'Done'