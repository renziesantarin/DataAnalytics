# Ask the user for a number
# Convert to int to do comparisons
day = int(input("Enter a number from 1 to 7: "))

# Determine/assign the number of the weeks
# Use if and elif to check conditions
# If true it will skip the rest of the conditions and print the day of the week
if day == 1:
    print("Monday")

elif day == 2:
    print("Tuesday")

elif day == 3:
    print("Wednesday")

elif day == 4:
    print("Thursday")

elif day == 5:
    print("Friday")

elif day == 6:
    print("Saturday")

elif day == 7:
    print("Sunday")

# If none of the conditions matched, the number is invalid so an error message should be displayed
else:
    print("Error: Please enter a number between 1 and 7.")

