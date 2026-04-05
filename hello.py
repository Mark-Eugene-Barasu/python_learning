# list = used to store multiple items in a single variable
# list is one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usages.
# lists are created using square brackets: []
# list items are ordered, changeable, and allow duplicate values.
# list items are indexed, the first item has index [0], the second item has index [1] etc.

# create a list
mylist = ["apple", "banana", "cherry"]
print(mylist)
# access list items
print(mylist[0])  # prints "apple"
print(mylist[1])  # prints "banana"
print(mylist[2])  # prints "cherry"
# change list items
mylist[1] = "orange"
print(mylist)  # prints ["apple", "orange", "cherry"]
# add list items
mylist.append("grape")
print(mylist)  # prints ["apple", "orange", "cherry", "grape"]
# remove list items
mylist.remove("orange")
print(mylist)  # prints ["apple", "cherry", "grape"]
# loop through a list
for item in mylist:
    print(item)
# check if an item is in a list
if "apple" in mylist:
    print("Yes, 'apple' is in the list")
# get the length of a list
print(len(mylist))  # prints 3
# clear a list
mylist.clear()
print(mylist)  # prints []
