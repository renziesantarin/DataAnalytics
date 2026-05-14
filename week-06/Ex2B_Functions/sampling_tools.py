# Importing the random module to perform various random operations.
import random

# List of products available.
products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam', 'Headset', 'Docking Station',
            'USB Hub', 'Desk Lamp', 'Surge Protector']

# Selecting one random item from products list to be stored in the variable product_of_the_day.
product_of_the_day = random.choice(products)
print("Product of the day:", product_of_the_day)

# Selecting 3 different products. The same product will not be picked twice because sample() chooses without replacement.
survey_products = random.sample(products,3)
print("Products selected for survey:", survey_products)

# This will rearrange the original list into a random order. The shuffle() function modifies the list in place and does not return a new list.
random.shuffle(products)
print("Shuffled product list:", products)

# This will generate a random integer between 50 and 300.
transaction_count = random.randint(50, 300)
print("Transaction count:", transaction_count)

