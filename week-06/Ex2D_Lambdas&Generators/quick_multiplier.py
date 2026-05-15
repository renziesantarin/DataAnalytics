# Ex2D Lamdas & Generators
# Lab 1 Quick Multiplier

# This creates a function and stores it inside the variable 'doubler' that takes in a number and multiplies it by 2
doubler = lambda n: n * 2

# This calls the doubler and gives it the number 8 which will be multiplied by 2 and printed
print(doubler(8))
# This calls the doubler and gives it the number -4 which will be multiplied by 2 and printed
print(doubler(-4))
# This calls the doubler and gives it the string "banana" which will be repeated twice and printed
print(doubler("banana"))

# This creates a function and stores it inside the variable 'tripler' that takes in a number and multiplies it by 3
tripler = lambda n: n * 3

# This calls the tripler and gives it the number 8 which will be multiplied by 3 and printed
print(tripler(8))
# This calls the tripler and gives it the number -4 which will be multiplied by 3 and printed
print(tripler(-4))
# This calls the tripler and gives it the string "banana" which will be repeated three times and printed
print(tripler("banana"))

# This creates a function called 'multiplier' that takes in a number and returns a lambda function that multiplies its input by that number
# The purpose of this function is to help create other multiplier functions without rewriting the lambda again and again
def multiplier(number):
    return lambda n: n * number

# Multiplier variables for numbers 4 through 10
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

# Print tests for the multiplier functions for numbers 4 through 10 using the number 5 as the input to be multiplied
print(quadrupler(5))
print(quintupler(5))
print(sextupler(5))
print(septupler(5))
print(octupler(5))
print(nonupler(5))
print(decupler(5))

