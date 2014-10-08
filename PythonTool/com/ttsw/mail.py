'''
Created on May 29, 2014

@author: terrymac
'''
import poplib,email

try:

    p=poplib.POP3('pop.qq.com')
    p.user('xx')
    p.pass_('xx')
    ret = p.stat()
except poplib.error_proto,e:
    print "Login failed:",e
list=p.list()[1]
list.reverse()
for item in list:
    number,octets = item.split(' ')
    lines=p.retr(number)[1]
    for piece in lines:
        print piece
