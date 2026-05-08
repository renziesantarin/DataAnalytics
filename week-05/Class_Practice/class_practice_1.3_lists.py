# Part 4:
# 1. Use append() to add 6 to the end of the list
# append() will add 6 to the end of the list
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)
# Output: [1, 2, 3, 4, 5, 6]

# 2. Use insert() to add 99 at index 2
# The first number is the index position and the second number is the value that will be added
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 99)
print(my_list)
# Output: [1, 2, 99, 3, 4, 5, 6]

# 3. Use remove() to delete the value 3
# remove() will delete the value from the list
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)
# Output: [1, 2, 4, 5]

# 4. Use pop() to remove and return the item at index 0
# pop() removes an item using the index position
# index 0 is 1, now that value will be stored inside removed_item
my_list = [1, 2, 3, 4, 5]
removed_item = my_list.pop(0)
print(removed_item)
print(my_list)
# Output: 1, and then [2, 3, 4, 5]

# 5. Use sort() to sort the list in ascending order
# I can also use the sorted function but it will be temporary
my_list = [1, 2, 3, 4, 5]
my_list.sort() # this method will make it permanent
print(my_list)
# Output: [1, 2, 3, 4, 5]

# 6. Use reverse() to reverse the list
# reverse() will flip the order of the list
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)
# Output: [5, 4, 3, 2, 1]

# 7. Use index() to find the position of the value 3
# index() searches for the given value inside the list, then returns the index position
my_list = [1, 2, 3, 4, 5]
position = my_list.index(3)
print(position)
# Output: 2

# 8. Use count() to count how many times 3 appears
# count() will check how many times the value appears in the list
my_list = [1, 2, 3, 4, 5]
total = my_list.count(3)
print(total)
# Output: 1

# 9. Use slicing to extract elements from index 1 to 3
# [1:4] means it will start at index 1 and stop before index 4
my_list = [1, 2, 3, 4, 5]
new_list = my_list[1:4]
print(new_list)
# Output: [2, 3, 4]

# 10. Use copy() to create a copy of the list
# copy() will create a new list and new_list becomes a separate copy
my_list = [1, 2, 3, 4, 5]
new_list = my_list.copy()
print(new_list)
# Output: [1, 2, 3, 4, 5]

# 11. Use clear() to remove all items from the list
# clear() removes all items from the list
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)
# Output: []

# Part 5:
# 1. Create a list of 5 student names and sort them alphabetically
# The variable students is storing the list of student names
# sort() arranges them in alphabetical order
students = ["MaoMao", "Jinshi", "Gaoshun", "Suiren", "Basen"]
students.sort()
print(students)
# Output: ['Basen', 'Gaoshun', 'Jinshi', 'MaoMao', 'Suiren']

# 2. Create a nested list to store 3 students and their grades, then access the second student's grade
# I have a list inside the list that contains student name and grade
students = [
    ["Jinshi", 90],
    ["MaoMao", 85],
    ["Basen", 95]
]
print(students[1])
# Output: ['MaoMao', 85]

# 3. Use a for loop to print each item in my_list with its index position
# In the for loop, index stores the position and value stores the item
# and then using enumerate() will get the index position and value
my_list = [1, 2, 3, 4, 5]
for index, value in enumerate(my_list):
    print(index, value)
# Output:
# 0 1
# 1 2
# 2 3
# 3 4
# 4 5

# 4. Check if the value 10 exists in my_list using the in operator
# in operator will check is 10 exists inside the list
my_list = [1, 2, 3, 4, 5]
print(10 in my_list)
# Output: False
