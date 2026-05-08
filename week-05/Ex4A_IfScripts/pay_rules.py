# Variables for pay rate and hours worked
pay_rate = 17.30
hours_worked = 45

# Checking for overtime
if hours_worked > 40:

# this stores the pay for the first 40 hours by multiplying to pay rate
    regular_pay = 40 * pay_rate

# this stores the additional hours after subtracting it from the regular 40 hours
    overtime_hours = hours_worked - 40

# this stores the overtime pay after multiplying the overtime hours to overtime pay rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)

# this stores the total pay after adding regular and overtime pay
    gross_pay = regular_pay + overtime_pay

else:
    gross_pay = hours_worked * pay_rate

# Print results
print(f"{'Pay rate:':<18} ${pay_rate:.2f}")
print(f"{'Hours worked:':<18} {hours_worked}")
print(f"{'Gross pay:':<18} ${gross_pay:.2f}")

