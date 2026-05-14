# Ex2C Lab 2 More Functions

# FIRST FUNCTION:
# Defining the dunction 'display_mailing_label' that takes in 5 parameters and prints them in a mailing label format
def display_mailing_label(name, address, city, state, zip_code):
    print(name)
    print(address)
    print(city + ", " + state + " " + zip_code)

# Calling the function with the appropriate arguments to display the mailing label
display_mailing_label("SpongeBob SquarePants", "124 Conch Street", "Bikini Bottom", "Pacific Ocean", "12345")
print("\n")  # Adding a newline for better readability
display_mailing_label("Patrick Star", "123 Conch Street", "Bikini Bottom", "Pacific Ocean", "12345")

print("\n")  # Adding a newline for better readability

# SECOND FUCNTION:
# Defining the function 'add_numbers' that takes in a variable number of arguments and prints the sum of those numbers in an equation format
def add_numbers(*numbers):
    total = sum(numbers)
    equation = " + ".join(str(num) for num in numbers)
    print(f"{equation} = {total}")

# Calling the function with the appropriate arguments to display the sum of the numbers
add_numbers(18)
print("\n")  # Adding a newline for better readability
add_numbers(22, 13)
print("\n")  # Adding a newline for better readability
add_numbers(1, 2, 3, 4, 5)

print("\n")  # Adding a newline for better readability

# THIRD FUNCTION:
# Defining the function 'display_receipt' that takes in two parameters and calculates the change due or remaining balance
def display_receipt(total_due, amount_paid):
    change_due = amount_paid - total_due
    print(f"Total Due: ${total_due:,.2f}")
    print(f"Amount Paid: ${amount_paid:,.2f}")

    # If amount due is greater than amount paid, this will print the change due
    if amount_paid > total_due:
        print(f"\nChange Due: ${change_due:,.2f}")
        
    # If amount due is equal to amount paid, this will print that there is no change due
    elif amount_paid == total_due:
        print(f"\nChange Due: $0.00")

    # If amount due is less than amount paid, this will print the remaining balance
    else:
        remaining_balance = total_due - amount_paid
        print(f"\nRemaining Balance: ${remaining_balance:,.2f}")

# Calling the function with the appropriate arguments to display the receipt and change due or remaining balance
display_receipt(80.00, 85.00)
print("\n")
display_receipt(80.00, 80.00)
print("\n")
display_receipt(80.00, 75.00)

