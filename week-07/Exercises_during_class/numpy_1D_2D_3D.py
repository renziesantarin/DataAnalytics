import numpy as np

# 1D array
arr1 = np.array([1, 2, 3])
# This is just straight row of values

# 2D array
arr2 = np.array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
])
# This is like a table with rows and columns

# 3D array
arr3 = np.array([
    [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ],
    [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ],
    [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ]
])
# This is like having multiple 2D tables stack together
# Each inner section is one layer

print("1D Array:")
print(arr1)

print("\n2D Array:")
print(arr2)

print("\n3D Array:")
print(arr3)
