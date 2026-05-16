# Weekly Sales Statistics Analyzer
# Marenza Santarin
# 5/16/2026

import statistics as stats

# User input
analyst = input("Analyst name: ")
region = input("Region: ")

# Prints instructions for the user
# The for loop is repeating 7 times because we need to collect sales for 7 days
# Using i + 1 to start the range to 1 instead of 0
print("Enter daily sales for 7 days (one per line): ")
sales = [float(input(f"Day {i+1}: $")) for i in range(7)]

# Defining function:
def analyze_sales(analyst, region, sales):
    mean = stats.mean(sales)
    median = stats.median(sales)
    mode = stats.mode(sales)
    stdev = stats.stdev(sales)
    revenue = sum(sales)
    highest = max(sales)
    lowest = min(sales)
    return mean, median, mode, stdev, revenue, highest, lowest
# return sends all the answers back out of the function from when the function gets called

# Unpacking multiple return values:
mean, median, mode, stdev, revenue, highest, lowest = analyze_sales(analyst, region, sales)

# Multi-line formatted print statement
print(f""""
================ Weekly Sales Statistics Report ================
Analyst: {analyst}
Region : {region}
Sales  : {sales}
----------------------------------------------------------------
Total Revenue: ${revenue:,.2f}
Mean (Avg)   : ${mean:,.2f}
Median       : ${median:,.2f}
Mode         : ${mode:,.2f}
Std deviation: ${stdev:,.2f}
Highest day  : ${highest:,.2f}
Lowest day   : ${lowest:,.2f}
================================================================
""")
