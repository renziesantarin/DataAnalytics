# Ask user for department code
dept_code = int(input("Please enter department code here: "))

# Validation
# Keep asking if code is invalid
while dept_code not in [1, 5, 10, 12, 18, 20]:

    print("Invalid department code.")

    dept_code = int(input("Please enter a valid department code: "))

# Determine/assign department name
# Use if and elif to check conditions
# If true it will skip the rest of the conditions and assign the department name to the variable "department"
if dept_code == 1:
    department = "Marketing"

elif dept_code == 5:
    department = "Human Resources"

elif dept_code == 10:
    department = "Accounting"

elif dept_code == 12:
    department = "Legal"

elif dept_code == 18:
    department = "IT"

elif dept_code == 20:
    department = "Customer Relations"

# Print result
print(f"Department code {dept_code} is {department}.")
