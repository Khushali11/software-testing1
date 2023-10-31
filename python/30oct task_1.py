# find max and min in the tuple
my_tuple = (15, 8, 25, 36, 42, 10)
print(my_tuple, type(my_tuple))

print("maximum nuber:", max(my_tuple))
print("minimum number:", min(my_tuple))
# find insertion and union of two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print("insertion of the sets:", set1.intersection(set2))
print("union of the sets:", set1.union(set2))
# Remove duplicate element inthe list
my_list = [1, 2, 2, 3, 4, 4, 5]
list2 = []
for i in my_list:
    if i not in list2:
        list2.append(i)

print(my_list,list2)
print(list(set(my_list)))
from collections import OrderedDict
print(list(OrderedDict.fromkeys(my_list)))
#remove a key value pair fron the dictionary
dict1={"anal":116,"bavya":123,"vaishvi":102}
print(dict1)
dict1['diya']= '145'# add items
print(dict1)
print(dict1.get('bavya'))# get value
del(dict1['anal'])# remove key value
print(dict1)
print(dict1.keys())# get keys
print(dict1.values())#get value
print(dict1.items())# get key value in tuple
dict1.popitem()
print("after popitem remove last add item:",dict1)
dict1.update({3:'vivan'})
print("after update 3:", dict1)
dict1.pop(3)
print("after pop 3:",dict1)
