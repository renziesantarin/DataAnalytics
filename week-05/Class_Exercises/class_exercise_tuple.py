states = ("New York", "California", "Texas", "Florida", "Illinois")

print(f"Total number of states: {len(states)}")
print(f"First state: {states[0]}")
print(f"Last state: {states[-1]}")
print(f"Is Texas in the tuple? {'Texas' in states}")
print(f"States in alphabetical order: {sorted(states)}")

longest_state = max(states, key=len)
print(f"Longest state name length: {len(longest_state)}")

