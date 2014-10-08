'''
Created on Jun 10, 2014

@author: terrymac
'''


a=[1,2,4,2,4,5,7,10,5,5,7,8,9,0,3]
a.sort()
# the last value
last=a[-1]
print last
index=len(a)-2
print index
# reverse range list
for i in range(index,-1,-1):
    if last==a[i]:
        del a[i]
    else:
        last=a[i]
    print(a)
