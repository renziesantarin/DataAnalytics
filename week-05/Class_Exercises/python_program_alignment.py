# Ask user for meal cost
meal_cost = eval(input("Enter the cost of the meal: "))

# Calculate tip and tax
tip = meal_cost * 0.20
tax = meal_cost * 0.0825

# Calculate total cost
total = meal_cost + tip + tax

# Display results
print("------ Meal Cost Breakdown ------")

print(f"{'Meal Cost:':<15}${meal_cost:>6.2f}")
print(f"{'Tip (20%):':<15}${tip:>6.2f}")
print(f"{'Tax (8.25%):':<15}${tax:>6.2f}")

print("---------------------------------")

print(f"{'Total Cost:':<20}${total:>6.2f}")