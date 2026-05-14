# Writing to a file
with open("students.txt", "w") as file:
    file.write("Alice\n")
    file.write("Bob\n")

# Reading from a file
with open("students.txt", "r") as file:
    content = file.read()
    print(content)

#Open file for reading
'''
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
'''
# FileNotFoundError: because it doesn't exist yet.

# Open file for writing
with open("example.txt", "w") as file:
    file.write("Hello, Python!")

# Append text to the file
with open("example.txt", "a") as file:
    file.write("\nNew line added.")

# Create new file
with open("newfile.txt", "w") as file:
    file.write("This file was created.")

# Read and write to the same file
with open("example.txt", "r+") as file:
    content = file.read()
    print(content)

    file.write("\nAdditional text.")

# Reopen and print updated file
with open("example.txt", "r") as file:
    print(file.read())
