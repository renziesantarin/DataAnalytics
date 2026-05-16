# Exercise 4.B Working with exceptions
# Lab 1


print("===== ValueError Example =====")
try:
    age = int("Hello")

except ValueError:
    print("ValueError: Oops, looks like you entered text instead of a number.")

else:
    print(age)

finally:
    print("Let's try another one...\n")
# Trying to convert "Hello" to an integer, but it is not a number
# Instead of crashing, except ValueError catches the error and shows a friendly message

print("===== NameError Example =====")
try:
    favorite_anime = Frieren

except NameError:
    print("NameError: Oops, looks like this variable was never defined.")

else:
    print(favorite_anime)

finally:
    print("Let's try another one...\n")
# The program sees Frieren, but since it was never defined (pizza = something)
# the program throws NameError

print("===== TypeError Example =====")
try:
    result = "8" + 18

except TypeError:
    print("TypeError: Oops, looks like you mixed incompatible data types.")

else:
    print(result)

finally:
    print("Let's try another one...\n")
# A string and an integer cannot be added/calculated that's why
# the program will throw TypeError

print("===== SyntaxError Example =====")
try:
    raise SyntaxError("Missing colon.")

except SyntaxError:
    print("SyntaxError: Oops, looks like Python syntax is incorrect.")

else: print("No error occured.")

finally:
    print("Let's try another one...\n")
# Syntax error is tricky because python catches it before running the code
# The normal try-except often will not catch it
# Using raise will manually creates the error

