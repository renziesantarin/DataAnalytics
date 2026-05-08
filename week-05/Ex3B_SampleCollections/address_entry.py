# Dictionary with contact information
contact_info = {
    "name": "MaoMao Kan",
    "address": "123 Outer Court",
    "city": "Imperial Palace",
    "state": "Li",
    "zip": "12345"
}

# Prints the formatted mailing address
# Using triple quotes to print on multiple lines just like how it's formatted for mailing
print(f"""
{contact_info["name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}
""")

# Removes the name key:value pair
contact_info.pop("name")

# New variable for full name and assign two key:value pairs
full_name = {
    "first name": "MaoMao",
    "last name": "Kan"
}

# Add key:value honorific
full_name.update({"honorific": "Ms."})

# full_name added to contact_info dictionary
contact_info.update({"full_name": full_name})

# Prints the updated mailing address
# Using triple quotes to print on multiple lines just like how it's formatted for mailing
print(f"""
{contact_info["full_name"]["honorific"]} {contact_info["full_name"]["first name"]} {contact_info["full_name"]["last name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}
""")
