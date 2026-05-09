# Assign values
a = 13
b = 22
c = 8

# Check which number is smallest
# After the condition is checked, the smallest variable will store the value of the smallest number
if a <= b and a <= c:

    smallest = a

elif b <= a and b <= c:

    smallest = b

else:

    smallest = c

# Check which number is largest
# After the condition is checked, the largest variable will store the value of the largest number
if a >= b and a >= c:

    largest = a

elif b >= a and b >= c:

    largest = b

else:

    largest = c

# Print results using the value stored in smallest and largest
print(f"The smallest number is {smallest}")
print(f"The largest number is {largest}")
