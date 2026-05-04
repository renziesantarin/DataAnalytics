# Marenza Santarin
# 5/4/2026


print('Hello world!')

message = 'Hello world!'
print(message)

# It prints twice because the first print statement prints the text directly,
# the second print statement prints the same text stored in the variable.


# Displaying dollars and cents

dollars = 3
cents = 0.50
print(dollars + cents)

# The result shows 3.5 instead of 3.50 because Python is treating it
# like a number and not money formatting.

cents = cents + 0.25
print(dollars + cents)

d_str = '3 dollars'
c_str = '50 cents'

print(d_str + " " + c_str)
