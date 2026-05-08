# Creating two tuples: Candy types and flavors
candies = ("Lollipops", "Gummies", "Bon Bons")
flavors = ("Lemon", "Strawberry", "Raspberry")

# Candy combinations
candy_combinations = set()

candy_combinations.add(f"{flavors[0]} {candies[0]}")
candy_combinations.add(f"{flavors[1]} {candies[1]}")
candy_combinations.add(f"{flavors[2]} {candies[2]}")

# Display results
print("Today's candy options include:")
print(candy_combinations)

# Output:
# Today's candy options include:
# {'LemonLollipops', 'Strawberry Gummies', 'Raspberry Bon Bons'}