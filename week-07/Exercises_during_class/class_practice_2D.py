import numpy as np

arrA = np.array([
    [11, 12, 13], # first row of the 2D array
    [14, 15, 16]  # second row of the 2D array
])
# There are 3 columns

print(arrA)
# This will print the whole 2D array

# This loop will go through each row, then multiplying by 2 and print them
for row in arrA:
    print(row * 2)

    # This second loop will grab each row and print it and then get each element
    # and the result variable will calculate it multiplying by 2 and hold the result
    for element in row:
        loop_result = element * 2
        print(loop_result)
        # This will print the result multplied by 2
        