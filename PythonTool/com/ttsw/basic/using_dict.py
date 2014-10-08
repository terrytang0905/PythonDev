#!/usr/bin/python
# Filename: using_dict.py

'''
Created on Jun 1, 2014

@author: terrymac
'''

db={'Swaroop':'swaroopch@byteofpython.info',
    'Larry':'larry@wall.org',
    'Matsumoto':'matz@ruby-lang.org',
    'Spammer':'spammer@hotmail.com'}

print "Swaroop's address is %s" % db['Swaroop']

# add new item into db
db['Guidb']='guidb@python.org'

del db['Spammer']

print '\n There are %d contacts in the address-book \n' % len(db)
for name,address in db.items():
    print 'Contact %s at %s' % (name,address)



if 'Guidb' in db:
    print "\n Guidb's color address is %s" % db['Guidb']