# User input
# Use float() since pay rates and hours worked can include decimal values.
pay_rate = float(input("Enter hourly pay rate: "))
hours_worked = float(input("Enter hours worked this week: "))
filing_status = input("Enter filing status (single/joint): ").lower()
# To make sure the user input is consistent, I use lower() to convert the input to lowercase 
# so that it can be compared to the expected values without worrying about case sensitivity.


# This condition checks for overtime
if hours_worked > 40:

    regular_pay = 40 * pay_rate

    overtime_hours = hours_worked - 40

    overtime_pay = overtime_hours * (pay_rate * 1.5)

    gross_pay = regular_pay + overtime_pay

# If employee didn't work overtime
else:

    gross_pay = hours_worked * pay_rate


# Calculate annual income 
# There are 52 weeks in a year
annual_income = gross_pay * 52

# Determine tax rate based on filing status and annual income
if filing_status == "single":

    if annual_income < 12000:
        tax_rate = 0.05

# elif doesn't need >= 12000 because python already knows previous 
# conditions failed, so it only needs to check if it's less than 25000.
    elif annual_income < 25000:
        tax_rate = 0.10

    elif annual_income < 75000:
        tax_rate = 0.15

    else:
        tax_rate = 0.20

elif filing_status == "joint":

    if annual_income < 12000:
        tax_rate = 0.00

    elif annual_income < 25000:
        tax_rate = 0.06

    elif annual_income < 75000:
        tax_rate = 0.11

    else:
        tax_rate = 0.20

else:

    print("Invalid filing status.")
    tax_rate = 0
# For invalid value, this will prevent the program from using an undefined 
# tax_rate variable in the calculations below, which would cause an error.


# Calculate the amount of taxes withheld by multiplying the gross pay by the tax rate.
tax_withheld = gross_pay * tax_rate

# Calculate net pay by subtracting the taxes withheld from the gross pay.
net_pay = gross_pay - tax_withheld

# Print results

print(f"\nYou worked {hours_worked} hours this period.")

print(f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${gross_pay:.2f}.")

print(f"Your filing status is {filing_status}.")

print(f"Your estimated annual income is ${annual_income:,.2f}.")

print(f"Your tax withholding for the week is ${tax_withheld:.2f}")

print(f"Your net pay is ${net_pay:.2f}")
