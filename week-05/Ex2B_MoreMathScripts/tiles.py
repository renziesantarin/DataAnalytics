import math

length = 10
width = 12

area = length * width

tiles_needed = area * 1.10  # add 10%

boxes = math.ceil(tiles_needed / 12) 
# using math.ceil to round up since I can only get full boxes
# dividing by 12 since there are 12 tiles per box

print(f"I need {boxes} boxes of tiles")
