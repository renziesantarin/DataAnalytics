# Starting values
bank_balance = 6500
savings_goal = 15000
weekly_savings = 500

# Check if bank balance is less than the savings goal.
while bank_balance < savings_goal:

    # Add weekly savings to bank balance
    bank_balance += weekly_savings

    # Check if bank balance is at least 75% of the savings goal.
    if bank_balance >= savings_goal * 0.75:

        # This will subtract $30 from the bank balance to represent the treat.
        bank_balance -= 30

        print(f"So close! After treating myself, my balance is up to ${bank_balance}.")

    # Check if bank balance is at least 50% of the savings goal.
    elif bank_balance >= savings_goal / 2:

        print(f"Almost there! This week my balance is up to ${bank_balance}.")

    # If neither of the above conditions are met, print the current balance.
    else:

        print(f"This week my balance increased to ${bank_balance}.")

# Final message once the goal is met.
print(f"Goal met! My current balance is ${bank_balance}.")

