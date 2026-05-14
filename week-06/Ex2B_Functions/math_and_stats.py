# Importing 3 modules
import random
import math
import statistics

# --------------------------------------------
# Starting variables

# This creates a range of numbers that includes 1 to 99
vals_1_100 = range(1,100)

# This creates a list of 75 unique numbers randomly selected from the range of 1 to 99
vals_sample = random.sample(vals_1_100, 75)

# This creates a list of 200 numbers randomly selected from the range of 1 to 99, allowing for duplicates
vals_choices = random.choices(vals_1_100, k = 200) 

# This generates a random integer between 3 and 10 to be used as the radius for the area of a  circle
radius = random.randint(3,10) 

# Storing the value of pi from the math module in a variable for later use
pi = math.pi 

# --------------------------------------------
# Subset of integers 1-100 calculations:

# This variable stores the sum of the 75 numbers in the vals_sample list
sample_sum = sum(vals_sample) 

# This variable stores the average of the numbers in the vals_sample list
sample_average = statistics.mean(vals_sample) 

# This variable stores the middle value of the numbers in the vals_sample list
sample_median = statistics.median(vals_sample) 

# --------------------------------------------
# Superset of 200 values, integers 1-100 calculations:

# This variable stores the average valueof the 200 random numbers in the vals_choices list
choices_average = statistics.mean(vals_choices) 

# This variable stores the middle value in the vals_choices list
choices_median = statistics.median(vals_choices) 

# This variable stores the most common value in the vals_choices list
choices_mode = statistics.mode(vals_choices) 

# This variable stores the standard deviation (how spread out the number are) in the vals_choices list
choices_stdev = statistics.stdev(vals_choices) 

# This variable stores the variance (how different the numbers are from the average) in the vals_choices list
choices_variance = statistics.variance(vals_choices)

# --------------------------------------------
# Modeling a random circle calculations:

# This variable stores the area of a circle with the randomly generated radius, using the formula A = pi * r^2
circle_area = pi * (radius ** 2)

# ceil() is a function from the math module that rounds a number up to the nearest whole number.
rounded_up = math.ceil(circle_area)

# floor() is a function from the math module that rounds a number down to the nearest whole number.
rounded_down = math.floor(circle_area)

# --------------------------------------------
# Final print statements for calculations:
print("_Experimenting with a subset of integers 1-100:")
print("Sum of 75 sample values from 1 to 100:", sample_sum)
print("Average of 75 sample values:", round(sample_average, 2))
print("Median of 75 sample values:", sample_median)

print('/n')

print("_Experimenting with a superset of 200 values, integers 1-100:")
print("Average of 200 values:", round(choices_average, 2))
print("Median of 200 values:", choices_median)
print("Mode of 200 values:", choices_mode)
print("Standard deviation of 200 values:", round(choices_stdev, 2))
print("Variance of 200 values:", round(choices_variance, 2))

print('/n')

print("_Modeling a random circle:")
print("Radius =", radius, ", area =", rounded_up, "(rounded up to the nearest integer)")
print("Radius =", radius, ", area =", rounded_down, "(rounded down to the nearest integer)")
