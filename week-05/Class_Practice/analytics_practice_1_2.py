# ======================================================
# Class Practice Exercise 1.2 -- Data Analytics
# Name: Marenza Santarin
# Date: 5/7/2026
# Course: Data Analytics
# File: analytics_practice_1_2.py
# Topic: Python statistics library & descriptive stats
# ======================================================

# -- Exercise 1: Import Styles -------------------------------------------

# These two are importing the whole module
# Importing the whole module I will need to use module.function()
import statistics
import math

# This will only import specific function
# Here I can use the function without the module name
from statistics import mean, median

# This will rename it to stats
# Using alias is good because its shorter to type but is less clear to other people
import statistics as stats

print("Exercise 1 -- Import Styles")

# This will access the pi value inside the math module
print("math.pi =", math.pi)

# This is calling the square root function from the math module
print("sqrt(144) =", math.sqrt(144))

# This uses the mean function from the statistics module
print("Mean (full module): ", statistics.mean([10, 20, 30]))

# This will do the same but since the function was imported directly, statistics doesn't need to be added
print("Mean (from import): ", mean([10, 20, 30]))

# This will do the same but statistics is now using the alias stats
print("Mean (alias stats): ", stats.mean([10, 20, 30]))

print("All three return the same result -- different styles, same function!")


# -- Exercise 2: Central Tendency -- Sales Data --------------------------

import statistics

# Monthly sales list
monthly_sales = [42, 55, 61, 48, 73, 58, 66, 51, 70, 63, 55, 80]

# Using the mean function to get average value
# This can be affected by very high or low values
sales_mean = statistics.mean(monthly_sales)

# Using the median function to get the middle value
# This is useful to check for outliers
sales_median = statistics.median(monthly_sales)

# Using the mode function to get the most common value
sales_mode = statistics.mode(monthly_sales)

print("Exercise 2 -- Sales Central Tendency")

print(f"Dataset: {monthly_sales}")

# Getting the length/count of the items in monthly_sales
print(f"{'Count:':<8} {len(monthly_sales)} months")

# Using :.2f to display as a float with 2 decimal places to get the expected output
print(f"{'Mean:':<8} ${sales_mean:.2f}k (average monthly sales)")

print(f"{'Median:':<8} ${sales_median}k (middle-ranked month)")

print(f"{'Mode:':<8} ${sales_mode}k (most frequent sales figure)")

if sales_mean > sales_median:
    print("Insight: Mean > Median -- a high-sales month is pulling the average up.")

elif sales_mean < sales_median:
    print("Insight: Mean < Median -- a low-sales month is dragging the average down.")

else:
    print("Insight: Mean equals Median -- data is likely symmetric.")
