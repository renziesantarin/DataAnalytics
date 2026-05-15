# Ex 3.A Working with classes
# 5/15/2026

# Creating a class called Restaurant that has two attributes: rest_name and food_type
class Restaurant:
    """Represents a restaurant and the type of food it serves."""
    def __init__(self, rest_name, food_type):
        # The 2 parameters in the __init__ method are used to initialize the attributes of the Restaurant class
        # The rest_name and food_type attributes will be set based on the arguments passed when creating the instance
        self.rest_name = rest_name
        self.food_type = food_type

    # This methods will use the values stored in __init__()
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

# Creating 3 instances of the class for different types of restaurants
# Restaurant() calls the class and creates a new object from the class blueprint
# Each variable will remember its name and food type
restaurant1 = Restaurant("The Krusty Krab", "Burgers & Fries")
restaurant2 = Restaurant("Sun Bakery", "Pastries")
restaurant3 = Restaurant("Ramen Ichiraku", "Japanese Ramen")

# Calling the describe_rest() and rest_open() methods to call each object to use its saved info
restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()
