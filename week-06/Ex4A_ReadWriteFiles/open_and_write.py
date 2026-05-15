# Exercise 4.A Lab 1

# Open the file in append mode
# If the file doesn't exist, Python will create it
# If the file already exists, Python will add new content to the end
f = open("about_me.txt", "a")

# Add a new line to the file
f.write("\nPerfect night out: Walking through a night market looking for strange herbs, medicines, teas, or unusual ingredients.")

# This will manually close the file
f.close()
