# Description: This script tests various numeric conversion techniques
# Author: Marenza Santarin

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# a_int = int(a) produces ValueError because int() cannot directly convert a decimal string
a_float = float(a)
a_int = int(float(a))
a_strip = a.strip() # to remove spaces

b_int = int(b)
b_float = float(b)

# c_float = float(c) Again, ValueError
c_slice = c[:3]
c_number = int(c_slice)

d_strip = d.strip()
d_slice = d[-2]
d_number = int(d_slice)

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
