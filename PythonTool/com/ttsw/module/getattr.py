'''
Created on Jun 10, 2014

@author: terrymac
'''

#import statsout

#def output(data, format="text"): 
#     output_function = getattr(statsout, "output_%s" % format) 
#     return output_function(data) 


#if __name__ == '__main__':
#    output('shanghai')

import odbchelper
object = odbchelper
method = 'buildConnectionString'
getattr(object, method)
print getattr(object, method).__doc__ 

def foo():
    '''test foo
    tang'''
    print 2
    
print foo.__doc__
print str(foo)
