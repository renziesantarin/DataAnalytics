# Product Pricing Calculator
# Marenza Santarin
# 5/16/2026

# User input
product_name = input("Enter product name: ")
category = input("Enter category: ")
price = float(input("Enter original price: $"))
discount = float(input("Enter discount percentage: "))
tax_rate = float(input("Enter tax rate percentage: "))

# Lambda functions:
# To get the discount, it needs 2 values: price and percentage (pct)
# This formula takes the full price and keeps what is left after the discount is applied
apply_discount = lambda price, pct: price * (1 - pct / 100)
# To add the tax, it needs 2 values: price and the tax rate
# This formula will add the tax on top of the price
# The 1 means the original 100% of the price, the rate / 100 is the tax percentage changed into a decimal
apply_tax = lambda price, rate: price * (1 + rate / 100)
# This chains the first 2 lambdas together, it applies the discount and then applies the tax
final_price = lambda price, disc, tax: apply_tax(apply_discount(price, disc), tax)

# Calculations:
# The value here is the price after the discount but before tax
discounted = apply_discount(price, discount)
# The value here is the discounted price after the tax
taxed = apply_tax(discounted, tax_rate)
# The value here is the original price, applied discount and tax
total = final_price(price, discount, tax_rate)
# This will calculate how much money was saved because of the discount
savings = price - discounted

# Pricing Report
print(f"""
======== PriceIQ Pricing Breakdown ========
Product Name : {product_name}
Category     : {category}
-------------------------------------------
Original Price     : ${price:,.2f}
Discount ({discount:.0f}%)     : -${savings:,.2f}
Discounted Price   : ${discounted:,.2f}
Tax ({tax_rate:.0f}%)           : +${taxed - discounted:,.2f}

Final Price        : ${total:,.2f}
""")
