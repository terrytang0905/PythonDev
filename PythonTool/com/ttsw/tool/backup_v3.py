'''
Created on Jun 3, 2014

@author: terrymac
'''

#!/usr/bin/python 
#Filename: backup_ver3.py
import os 
import time
#1. T hefiles anddirectories tobebackeduparespecifiedin alist.
source=['/Users/terrymac/Downloads/Resume','/Users/terrymac/Downloads/Share']
#I f you areusingWindows, usesource= [r'C:\Documents', r'D:\Work'] or somethinglikethat
#2. T hebackupmust bestoredin amain backupdirectory
target_dir='/Users/terrymac/Downloads/backup/' #Remember tochangethistowhatyouwill beusing

#3. T hefiles arebackedupintoazipfile.
#4. T hecurrent day is thenameof thesubdirectory in themain directory 
today= target_dir + time.strftime('%Y%m%d')
#T hecurrent timeis thenameof theziparchive
now= time.strftime('%H%M%S')
#T akeacomment fromtheuser tocreatethenameof thezipfile 
comment = raw_input('Enter a comment --> ')
if len(comment) == 0: #check if acomment was entered
    target = today + os.sep+ now+ '.zip' 
else:
    target = today + os.sep+ now+ '_' + \
        comment.replace(' ', '_') + '.zip'
#Createthesubdirectory if it isn't already there 
if not os.path.exists(today):
    os.mkdir(today) #makedirectory
    print 'Successfully created directory', today
# 5 . W e u s e t h e z i p co m m an d ( i n U n i x / L i n u x ) t o p u t t h e f i l es i n a z i p ar ch i v e 
zip_command= "zip -qr '%s' %s" % (target, ' '.join(source))
#Run thebackup
if os.system(zip_command) == 0:
    print 'Successful backup to', target 
else:
    print 'Back up FAILED'