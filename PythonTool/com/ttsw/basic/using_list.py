
#!/usr/bin/python
# Filename: using_list.py

'''
Created on Jun 1, 2014

@author: terrymac
'''

#This is my shopping list
shopinglist=['apple','mango','carrot','banana']

print 'I have',len(shopinglist),'items to purchase.'

print 'These items are:',
for item in shopinglist:
    print item
    
print '\n I also have to buy rice.'
shopinglist.append('rice')
print 'My shopinglist is now',shopinglist

shoppinglist2=['banana','test']

shopinglist.append(shoppinglist2)
print 'My shopinglist and shopinglist2 is now',shopinglist

shoppinglist3=['banana3','test3']

shopinglist.extend(shoppinglist3)
print 'My shopinglist and shopinglist3 is now',shopinglist

shopinglist.remove(shoppinglist2)
print 'My shopinglist and shopinglist4 is now',shopinglist

print'I will sort my list now' 
shopinglist.sort()
print 'Sorted shopping list is', shopinglist

print 'The first item I will buy is',shopinglist[0]
olditem=shopinglist[0]
del shopinglist[0]
print 'I bought the ',olditem
print 'My shoppinglist is now',shopinglist
