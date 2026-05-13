# Sales Summary Exercise
# Marenza Santarin
# 5/12/2026

# Collecting user input for sales summary
name = input("Associate name: ")
region = input("Store region: ")
# Converting input to integer for calculations
units_sold = int(input("Units sold: "))
# Converting input to float for calculations and because prices usually has decimal points
price = float(input("Price per unit: $")) 

# Defining a function with 4 parameters to calculate revenue and bonus
def sales_summary(name, region, units_sold, price):
    revenue = units_sold * price
    bonus = revenue * 0.10
    return revenue, bonus
# Return will send the calculated revenue and bonus out of the function to be used in 
# the main program in the print statement

 
# Calling the function and storing the returned values in variables
revenue, bonus = sales_summary(name, region, units_sold, price)

# Displaying results formatted based on the exercise expected output
print(f"""
      ====== RetailEdge Inc. - Sales Summary ======
      Associate Name : {name}
      Store Region   : {region}
      Units Sold     : {units_sold}
      Price per Unit : ${price:,.2f}
      ---------------------------------------------
      Total Revenue  : ${revenue:,.2f}
      Bonus (10%)    : ${bonus:,.2f}
      =============================================
      """)
