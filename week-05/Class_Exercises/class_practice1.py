# Exercise 1

number1 = 12.0
number2 = 8
sum_result = number1 + number2

print(sum_result)
print(type(sum_result))

# What value was displayed? Is it what you expected? 20.
# What does type() tell you about sum_result? Why does that matter? The result is an integer.
# What happens if you change number1 = 12.0? Does the output change? The result will become a float (20.0).

# Exercise 2

initial_value = 25
reduction = 11

difference = initial_value - reduction
print(difference)

initial_value -= 5
print(initial_value)

initial_value += 10
print(initial_value)

counter = 50

counter += 8
print(counter)

counter -= 3
print(counter)

# What is the difference between initial_value = initial_value - 5 and initial_value -= 5? It is a shorter and cleaner version.
# In what real-life programs might you need to increment or decrement a variable repeatedly? It can be used for inventory tracking or balances.
# What happens if you try: 25 - 'five'? What error appears, and why? Integers and texts can't be mixed.

# Exercise 3

x = 5
y = 2
z = 3

result_a = x * y + z
print(result_a)

result_b = x * (y + z)
print(result_b)

multiplier = 7
multiplicand = 9

product = multiplier * multiplicand
print(product)

item_price = 3.75
quantity = 5

total_cost = item_price * quantity
print(total_cost)

# Why are result_a and result_b different even though they use the same values? Because they follow PEMDAS.
# In a real shopping app, why is it important that multiplication happens before addition? The price and quantity should be calculated first before taxes and fees.
# What would happen if Python evaluated operators strictly left-to-right with no precedence rules? The result would be wrong.

# Exercise 4

numerator = 30
denominator = 6

print(numerator / denominator)
print(numerator // denominator)

denominator = 7

print(numerator / denominator)
print(numerator // denominator)

value = 19
modulus = 4

remainder_val = value % modulus
print(remainder_val)

print(20 % 2)
print(21 % 2)

print(100 // 60)
print(100 % 60)

# When would you choose // over /? Give a concrete programming example. When I only need whole number results, like needing the count of people per group or needing how many hours are left.
# How could you use % to check if a number is even or odd in a program? Using modulo 2.
# What result does 0 % 5 give? What about 5 % 5? Can you form a rule? If a number can be divided evenly with nothing left over, the result of using % will be 0.

# Exercise 5

