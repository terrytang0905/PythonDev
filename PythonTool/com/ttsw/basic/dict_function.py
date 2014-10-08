'''
Created on Jun 4, 2014

@author: terrymac
'''

def powersum(power, *args):
    ''' Return the sum of each argument raised to specified power. power agrument is the first agrument'''
    total=0
    for i in args:
        total+=pow(i,power) #index multiple 3^2+4^2
    print total
    return total


def powersum2(power, **args):
    for name,address in args.items():
        print 'Contact %s at %s' % (name,address)
    return 0

powersum(2,3,4)
powersum(2,10)
db={'Swaroop':'swaroopch@byteofpython.info',
    'Larry':'larry@wall.org',
    'Matsumoto':'matz@ruby-lang.org',
    'Spammer':'spammer@hotmail.com'}
powersum2(db)