'''
This script shows the usage of list, set, tuple, and dictionary
'''

'''
LIST
'''

# assign a list
mylist = ['banana', 'apple', 'durian']
mylist2 = [2,5,6,7]
mylist3 = [2, 5.0, 'halo']

# print a list
# print(mylist)

# print specific member of a list
# print(mylist[2])

# change specific list member
# mylist[1] = 'watermelon'
# print(mylist)

# sort a list
# mylist.sort()
# print(mylist)

'''
TUPLE
'''

# assign a tuple
mytuple = ('faiz', 'ardan', 'fahri')

# try to change tuple
# mytuple[0] = 'nabil'

'''
SET
'''

# assign a set
myset = {'banana', 'apple', 'durian'}

for x in myset:
    print(x)

'''
DICTIONARY
'''

# assign a dictionary
# dictionary = {idKey:Value}
mydict = { "brand": "Ford", "model": "Mustang","year": 1964}
print(mydict["model"])
