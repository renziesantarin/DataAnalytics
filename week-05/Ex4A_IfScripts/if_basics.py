# Starting variables
x = 100
y = 20

# Part A
# this checks if 100/20 is equal to 5
if x / y == 5:
    print("x divided by y is 5")
    x = 1
else:
    print("are the variables set up correctly?")
# Output: x divided by y is 5 because the condition is true

# Part B
# this checks if 1 * 20 is equal to 20
if x * y == y:
    print("now x times y is y")
    x = 10
else:
    print(f"Whoops, x equals {x}")
# Output: now x times y is y because the condition is true

# Part C
# this checks if 10 < 20
if x < y:
    print("x is less than y")
    x = x * 2
else:
    print("uh oh, x is not less than y")
# Output: x is less than y because the condition is true

# Part D
# this checks if 20 > 20
if x > y:
    print("how is x greater than y??")
else:
    print("x is NOT greater than y")
# Output: x is NOT greater than y / else ran because the if condition is false

# Final output
# this prints the final value set for x and y after all the updates
print(f"The final value of x is {x} and the final value of y is {y}.")

