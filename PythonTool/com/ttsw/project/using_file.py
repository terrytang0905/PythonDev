'''
Created on Jun 3, 2014

@author: terrymac
'''

#!/usr/bin/python 
#Filename: using_file.py
poem = ''' \
    Programmingis fun
    When thework is done
    if you wanna make your work also fun :
    use Python! '''
    
f = file('/Users/terrymac/Downloads//backup/poem.txt', 'w') #open for 'w'riting 
f.write( poem) # wr i t e t ex t t o f i l e
f.close() #closethefile

f = file('/Users/terrymac/Downloads//backup/poem.txt')
#i f no modei s speci fi ed, ' r ' ead modei s assumed by defaul t 
while True:
    line= f.readline()
    if len(line)== 0 : # Z er o l en gt h i n d i cat es E O F
        break
    print line, #Noticecommatoavoidautomaticnewlineaddedby Python
    
f.close() #closethefile