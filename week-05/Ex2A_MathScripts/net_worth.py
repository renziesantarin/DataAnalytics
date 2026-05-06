# a. What are “assets” that would need to be included in this calculation? What about “debts”?
# I would include checking, savings and car value. For debts, it can be a credit card debt or student or medical loan.

# b. Formula to calculate net worth:
# assets - debts = net worth

# assets
checking = 1500
savings = 4000
car_value = 12000

# debts
credit_card_debt = 700
student_loans = 3000

# calculations
total_assets = checking + savings + car_value
total_debts = credit_card_debt + student_loans
net_worth = total_assets - total_debts

# results
print(f"Your total assets are ${total_assets:,.2f}")
print(f"Your total debts are ${total_debts:,.2f}")
print(f"Your net worth is ${net_worth:,.2f}")
