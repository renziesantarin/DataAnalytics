# Exercise 1: Average

# Getting username:
name = input("Enter your name: ")

# Get the three numbers:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Calculate average:
average = (num1 + num2 + num3) / 3

# Display the result with 2 decimal places
print(f"Hello {name}! The average of {num1}, {num2} and {num3} is: {average:.2f}")
