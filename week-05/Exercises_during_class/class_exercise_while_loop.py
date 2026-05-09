# Initialize variables
total = 0
count = 0

# Display instructions to the user
print("Enter positive numbers one at a time.")
print("Enter a negative number to stop.")

# Ask user for first number
# Convert the input to an integer
number = int(input("Enter a number: "))

# Loop while the number is positive
while number >= 0:

    # Number entered will get added to total
    total += number

    # If the number is positive, count will increase by 1
    # keep track of how many numbers were entered
    count += 1

    # Ask for another number
    number = int(input("Enter a number: "))

# Display results
print(f"\nNumbers entered: {count}")
print(f"Sum: {total:.2f}")
