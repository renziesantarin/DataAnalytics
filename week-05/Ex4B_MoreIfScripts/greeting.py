# User input
# Convert to int to be able to compare to numbers
hour = int(input("Please enter the hour of the day (0-23): "))

# Determine greeting based on hour
if hour >= 0 and hour < 4:
    print("What are you doing up so late??")
elif hour >= 4 and hour < 10:
    print("Good morning!")
elif hour >= 10 and hour < 17:
    print("Good day!")
else:
    print("Good evening!")
