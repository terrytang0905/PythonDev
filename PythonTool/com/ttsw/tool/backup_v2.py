'''
Created on Jun 3, 2014

@author: terrymac
'''

#!/usr/bin/python 
#Filename: backup_ver2.py
import os 
import time
#1. The files and directories to be backed up a respecified in a list.
source=['/Users/terrymac/Downloads/Resume','/Users/terrymac/Downloads/Share']
#I f you are using Windows, use source= [r'C:\Documents', r'D:\Work'] or something like that
#2. T hebackupmust bestoredin amain backupdirectory
target_dir='/Users/terrymac/Downloads/backup/' #Remember tochangethistowhatyouwill beusing

#3. T hefiles arebackedupintoazipfile.
#4. T hecurrent day is thenameof thesubdirectory in themain directory 
today= target_dir + time.strftime('%Y%m%d')
#T hecurrent timeis thenameof theziparchive
now= time.strftime('%H %M%S')
#Createthesubdirectory if it isn't already there 
if not os.path.exists(today):
    os.mkdir(today) #makedirectory
    print 'Successfully created directory', today
# T h e n am e o f t h e z i p f i l e
target = today + os.sep+ now+ '.zip'
# 5 . W e u s e t h e z i p co m m an d ( i n U n i x / L i n u x ) t o p u t t h e f i l es i n a z i p ar ch i v e 
zip_command= "zip -qr '%s' %s" % (target, ' '.join(source))
#Run thebackup
if os.system(zip_command) == 0:
    print 'Successful backup to', target 
else:
    print ' Back up FAILED '