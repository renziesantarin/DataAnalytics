# iterate with for loop

my_set = {"Alice", "Bob", "Charlie"}

for item in my_set:
    print(item)

# Membership test

my_set = {1, 2, 3, 4, 5}

print(3 in my_set)
print(9 in my_set)

my_list = list(my_set)
print(my_list[2])

# covert to a sorted list
my_set = {1, 2, 3, 4, 5}

my_list = sorted(my_set)
print(my_list[2])

# Unpacking
my_set = {1, 2, 3, 4, 5}

a, b, c, d, e = my_set
print(a, b, c, d, e)