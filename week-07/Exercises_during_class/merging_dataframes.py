# merging dataframes

import pandas as pd

# DataFrame 1: Students
students = pd.DataFrame({
    "StudentID": [1, 2, 3, 4],
    "Name": ["Amy", "Bob", "Cara", "Dan"]
})

# DataFrame 2: Scores
scores = pd.DataFrame({
    "StudentID": [1, 2, 3, 5],
    "Score": [85, 92, 78, 88]
})

print("STUDENTS DATAFRAME")
print(students)

print("\nSCORES DATAFRAME")
print(scores)

print()

# INNER JOIN
inner_merge = pd.merge(students, scores, on="StudentID", how="inner")
print("\nINNER MERGE (only matching StudentID)")
print(inner_merge)

# LEFT JOIN
left_merge = pd.merge(students, scores, on="StudentID", how="left")
print("\nLEFT MERGE (all students kept)")
print(left_merge)

# RIGHT JOIN
right_merge = pd.merge(students, scores, on="StudentID", how="right")
print("\nRIGHT MERGE (all scores kept)")
print(right_merge)

# OUTER JOIN
outer_merge = pd.merge(students, scores, on="StudentID", how="outer")
print("\nOUTER MERGE (all data from both)")
print(outer_merge)

