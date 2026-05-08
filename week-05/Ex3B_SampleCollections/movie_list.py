# Title list of my favorite movies
movies = ["The Avengers", "X-Men: First Class", "Me Before You", "This is Where I Leave You"]

# Prints the sentence in the f-string inclduing the number of 
# movies inside the list using the len() function
print(f"The list movies includes my top {len(movies)} favorite movies.")
# Prints the entire list
print(movies)

print(sorted(movies)) # This sorted the list in alphabetical order
print(movies) # This printed it how I had them in the list

movies.sort() # This rearranged the movies in alphabetical order permanently
print(movies) # This prints the now permanently sorted list

movies.append("Blended") # This would add the movie in the end of the list
movies.sort() # I used this to sort it permanently
print(movies)
print(f"The list movies includes my top {len(movies)} favorite movies.")