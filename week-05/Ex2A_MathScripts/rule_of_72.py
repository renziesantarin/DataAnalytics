# Rule of 72
# Formula: 
# 72 / interest rate (as a whole number) = years to double

# Rule of 72

current_savings = 5200
interest_rate = 8

years = 72 / interest_rate
doubled_savings = current_savings * 2

print(f"Your current savings is ${current_savings:,.2f}.")
print(f"At a {interest_rate:.0f}% interest rate, your savings account will be worth ${doubled_savings:,.2f} in {years:.1f} years.")