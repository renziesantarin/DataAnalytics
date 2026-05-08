# Description: This script tests various numeric conversion techniques
# Author: Marenza Santarin

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# a_int = int(a) produces ValueError because int() can only convert whole numbers
# Converting to a float
a_float = float(a)
# Converting to int by converting to float first
a_int = int(float(a))
# Using .strip() to remove spaces
a_strip = a.strip()

# Converting b to integer
b_int = int(b)
# Converting b to float
b_float = float(b)

# c_float = float(c) Again, ValueError because it contains letters
# Taking only the number part
c_slice = c[:3]
# Converting the sliced value into integer
c_number = int(c_slice)

# Using .strip() to remove spaces
d_strip = d.strip()
# Taking only the number part
d_slice = d[-2] #
# Converting the sliced value into integer
d_number = int(d_slice)

# Print results and data types
print(a, type(a))
print(a_float, type(a_float))
print(a_int, type(a_int))
print(a_strip, type(a_strip))

print(b, type(b))
print(b_int, type(b_int))
print(b_float, type(b_float))

print(c, type(c))
print(c_slice, type(c_slice))
print(c_number, type(c_number))

print(d, type(d))
print(d_strip, type(d_strip))
print(d_slice, type(d_slice))
print(d_number, type(d_number))
