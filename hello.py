# tuple
my_tuple = (1, 2, 3)
print(my_tuple)

my_tuple = (1, 2, 2, 2, 3, 4, 5)
my_tuple = my_tuple[0:3] # slicing a tuple creates a new tuple
print(my_tuple.extend([6, 7, 8])) # tuples do not have an extend method, so this will raise an error
print(my_tuple.append(9)) # tuples do not have an append method, so this will raise an error
print(my_tuple[0]) # tuples are indexed, so we can access individual elements
print(my_tuple.pop()) # tuples do not have a pop method, so this will raise an error
print(my_tuple + (6, 7, 8)) # tuples can be concatenated to create a new tuple

# set
my_set = {1, 2, 3}
print(my_set)
print(my_set.append(4)) # sets do not have an append method, so this will raise an error
print(my_set.extend([5, 6, 7])) # sets do not have an extend method, so this will raise an error
print(my_set[0]) # sets are not indexed, so this will raise an error

my_set = {1, 2, 2, 3, 4, 5}
print(my_set) # sets do not allow duplicates, so the second 2 is ignored