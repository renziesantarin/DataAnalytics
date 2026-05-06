import math

people = 38

vans = math.ceil(people / 15)

total_cost = vans * 250
cost_per_person = total_cost / people

print(f"Vans needed: {vans}")
print(f"Total cost: ${total_cost:,.2f}")
print(f"Cost per person: ${cost_per_person:,.2f}")

# There is leftover money because I rounded up the total cost for 3 vans but the cost per person is split exactly
