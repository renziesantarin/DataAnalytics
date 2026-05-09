# Python set

# unordered
my_set = {3, 1, 2}
print(my_set)

# no duplicates
my_set = {1, 2, 3, 3, 3, 3}
print(my_set)

# mutable
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

# mutable
my_set = {1, 2, 3} 
my_set.remove(2) # will remove the value since it's not indexed
print(my_set)

# mutable
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)

# iteration
my_set = {1, 2, 3}
for item in my_set:
    print(item)

# unindexable
my_set = {1, 2, 3}
print(my_set[0]) # will give an error since sets does not have an index
