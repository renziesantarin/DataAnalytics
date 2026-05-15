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
        self.number_served = 0
        self.customer_ratings = []
        # Creating new attributes that will keep track of how many customers the restaurant served and collect customer ratings

    # This methods will use the values stored in __init__()
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    # This method has self because it needs to update the specific retaurant object
    # It will ask users to type how many customers were served
    # And then it will add it to the restaurant's running total
    def add_num_served(self):
        customers_today = int(input("How many customers served today?"))
        self.number_served += customers_today

    # This will show the current number of customers served
    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers")

    # This will ask for a rating, save it, calculate the average and then print the result
    def customer_rating(self):

        rating = float(input(
        "How would you rate your experience today on a scale of 1–5 (5 being excellent)? "
        ))

        self.customer_ratings.append(rating)

        average_rating = sum(self.customer_ratings) / len(self.customer_ratings)

        print(f"Your rating was {rating}.")
        print(f"The average rating for this restaurant is {average_rating:.2f}")

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

# This will check the starting customer count. It will run add_num_served() multiple times to 
# add customers served and check if the running total updates properly
restaurant1.print_num_served()
restaurant1.add_num_served()
restaurant1.add_num_served()
restaurant1.print_num_served()

# This will enter the customer ratings and confirm that the restaurant saves the ratings
# and updates the avergae rating after each entry
restaurant1.customer_rating()
restaurant1.customer_rating()
restaurant1.customer_rating()

