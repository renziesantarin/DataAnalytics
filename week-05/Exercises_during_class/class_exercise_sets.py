# Create a set of U.S. states
states = {"Texas", "California", "Florida", "Illinois", "New York"}

# Display total number of states using len() function
print(f"Total number of states: {len(states)}")

# Check if Texas is in the set
print(f"Is Texas in the set? {'Texas' in states}")

# Display states in alphabetical order
print(f"States in alphabetical order: {sorted(states)}")

# Find the longest state name using max() and key=len (to compare based on string length)
longest_state = max(states, key=len)

# Display the length of the longest state name
print(f"Length of the longest state name: {len(longest_state)}")

# Add Georgia to the set
states.add("Georgia")

# Display updated set after adding Georgia
print(f"Updated set after adding Georgia: {states}")

# Remove Florida from the set
states.discard("Florida")

# Display updated set after removing Florida
print(f"Updated set after removing Florida: {states}")

