# Favorite food list
foods = ["kare-kare", "takoyaki", "ramen", "bruschetta", "carbonara"]

# Loop through the list
# enumerate() gives both the index and the value of each item in the list
# and start=1 makes the index or the numbering to start from 1 instead of 0
# index will temporarily store the number
# food will temporarily store the name of the current item in the list
for index, food in enumerate(foods, start=1):

    # This will check if the current index is 1 to print the top pick note.
    if index == 1:

        print(f"{index}. {food} <- top pick!")
    
    # This is for any item that is not the top pick.
    else:

        print(f"{index}. {food}")

