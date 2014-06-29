'''
Created on Jun 11, 2014

@author: terrymac
'''

logfile = open('test.log', 'w') #write
logfile.write('test succeeded')
logfile.close()
print file('test.log').read()

logfile = open('test.log', 'a') #append
logfile.write('line 2')
logfile.close()
print file('test.log').read()

if __name__ == '__main__':
    pass