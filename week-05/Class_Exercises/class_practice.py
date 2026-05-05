# Indexing and Slicing

string = "Hello, World!"

print(string[0]) # Output H
print(string[-1]) # Output !
print(string[1:4]) # Output ell

# Concatenation

greeting = "Hello, " + "World!"
print(greeting)

# Class Exercise:

name1 = "Chantal Lee"
name2 = "Dimitri Nji"
name3 = "Vesna Cari"

print(f"Names of three classmates: {name1}, {name2}, {name3}")

# Importing math module

import math

print(f'Pi value: {math.pi:.2f}')

# Using input and type casting

name = input("Enter your name: ")
print(f"Hello {name}")

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number: "))

print(f'You have entered {num1} and {num2}')

print(type(num1))
print(type(num2))

print(f'The sum of {num1} and {num2} is {num1+num2}')
print(f'The product of {num1} and {num2} is {num1*num2}')
print(f'The product of 2 and {num2} is {2*num2}')


