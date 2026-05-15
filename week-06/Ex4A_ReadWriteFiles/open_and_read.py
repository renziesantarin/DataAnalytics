# Open the file in read mode
f = open("about_me.txt", "r")

# Read and print the whole file
# print(f.read()) 0) Changing to f.read(50)
# print(f.read(50))
# print(f.read(50))
# After it reads the first 50 characters, it continued from where it left off in the next line

# print(f.readline(10))
# print(f.readline())
# This does the same thing, continues after where it left off

# This runs the loop 4 times
# Each time the loop runs, it reads one line from the file
# for i in range(1, 5):
#     print(f.readline())

# print(f.readlines(1))
# print(f.readlines(1))
# print(f.readlines(10))
# print(f.readlines(100))
# print(f.readlines(-1))
# This returns a list [] of lines and then it has \n (line break) at the end of that line

first_50 = f.read(50)

# This is creating a empty list to store the next few lines
next_four_lines = []

# Each time, it reads one line and adds that line to the list
for i in range(1,5):
    next_four_lines.append(f.readline())

next_100_lines = f.readlines(100)

# Printing the following:
print(f"First 50 characters: {first_50}")
print(f"Next four lines, as list by line: {next_four_lines}")
print(f"Next 100 characters, as list by line, rounded up to complete lines: {next_100_lines}")

# Close file manually
f.close
