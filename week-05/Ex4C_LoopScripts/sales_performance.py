# Sales records
sales_data = [
    ('Marcus Webb', 'East', 4250.00),
    ('Priya Sharma', 'West', 5875.50),
    ('DeShawn Carter', 'East', 3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen', 'West', 4980.25)
]

# Store total sales of all employees
total_sales = 0

# Loop through records
# name, region and sales will automatically be separated into their 
# own variables in the order they appear in the tuple.
for name, region, sales in sales_data:

    print(f"{name} ({region}): ${sales:,.2f}")

    # This will add the employee's sales to the total sales.
    total_sales += sales

    # Checking for top performer
    if sales > 5000:

        print(" ^ Top performer!")

# After the loop finishes, this will print the total sales.
print(f"\nTotal sales across all employees: ${total_sales:,.2f}.")
