# Ask user for department code
dept_code = int(input("Please enter department code here: "))

# Validation
# Keep asking while code is invalid
while dept_code not in [1, 5, 10, 12, 18, 20]:

    print("Invalid department code.")

    dept_code = int(input("Please enter a valid department code: "))

# Match department code
# If true it will skip the rest
# I don't need to use case_: as the default since I have a while loop that will only allow valid codes to be entered
match dept_code:

    case 1:
        department = "Marketing"

    case 5:
        department = "Human Resources"

    case 10:
        department = "Accounting"

    case 12:
        department = "Legal"

    case 18:
        department = "IT"

    case 20:
        department = "Customer Relations"

# Print result
print(f"Department code {dept_code} is {department}.")

